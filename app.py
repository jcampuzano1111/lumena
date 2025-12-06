# app.py
from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect
)


@app.before_request
def enforce_https_in_production():
    # Railway / proxies usually set X-Forwarded-Proto
    proto = request.headers.get("X-Forwarded-Proto", "http")
    if proto == "http":
        url = request.url.replace("http://", "https://", 1)
        return redirect(url, code=301)
from datetime import date, datetime

# Importa los textos de numerología por idioma
from numerology_texts_en import NUMEROLOGY_TEXTS as NUM_TEXTS_EN
from numerology_texts_es import NUMEROLOGY_TEXTS as NUM_TEXTS_ES


app = Flask(__name__)
app.secret_key = "cambia_esta_clave_super_secreta"


# ---------------------------
# Placeholders para las cards (antes de llenar el formulario)
# ---------------------------
PLACEHOLDER_TEXTS = {
    "es": {
        "life_path": {
            "title": "Sendero de Vida (Life Path)",
            "description": (
                "La misión principal o el camino de la vida. Revela la esencia de tu personalidad, "
                "los talentos innatos y las lecciones mayores que viniste a aprender. Es el número más influyente."
            ),
        },
        "birthday": {
            "title": "Día de Nacimiento (Birth Day Gift)",
            "description": (
                "Un talento o rasgo específico que te acompaña desde el nacimiento. "
                "Actúa como un rasgo de apoyo al Sendero de Vida."
            ),
        },
        "expression": {
            "title": "Número de Expresión / Destino (Expression / Destiny)",
            "description": (
                "Tu potencial y tus habilidades. Representa lo que viniste a hacer con tu vida. "
                "Muestra las herramientas, talentos y la carrera ideal para ti."
            ),
        },
        "soul_urge": {
            "title": "Deseo del Alma (Soul Urge)",
            "description": (
                "Tus deseos, motivaciones e impulsos internos. Es lo que te hace sentir más realizado "
                "y lo que realmente quieres."
            ),
        },
        "personality": {
            "title": "Número de Personalidad (Personality)",
            "description": (
                "La primera impresión que das a los demás. Es la máscara social o la apariencia externa "
                "que proyectas al mundo."
            ),
        },
    },
    "en": {
        "life_path": {
            "title": "Life Path",
            "description": (
                "Your main mission and life direction. It reveals the essence of your personality, "
                "your innate talents, and the major lessons you came to learn. It is the most influential number."
            ),
        },
        "birthday": {
            "title": "Birth Day Gift",
            "description": (
                "A specific talent or trait you carry from birth. "
                "It acts as a supportive quality for your Life Path."
            ),
        },
        "expression": {
            "title": "Expression / Destiny Number",
            "description": (
                "Your potential and abilities. It represents what you came to do with your life and shows "
                "your natural tools, talents, and ideal career direction."
            ),
        },
        "soul_urge": {
            "title": "Soul Urge / Heart’s Desire",
            "description": (
                "Your inner desires, motivations, and impulses. It is what makes you feel most fulfilled "
                "and what you truly long for."
            ),
        },
        "personality": {
            "title": "Personality Number",
            "description": (
                "The first impression you make on others. It is the social mask or outer appearance "
                "you project to the world."
            ),
        },
    },
}


# ---------------------------
# Helpers de idioma
# ---------------------------
def get_current_lang():
    """
    Obtiene el idioma actual:
    - Si viene ?lang=es|en en la URL, se guarda en sesión.
    - Si no, usa lo que esté en sesión o 'en' por defecto.
    """
    lang_param = request.args.get("lang")
    if lang_param in ("en", "es"):
        session["lang"] = lang_param
    return session.get("lang", "en")


def get_texts_for_lang(lang: str) -> dict:
    """
    Devuelve el diccionario de textos de numerología para el idioma dado.

    - En inglés (en): usa NUM_TEXTS_EN tal como viene.
    - En español (es): adapta las claves del archivo numerology_texts_es.py
      (LIFE_PATH_MEANINGS, BIRTHDAY_MEANINGS, etc.) a las claves que el resto
      de la app espera: life_path, birthday, expression, soul_urge, personality.
    """
    lang = (lang or "en").lower()

    if lang == "es":
        es = NUM_TEXTS_ES or {}

        # Normalizamos las claves al mismo esquema que en inglés
        texts_es_normalized = {
            "life_path": es.get("LIFE_PATH_MEANINGS", {}),
            "birthday": es.get("BIRTHDAY_MEANINGS", {}),
            "expression": es.get("EXPRESSION_MEANINGS", {}),
            "soul_urge": es.get("SOUL_URGE_MEANINGS", {}),
            "personality": es.get("PERSONALITY_MEANINGS", {}),
            # Si en el futuro agregas maestros/kármicos en ES, puedes mapealos aquí:
            # "master_numbers": es.get("MASTER_MEANINGS", {}),
            # "karmic_numbers": es.get("KARMIC_MEANINGS", {}),
        }

        return texts_es_normalized

    # Idioma por defecto: inglés
    return NUM_TEXTS_EN



def get_placeholders_for_lang(lang: str) -> dict:
    """
    Devuelve los placeholders de las cards según el idioma.
    """
    return PLACEHOLDER_TEXTS.get(lang, PLACEHOLDER_TEXTS["en"])


# ---------------------------
# Página principal
# ---------------------------
@app.route("/", methods=["GET"])
def index():
    lang = get_current_lang()
    today_str = date.today().isoformat()

    # Antes de llenar el formulario NO hay numerology,
    # así que las cards deben mostrar los placeholders.
    card_placeholders = get_placeholders_for_lang(lang)

    return render_template(
        "index.html",
        lang=lang,
        today=today_str,
        numerology=None,          # <- sin resultados aún
        form_error=None,
        card_placeholders=card_placeholders,
    )


# ---------------------------
# Procesar formulario "Who Am I"
# ---------------------------
@app.route("/who-am-i", methods=["POST"])
def who_am_i():
    lang = get_current_lang()
    today_str = date.today().isoformat()
    card_placeholders = get_placeholders_for_lang(lang)

    # Campos del formulario
    first_name = (request.form.get("first_name") or "").strip()
    second_name = (request.form.get("second_name") or "").strip()
    last_names = (request.form.get("last_names") or "").strip()
    date_of_birth = (request.form.get("date_of_birth") or "").strip()
    country_of_birth = (request.form.get("country_of_birth") or "").strip()

    form_error = None

    # Validaciones básicas
    if not first_name or not last_names or not date_of_birth or not country_of_birth:
        form_error = (
            "Please fill all required fields."
            if lang == "en"
            else "Por favor completa todos los campos obligatorios."
        )
    else:
        try:
            dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
            if dob > date.today():
                form_error = (
                    "Your date of birth cannot be in the future."
                    if lang == "en"
                    else "Tu fecha de nacimiento no puede estar en el futuro."
                )
        except ValueError:
            form_error = (
                "Please enter a valid date."
                if lang == "en"
                else "Por favor ingresa una fecha válida."
            )

    if form_error:
        # No calculamos numerología, solo mostramos error + placeholders
        return render_template(
            "index.html",
            lang=lang,
            today=today_str,
            numerology=None,
            form_error=form_error,
            card_placeholders=card_placeholders,
        )

    # Cálculo de numerología con textos de ES/EN
    numerology = calculate_numerology_with_texts(
        first_name=first_name,
        second_name=second_name,
        last_names=last_names,
        date_of_birth=date_of_birth,
        lang=lang,
    )

    # NOTA: ya no guardamos numerology en sesión; solo mostramos resultado
    return render_template(
        "index.html",
        lang=lang,
        today=today_str,
        numerology=numerology,
        form_error=None,
        card_placeholders=card_placeholders,
    )


# ---------------------------
# Lógica numérica base
# ---------------------------
def reduce_to_digit(n: int) -> int:
    """
    Reduce un número sumando sus dígitos hasta obtener 1–9.
    (Ejemplo simple. Si manejas Números Maestros de otra forma,
    aquí puedes ajustar la lógica).
    """
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


# ---------------------------
# Helper: construcción de cada bloque con textos
# ---------------------------
def build_number_block(
    kind: str,
    number: int,
    texts: dict,
    default_title_en: str,
    default_title_es: str,
    lang: str,
):
    """
    kind: 'life_path', 'birthday', 'expression', 'soul_urge', 'personality'
    number: número calculado (1–9)
    texts: diccionario NUMEROLOGY_TEXTS del idioma
    """

    # Bloque general por tipo (life_path, birthday, etc.)
    by_kind = texts.get(kind, {}) or {}

    # Puede venir como {"numbers": {4: {...}}} o {"numbers": {"4": {...}}}
    raw_numbers = by_kind.get("numbers", {}) if isinstance(by_kind, dict) else {}

    # Normalizamos para aceptar keys int y str indistintamente
    numbers_dict = {}
    for k, v in raw_numbers.items():
        if isinstance(k, int):
            numbers_dict[k] = v
            numbers_dict[str(k)] = v
        else:
            numbers_dict[k] = v
            try:
                ik = int(k)
                numbers_dict[ik] = v
            except (ValueError, TypeError):
                pass

    # Recuperar data del número (soporta clave int o str)
    data = numbers_dict.get(number) or numbers_dict.get(str(number)) or {}

    # ---------- TÍTULO ----------
    title = (
        data.get("title")
        or data.get("titulo")
        or data.get("gift")  # added this
        or (default_title_es if lang == "es" else default_title_en)
    )

    # ---------- DESCRIPCIÓN DE CATEGORÍA (texto pequeño arriba) ----------
    category_description = (
        by_kind.get("description")
        or by_kind.get("descripcion")
        or ""
    )

    # ---------- CAMPOS ESPECÍFICOS ----------
    meaning = data.get("meaning") or data.get("significado") or ""
    essence = data.get("essence") or data.get("esencia") or ""
    gift = data.get("gift") or data.get("don") or ""
    lesson = data.get("lesson") or data.get("leccion") or ""
    shadow = data.get("shadow") or data.get("sombra") or ""

    # Texto largo principal
    expanded = (
        data.get("expanded")
        or data.get("detalles")
        or data.get("texto_largo")
        or data.get("talent")
        or data.get("manifestation")
        or meaning
        or ""
    )

    return {
        "number": number,
        "title": title,
        "label": by_kind.get("label", "") or by_kind.get("etiqueta", ""),
        "category_description": category_description,
        "meaning": meaning,
        "essence": essence,
        "gift": gift,
        "lesson": lesson,
        "shadow": shadow,
        "expanded": expanded,
    }



# ---------------------------
# Cálculo de numerología con textos ES/EN
# ---------------------------
def calculate_numerology_with_texts(first_name, second_name, last_names, date_of_birth, lang="en"):
    texts = get_texts_for_lang(lang)

    # --- Números base (puedes reemplazar por tu lógica real) ---
    dob_digits = [int(c) for c in date_of_birth if c.isdigit()]
    lp_number = reduce_to_digit(sum(dob_digits))

    day = int(date_of_birth.split("-")[2])
    bd_number = reduce_to_digit(day)

    full_name = f"{first_name} {second_name} {last_names}".strip().upper()
    letter_values = {c: (i % 9) + 1 for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

    expr_sum = sum(letter_values.get(c, 0) for c in full_name if c.isalpha())
    ex_number = reduce_to_digit(expr_sum)

    vowels = "AEIOU"
    su_sum = sum(letter_values.get(c, 0) for c in full_name if c in vowels)
    su_number = reduce_to_digit(su_sum) if su_sum > 0 else 0

    pe_sum = sum(
        letter_values.get(c, 0)
        for c in full_name
        if c.isalpha() and c not in vowels
    )
    pe_number = reduce_to_digit(pe_sum) if pe_sum > 0 else 0

    # --- Construcción de bloques usando numerology_texts_xx.py ---
    life_path = build_number_block(
        kind="life_path",
        number=lp_number,
        texts=texts,
        default_title_en="Life Path",
        default_title_es="Camino de Vida",
        lang=lang,
    )

    birthday = build_number_block(
        kind="birthday",
        number=bd_number,
        texts=texts,
        default_title_en="Birth Day Gift",
        default_title_es="Regalo de tu día de nacimiento",
        lang=lang,
    )

    expression = build_number_block(
        kind="expression",
        number=ex_number,
        texts=texts,
        default_title_en="Expression / Destiny",
        default_title_es="Número de Expresión / Destino",
        lang=lang,
    )

    soul_urge = build_number_block(
        kind="soul_urge",
        number=su_number,
        texts=texts,
        default_title_en="Soul Urge",
        default_title_es="Número del Alma",
        lang=lang,
    )

    personality = build_number_block(
        kind="personality",
        number=pe_number,
        texts=texts,
        default_title_en="Personality",
        default_title_es="Número de Personalidad",
        lang=lang,
    )

    # --- Números especiales (Master / Kármicos) si los definiste en los textos ---
    special_numbers = []
    master_details = []
    karmic_details = []

    master_texts = texts.get("master_numbers", {})
    karmic_texts = texts.get("karmic_numbers", {})

    core_numbers = {
        "life_path": lp_number,
        "birthday": bd_number,
        "expression": ex_number,
        "soul_urge": su_number,
        "personality": pe_number,
    }

    for n in set(core_numbers.values()):
        if n in master_texts:
            special_numbers.append(n)
            master_details.append({
                "number": n,
                "data": master_texts[n],
            })
        if n in karmic_texts:
            special_numbers.append(n)
            karmic_details.append({
                "number": n,
                "description": karmic_texts[n].get("description", ""),
            })

    special_numbers = sorted(set(special_numbers))

    numerology = {
        "life_path": life_path,
        "birthday": birthday,
        "expression": expression,
        "soul_urge": soul_urge,
        "personality": personality,
        "special_numbers": special_numbers,
        "master_details": master_details,
        "karmic_details": karmic_details,
    }

    return numerology


if __name__ == "__main__":
    app.run(debug=True)




