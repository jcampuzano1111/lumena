# numerology_texts_es.py
# -*- coding: utf-8 -*-
"""
Textos y significados de numerología para AURA.

Aquí centralizamos todo el contenido descriptivo para mantener app.py limpio.
"""

NUMEROLOGY_TEXTS = {
    # ============================================================
    # CAMINO DE VIDA (LIFE PATH)
    # ============================================================
    "LIFE_PATH_MEANINGS": {
        "label": "Camino de Vida",
        "description": (
            "El Camino de Vida se calcula a partir de tu fecha completa de nacimiento. "
            "Es el eje central de tu mapa numerológico: revela la dirección general de tu existencia, "
            "las lecciones principales y el tipo de experiencias que tu alma vino a vivir."
        ),
        "numbers": {
            1: {
                "title": "Camino de Vida 1 – El Líder Pionero",
                "essence": "Camino de liderazgo, iniciativa y autonomía. Vida que te invita a abrir camino y tomar decisiones.",
                "expanded": """Tu misión es ser pionero, innovador y líder natural. Naciste para iniciar proyectos, 
abrir nuevos caminos y confiar en tu propia visión. Este camino te enseña independencia, coraje y 
autoconfianza.

Aprendes a ser el número uno sin aplastar a otros, a tomar la iniciativa sin imponerte. Tu poder está 
en tu originalidad y en tu capacidad de comenzar desde cero, incluso cuando otros dudan.

Retos principales:
- Impaciencia
- Autoritarismo
- Aislamiento por exceso de independencia

Regalos y talentos:
- Valentía
- Iniciativa
- Capacidad de liderar e inspirar a otros

Camino profesional sugerido:
- Emprendimiento
- Dirección ejecutiva
- Política
- Deportes competitivos
- Innovación y startups"""
            },
            2: {
                "title": "Camino de Vida 2 – El Mediador",
                "essence": "Camino de cooperación, sensibilidad y construcción de puentes.",
                "expanded": """Tu vida gira en torno a la colaboración, la empatía y la creación de armonía. 
Viniste a unir, no a separar. Tu presencia suaviza tensiones y facilita acuerdos.

Aprendes a escuchar profundamente, a leer las emociones sutiles y a crear espacios de paz. 
Tu mayor reto es no perderte en las necesidades de otros y recordar tus propios límites.

Retos principales:
- Evitar la dependencia emocional
- No huir del conflicto por miedo
- No reprimir lo que realmente sientes

Regalos y talentos:
- Diplomacia
- Escucha profunda
- Capacidad para mediar conflictos

Camino profesional sugerido:
- Recursos humanos
- Consejería
- Terapia
- Mediación
- Trabajo en equipo y relaciones públicas"""
            },
            3: {
                "title": "Camino de Vida 3 – El Comunicador Creativo",
                "essence": "Camino de expresión, alegría y creatividad.",
                "expanded": """Viniste a expresarte: con la voz, la escritura, el arte, el humor o el cuerpo. 
Tu energía está diseñada para inspirar, alegrar y dar color a la vida de otros.

Aprendes a confiar en tu voz interna, a no censurarte por miedo al juicio y a usar tu creatividad 
de forma madura, no solo como escape.

Retos principales:
- Superficialidad
- Dispersión
- Miedo a ser juzgado que bloquea tu expresión

Regalos y talentos:
- Carisma
- Sentido del humor
- Talentos artísticos y comunicativos

Camino profesional sugerido:
- Arte y entretenimiento
- Contenido digital
- Marketing
- Enseñanza creativa
- Comunicación en general"""
            },
            4: {
                "title": "Camino de Vida 4 – El Constructor",
                "essence": "Camino de estructura, disciplina y trabajo constante.",
                "expanded": """Viniste a construir bases sólidas: proyectos, empresas, familias, estructuras 
que duren. Tu vida te enseña el valor de la constancia, el orden y la responsabilidad.

Aprendes a confiar en el proceso paso a paso, a honrar el trabajo bien hecho y a no temer al esfuerzo.

Retos principales:
- Rigidez
- Exceso de control
- Miedo al cambio

Regalos y talentos:
- Organización
- Paciencia
- Perseverancia

Camino profesional sugerido:
- Administración
- Ingeniería
- Gestión de proyectos
- Operaciones
- Contabilidad y áreas técnicas"""
            },
            5: {
                "title": "Camino de Vida 5 – El Explorador",
                "essence": "Camino de libertad, cambio y experiencias intensas.",
                "expanded": """Viniste a explorar, moverte, cambiar y aprender a través de la experiencia directa. 
Tu vida rara vez es lineal; está llena de giros, viajes, cambios y sorpresas.

Aprendes a amar la libertad sin convertirla en fuga, y a usar el cambio como herramienta de crecimiento.

Retos principales:
- Inquietud extrema
- Falta de compromiso
- Búsqueda constante de estimulación

Regalos y talentos:
- Adaptabilidad
- Versatilidad
- Carisma social

Camino profesional sugerido:
- Viajes
- Ventas
- Marketing
- Periodismo
- Consultoría y trabajos dinámicos"""
            },
            6: {
                "title": "Camino de Vida 6 – El Cuidador",
                "essence": "Camino de amor, responsabilidad afectiva y armonía.",
                "expanded": """Tu vida gira en torno al cuidado, la familia, la comunidad y la creación de belleza. 
Tienes un llamado profundo a servir, proteger y embellecer el mundo que te rodea.

Aprendes a cuidar sin sacrificarte por completo, y a amar sin caer en la sobreprotección.

Retos principales:
- Perfeccionismo
- Sacrificio excesivo
- Carga de responsabilidades ajenas

Regalos y talentos:
- Gran capacidad de cuidado y contención
- Sentido estético
- Vocación de servicio

Camino profesional sugerido:
- Educación
- Salud
- Diseño
- Trabajo social
- Terapias y oficios de servicio"""
            },
            7: {
                "title": "Camino de Vida 7 – El Buscador",
                "essence": "Camino de introspección, sabiduría y profundidad espiritual.",
                "expanded": """Viniste a buscar la verdad, más allá de lo obvio. Tu vida te lleva a explorar 
la mente, el alma, la ciencia, la filosofía o la espiritualidad.

Aprendes a confiar en tu intuición, a integrar razón y misterio, y a disfrutar de tu propio mundo interno.

Retos principales:
- Aislamiento
- Escepticismo extremo
- Desconexión emocional

Regalos y talentos:
- Capacidad analítica profunda
- Intuición
- Conexión con lo espiritual

Camino profesional sugerido:
- Investigación
- Ciencia
- Psicología
- Filosofía
- Espiritualidad y análisis de datos"""
            },
            8: {
                "title": "Camino de Vida 8 – El Gestor de Poder",
                "essence": "Camino de logro material, liderazgo y poder bien usado.",
                "expanded": """Tu vida te enseña a relacionarte con el poder, el dinero y la autoridad. 
Viniste a aprender a crear abundancia y a usarla con integridad.

Aprendes a liderar sin dominar, a lograr sin destruir, y a honrar el valor del trabajo y la recompensa.

Retos principales:
- Ambición desmedida
- Control
- Conflictos de poder

Regalos y talentos:
- Visión estratégica
- Liderazgo ejecutivo
- Capacidad de generar recursos

Camino profesional sugerido:
- Negocios
- Finanzas
- Dirección ejecutiva
- Emprendimiento
- Alta gestión"""
            },
            9: {
                "title": "Camino de Vida 9 – El Humanitario",
                "essence": "Camino de servicio, cierre de ciclos y amor universal.",
                "expanded": """Tu vida tiene un tono de cierre, síntesis y servicio a algo más grande que tú. 
Viniste a aprender a soltar, a perdonar y a servir a la humanidad.

Aprendes a transformar el dolor en compasión, y las pérdidas en sabiduría.

Retos principales:
- Apegos al pasado
- Martirio emocional
- Idealismo doloroso

Regalos y talentos:
- Gran sensibilidad
- Vocación de servicio
- Capacidad de inspirar desde la experiencia

Camino profesional sugerido:
- ONGs y trabajo social
- Medicina y salud
- Arte con mensaje
- Educación transformadora"""
            },
            11: {
                "title": "Camino de Vida 11 – El Maestro Intuitivo",
                "essence": "Camino maestro de intuición, sensibilidad espiritual e inspiración.",
                "expanded": """El 11 es un Camino Maestro de alta sensibilidad, intuición y conexión espiritual. 
Viniste a iluminar, inspirar y elevar la consciencia de otros.

Tu vida rara vez es simple: está llena de intensidades, despertares y pruebas profundas que activan tu maestría.

Reto central:
- Manejar tu hipersensibilidad sin quebrarte
- Anclarte en la realidad mientras recibes tanta información sutil"""
            },
            22: {
                "title": "Camino de Vida 22 – El Maestro Constructor",
                "essence": "Camino maestro de manifestación a gran escala.",
                "expanded": """El 22 combina la visión espiritual con la capacidad de construir estructuras 
concretas de gran impacto. Viniste a materializar proyectos grandes al servicio de muchos.

Reto central:
- No paralizarte por la magnitud de tu visión
- Recordar que los legados se construyen paso a paso"""
            },
            33: {
                "title": "Camino de Vida 33 – El Maestro Sanador",
                "essence": "Camino maestro de amor incondicional y sanación colectiva.",
                "expanded": """El 33 es el maestro del amor y del servicio. Viniste a sanar, contener y elevar 
emocional y espiritualmente a otros.

Reto central:
- Aprender límites sanos
- Cuidarte a ti mismo mientras cuidas a otros"""
            },
        },
    },

    # ============================================================
    # DÍA DE NACIMIENTO (BIRTHDAY)
    # ============================================================
    "BIRTHDAY_MEANINGS": {
        "label": "Día de Nacimiento",
        "description": (
            "El día exacto en que naciste revela un don especial, un talento natural que llevas desde el inicio. "
            "Es tu herramienta primaria para cumplir tu Camino de Vida."
        ),
        "numbers": {
            1: {
                "gift": "Don de Iniciativa",
                "description": "Día de pionero: iniciativa fuerte, individualidad marcada y deseo de ir primero.",
                "talent": """Posees un coraje natural para comenzar cosas nuevas. No esperas a que otros tomen 
la delantera; tu instinto te impulsa a ser el primero. Este don te hace excelente para abrir 
caminos donde no los hay.

MANIFESTACIÓN DEL DON: Desde niño mostraste independencia marcada. Eres de los que levantan 
la mano primero, toman la iniciativa en proyectos, y no temen comenzar desde cero. Tu energía 
es de arranque, de motor, de quien enciende el fuego.

APLICACIÓN PRÁCTICA: Úsalo para emprendimientos, liderazgo de equipos, innovación, o cualquier 
área que requiera valentía para ir donde nadie ha ido. Tu don natural es vencer el miedo inicial 
que paraliza a otros. Excelente para: startups, proyectos innovadores, exploración de territorios 
nuevos (literal o metafórico).

DESAFÍO: Aprender a sostener lo que inicias. A veces tu don es comenzar, no terminar. Necesitas 
rodearte de quienes complementen tu inicio con seguimiento."""
            },
            2: {
                "gift": "Don de Mediación",
                "description": "Día de mediador: sensibilidad, cuidado por el otro y energía cooperativa.",
                "talent": """Tienes una habilidad innata para percibir las necesidades emocionales de otros y 
crear puentes entre personas. Tu sensibilidad es tu superpoder diplomático.

MANIFESTACIÓN DEL DON: Desde pequeño fuiste el que notaba cuando alguien estaba triste, el que 
unía a grupos separados, el que encontraba soluciones que satisfacían a todos. Percibes energías 
sutiles que otros no captan. Eres el termómetro emocional de cualquier grupo.

APLICACIÓN PRÁCTICA: Úsalo en mediación de conflictos, recursos humanos, terapia, consejería, 
diplomacia, o cualquier campo donde se requiera crear armonía entre personas o grupos. Tu don 
es ver ambos lados sin perder objetividad. Excelente para: negociación, resolución de conflictos, 
crear equipos cohesionados, terapia de parejas.

DESAFÍO: No perderte en las emociones ajenas. Tu sensibilidad puede agotarte si no estableces 
límites energéticos claros. Aprende a sentir sin absorber."""
            },
            3: {
                "gift": "Don de Expresión",
                "description": "Día expresivo: carisma, comunicación y creatividad natural.",
                "talent": """Naciste con el don de la palabra, el arte o cualquier forma de expresión creativa. 
Tu presencia ilumina ambientes y tu creatividad fluye sin esfuerzo.

MANIFESTACIÓN DEL DON: Desde niño fuiste el alma de las reuniones, el que contaba historias, 
el que hacía reír o conmover. Tu energía es magnética, atractiva, inspiradora. Tienes facilidad 
natural para comunicar ideas complejas de manera simple y cautivadora.

APLICACIÓN PRÁCTICA: Úsalo en comunicación (oratoria, escritura, periodismo), arte (cualquier 
forma), entretenimiento, enseñanza, o cualquier campo donde inspirar y conectar con otros sea 
esencial. Tu don es hacer que la gente SIENTA algo. Excelente para: presentaciones públicas, 
creación de contenido, arte performático, educación creativa, marketing emocional.

DESAFÍO: Evitar la superficialidad. Tu don te permite brillar fácilmente, pero el reto es 
agregar profundidad a tu brillo. No te quedes solo en la superficie encantadora."""
            },
            4: {
                "gift": "Don de Estructura",
                "description": "Día estable: sentido del deber, orden y practicidad.",
                "talent": """Posees una capacidad natural para organizar, planificar y construir sistemas que 
funcionen. Ves el orden donde otros ven caos.

MANIFESTACIÓN DEL DON: Desde pequeño fuiste el organizado, el que hacía listas, el que terminaba 
lo que empezaba. Tienes visión arquitectónica: ves cómo las piezas se ensamblan para formar 
estructuras sólidas. Tu mente naturalmente ordena, clasifica y sistematiza.

APLICACIÓN PRÁCTICA: Úsalo en gestión de proyectos, administración, construcción (física o 
conceptual), contabilidad, ingeniería, o cualquier campo que requiera crear sistemas confiables. 
Tu don es convertir caos en cosmos, desorden en estructura funcional. Excelente para: 
planificación estratégica, logística, gestión de operaciones, creación de procesos eficientes.

DESAFÍO: Evitar la rigidez excesiva. Tu amor por el orden puede convertirse en inflexibilidad. 
Aprende que a veces el caos creativo es necesario para la innovación."""
            },
            5: {
                "gift": "Don de Adaptabilidad",
                "description": "Día inquieto: gusto por el cambio, la aventura y la experiencia directa.",
                "talent": """Tienes una versatilidad excepcional y una capacidad única de adaptarte a cualquier 
circunstancia. El cambio no te asusta, te energiza.

MANIFESTACIÓN DEL DON: Desde niño fuiste el curioso insaciable, el que quería probar todo, 
el que se adaptaba fácilmente a nuevos ambientes. Tienes una flexibilidad natural que te permite 
prosperar en situaciones que paralizarían a otros. Tu energía es como el agua: fluye y se adapta.

APLICACIÓN PRÁCTICA: Úsalo en campos que requieran versatilidad: ventas, viajes, periodismo, 
consultoría, traducción, trabajo multicultural, o cualquier área que demande adaptación constante. 
Tu don es reinventarte y prosperar en la incertidumbre. Excelente para: exploración de mercados 
nuevos, gestión de crisis, trabajo internacional, innovación disruptiva.

DESAFÍO: Evitar la dispersión o la falta de compromiso. Tu facilidad para adaptarte puede 
llevarte a no profundizar en nada. Aprende a elegir batallas donde enfocar tu versatilidad."""
            },
            6: {
                "gift": "Don de Cuidado",
                "description": "Día protector: foco en familia, cuidado y responsabilidad afectiva.",
                "talent": """Naciste con un corazón que naturalmente nutre y protege. Tienes el don de crear 
armonía y hacer sentir a otros seguros y amados.

MANIFESTACIÓN DEL DON: Desde pequeño fuiste el cuidador, el que se preocupaba por otros, el 
que creaba ambientes acogedores. Tienes una capacidad natural para detectar necesidades afectivas 
y responder con amor práctico. Tu presencia es como un abrazo: cálida, segura, nutritiva.

APLICACIÓN PRÁCTICA: Úsalo en educación, sanación, consejería, diseño de espacios (interiores), 
gastronomía, trabajo comunitario, o cualquier campo donde cuidar del bienestar ajeno sea central. 
Tu don es crear hogar, literal o metafórico. Excelente para: terapia familiar, trabajo social, 
enfermería, creación de comunidades, hospitalidad.

DESAFÍO: Evitar el sacrificio extremo o la sobreprotección. Tu don puede convertirse en 
codependencia si no estableces límites. Aprende que cuidar bien incluye permitir que otros 
aprendan de sus errores."""
            },
            7: {
                "gift": "Don de Profundidad",
                "description": "Día analítico: mente profunda, observadora y espiritualidad latente.",
                "talent": """Posees una mente que ve más allá de lo superficial. Tu intuición y capacidad 
analítica te permiten comprender misterios que otros no perciben.

MANIFESTACIÓN DEL DON: Desde niño fuiste el observador silencioso, el que hacía preguntas 
profundas, el que necesitaba entender el "por qué" de todo. Tienes una mente investigadora 
natural y una conexión especial con lo intangible. Tu percepción capta capas de realidad que 
otros no ven.

APLICACIÓN PRÁCTICA: Úsalo en investigación, análisis, espiritualidad, psicología, filosofía, 
ciencia, o cualquier campo que requiera penetrar bajo la superficie. Tu don es descubrir verdades 
ocultas y conectar con sabiduría profunda. Excelente para: investigación científica, análisis de 
datos complejos, consejería espiritual, detección de patrones, escritura filosófica.

DESAFÍO: Evitar el aislamiento excesivo o el escepticismo paralizante. Tu profundidad puede 
alejarte de la conexión humana básica. Aprende a compartir tu sabiduría sin arrogancia."""
            },
            8: {
                "gift": "Don de Gestión",
                "description": "Día de logro: impulso a liderar, emprender y gestionar recursos.",
                "talent": """Tienes un talento natural para gestionar recursos, liderar equipos y crear 
abundancia material. El poder te viene naturalmente.

MANIFESTACIÓN DEL DON: Desde niño mostraste capacidad organizativa y sentido de autoridad. 
Entiendes instintivamente cómo funcionan sistemas de poder, dinero y gestión. Tienes visión 
estratégica natural y habilidad para convertir ideas en empresas rentables. Tu energía es 
ejecutiva, eficiente, orientada a resultados.

APLICACIÓN PRÁCTICA: Úsalo en negocios, finanzas, administración ejecutiva, bienes raíces, 
emprendimiento, o cualquier campo donde gestionar recursos y personas sea clave. Tu don es 
crear abundancia y estructuras de poder sostenibles. Excelente para: dirección de empresas, 
inversiones, negociación de alto nivel, gestión de grandes presupuestos, emprendimiento escalable.

DESAFÍO: Evitar el materialismo extremo o el abuso de poder. Tu don puede convertirse en 
tiranía o adicción al dinero. Aprende a usar tu poder para elevar, no solo para acumular."""
            },
            9: {
                "gift": "Don de Compasión",
                "description": "Día humanitario: sensibilidad, empatía y vocación de servicio.",
                "talent": """Naciste con un corazón universal capaz de sentir el dolor del mundo y el impulso 
de sanarlo. Tu compasión es tu herramienta transformadora.

MANIFESTACIÓN DEL DON: Desde pequeño sentiste el sufrimiento ajeno como propio. Tienes una 
empatía que trasciende fronteras personales, culturales o nacionales. Tu corazón ve la humanidad 
completa como familia. Posees sabiduría emocional natural y capacidad de perdón profunda.

APLICACIÓN PRÁCTICA: Úsalo en trabajo humanitario, ONGs, medicina, psicología transpersonal, 
arte sanador, activismo social, o cualquier campo donde aliviar sufrimiento colectivo sea el 
objetivo. Tu don es ver la unidad más allá de las diferencias. Excelente para: cooperación 
internacional, trabajo con refugiados, sanación comunitaria, arte con mensaje social, educación 
para la paz.

DESAFÍO: Evitar el martirio o la identificación con el sufrimiento. Tu compasión puede agotarte 
si no aprendes límites sanos. No puedes salvar al mundo, pero sí puedes iluminarlo."""
            },
            11: {
                "gift": "Don de Intuición",
                "description": "Día maestro intuitivo: percepción fina, inspiración y fuerte vida interior.",
                "talent": """Posees una intuición extraordinaria y capacidad de conectar con dimensiones sutiles. 
Eres un canal natural de inspiración elevada.

MANIFESTACIÓN DEL DON: Desde niño fuiste "diferente": hipersensible, perceptivo, capaz de saber 
cosas sin explicación lógica. Tienes conexión directa con tu guía interior y con frecuencias 
elevadas de consciencia. Tu sistema nervioso es como una antena refinada que capta señales sutiles.

APLICACIÓN PRÁCTICA: Úsalo en espiritualidad, sanación energética, arte visionario, coaching 
transformacional, escritura inspirada, o cualquier campo donde canalizar energía elevada sea 
esencial. Tu don es ser puente entre lo invisible y lo visible. Excelente para: guía espiritual, 
sanación intuitiva, arte que eleva consciencia, consejería de alma, enseñanza de desarrollo personal.

DESAFÍO: Manejar tu hipersensibilidad sin quebrarte. Tu sistema nervioso necesita cuidados 
especiales. Aprende prácticas de enraizamiento y protección energética para no agotarte."""
            },
            22: {
                "gift": "Don de Manifestación",
                "description": "Día maestro constructor: capacidad de organizar y concretar grandes proyectos.",
                "talent": """Tienes el raro don de convertir visiones en realidades tangibles de gran escala. 
Combinas idealismo con pragmatismo magistral.

MANIFESTACIÓN DEL DON: Desde joven mostraste capacidad excepcional para organizar, planificar 
y ejecutar proyectos grandes. Ves el panorama completo Y los detalles necesarios simultáneamente. 
Tu mente es arquitectónica a nivel maestro: construyes imperios, no solo casas.

APLICACIÓN PRÁCTICA: Úsalo en proyectos de gran impacto social, construcción de organizaciones 
globales, arquitectura de sistemas complejos, dirección de movimientos sociales, o cualquier 
campo donde manifestar visiones colectivas sea el objetivo. Tu don es hacer real lo que otros 
solo sueñan. Excelente para: fundación de empresas con impacto social, liderazgo de movimientos 
transformadores, proyectos de infraestructura masiva, innovación sistémica.

DESAFÍO: No abrumarte por la magnitud de tu visión. Aprende a dividir tus grandes sueños en 
pasos manejables. Tu don es potente pero requiere paciencia para materializarse."""
            },
            33: {
                "gift": "Don de Sanación",
                "description": "Día maestro sanador: energía de servicio amoroso, vocación de ayuda.",
                "talent": """Naciste con una presencia naturalmente sanadora. Tu energía tiene el poder de 
transformar y elevar a quienes te rodean.

MANIFESTACIÓN DEL DON: Desde niño, tu sola presencia calmaba a otros. Tienes una cualidad 
energética especial que hace que las personas se sientan seguras, vistas y amadas cerca de ti. 
Tu corazón es un portal de amor incondicional que sana sin necesidad de palabras.

APLICACIÓN PRÁCTICA: Úsalo en sanación (de cualquier tipo), maestría espiritual, terapia 
profunda, trabajo con trauma colectivo, arte sanador, o cualquier campo donde tu presencia 
amorosa sea el agente transformador principal. Tu don no es tanto lo que haces, sino lo que ERES. 
Excelente para: terapia holística, liderazgo compasivo, creación de espacios de sanación colectiva, 
consejería de alto nivel, enseñanza espiritual profunda.

DESAFÍO: Cuidar al cuidador. Tu don puede agotarte emocionalmente si das sin límites. Aprende 
que cuidarte a ti mismo no es egoísmo, es necesidad para sostener tu misión."""
            },
        },
    },

    # ============================================================
    # NÚMERO DE EXPRESIÓN / DESTINO (EXPRESSION)
    # ============================================================
    "EXPRESSION_MEANINGS": {
        "label": "Número de Expresión / Destino",
        "description": (
            "Calculado desde tu nombre completo, revela cómo te manifiestas en el mundo, "
            "tus talentos naturales y la manera en que cumples tu propósito. "
            "Es la energía que proyectas y cómo otros experimentan tu esencia."
        ),
        "numbers": {
            1: {
                "essence": "Expresión de líder directo, independiente y orientado a objetivos.",
                "manifestation": """Te manifiestas con autoridad natural, iniciativa y valentía. Tu destino 
involucra ser pionero y abrir caminos para otros.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de comandante natural. Cuando entras a un espacio, 
tu presencia comunica liderazgo sin necesidad de anunciarlo. Hablas con claridad y decisión. 
Actúas con confianza y rapidez. Tu estilo es directo, sin rodeos, yendo al grano. No esperas 
que otros te digan qué hacer; tomas la iniciativa automáticamente.

TALENTOS NATURALES:
- Capacidad de tomar decisiones rápidas y asertivas bajo presión
- Habilidad para iniciar proyectos y motivar a otros a seguirte
- Coraje natural para enfrentar desafíos que intimidan a otros
- Pensamiento independiente: no necesitas aprobación externa
- Innovación: ves soluciones originales donde otros ven problemas

TU DESTINO Y PROPÓSITO: Estás aquí para LIDERAR, no para seguir. Tu nombre te programa para 
abrir caminos nuevos, ser el primero en territorio inexplorado, y mostrar a otros que lo 
imposible es posible. Tu legado serán las puertas que abriste y los caminos que marcaste.

EN EL TRABAJO: Te destacas en roles de liderazgo, emprendimiento, dirección ejecutiva, o 
cualquier posición donde tu autonomía y capacidad de decisión sean esenciales.

EN RELACIONES: Te expresas con honestidad directa. Valoras la independencia mutua. Necesitas 
una pareja que respete tu necesidad de liderar sin competir por poder.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de fuego: enciende, inicia, transforma. 
Cada vez que alguien pronuncia tu nombre, invoca energía de liderazgo y acción."""
            },
            2: {
                "essence": "Expresión conciliadora, empática y cooperativa.",
                "manifestation": """Te manifiestas creando puentes, armonía y unión. Tu destino involucra 
traer paz y equilibrio a situaciones conflictivas.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de mediador natural. Cuando entras a un espacio, 
tu presencia suaviza tensiones. Hablas con diplomacia y sensibilidad. Actúas considerando 
el impacto emocional en otros. Tu estilo es cooperativo, buscando ganar-ganar y creando consenso. 
Escuchas profundamente antes de hablar.

TALENTOS NATURALES:
- Empatía excepcional: sientes las emociones de otros como propias
- Habilidad para mediar conflictos encontrando soluciones que satisfacen a todos
- Intuición social: sabes qué decir y cuándo decirlo
- Capacidad de colaboración: trabajas excepcionalmente bien en equipo
- Sensibilidad artística: especialmente música y ritmo

TU DESTINO Y PROPÓSITO: Estás aquí para UNIR, no para dividir. Tu nombre te programa para 
crear armonía donde hay discordia, construir puentes donde hay separación, y recordar a otros 
el valor de la cooperación. Tu legado serán las relaciones que sanaste y la paz que creaste.

EN EL TRABAJO: Te destacas en recursos humanos, mediación, consejería, trabajo en equipo, 
diplomacia, o cualquier rol donde tu sensibilidad y habilidad para crear armonía sean valiosas.

EN RELACIONES: Te expresas con ternura y comprensión profunda. Valoras la intimidad emocional. 
Necesitas una pareja que aprecie tu sensibilidad sin aprovecharse de tu tendencia a complacer.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de agua: fluye, adapta, nutre. Cada vez 
que alguien pronuncia tu nombre, invoca energía de paz y conexión."""
            },
            3: {
                "essence": "Expresión creativa, artística y comunicadora.",
                "manifestation": """Te manifiestas a través de la palabra, el arte y la alegría. Tu destino 
involucra inspirar y alegrar la vida de otros.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de artista natural. Cuando entras a un espacio, 
tu presencia ilumina el ambiente. Hablas con color y expresividad. Actúas con espontaneidad 
creativa. Tu estilo es alegre, inspirador, contagioso. Comunicas ideas de manera que otros 
las SIENTEN, no solo las entienden.

TALENTOS NATURALES:
- Expresión artística en múltiples formas: palabra, imagen, sonido, movimiento
- Capacidad de comunicar ideas complejas de manera simple y atractiva
- Optimismo natural que eleva el ánimo de grupos enteros
- Creatividad desbordante: ves posibilidades donde otros ven límites
- Magnetismo personal: atraes a otros con tu energía vibrante

TU DESTINO Y PROPÓSITO: Estás aquí para INSPIRAR y ALEGRAR, no para conformarte con lo gris. 
Tu nombre te programa para traer belleza, creatividad y júbilo al mundo. Tu legado será la 
inspiración que dejaste y los corazones que alegraste con tu expresión auténtica.

EN EL TRABAJO: Te destacas en comunicación, arte, entretenimiento, escritura, diseño, enseñanza 
creativa, o cualquier campo donde tu expresión y creatividad sean el producto principal.

EN RELACIONES: Te expresas con pasión y romance. Valoras la diversión y la expresión emocional. 
Necesitas una pareja que celebre tu creatividad sin intentar “seriarte” o limitarte.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de luz: brilla, expande, contagia. Cada 
vez que alguien pronuncia tu nombre, invoca energía de alegría y creatividad."""
            },
            4: {
                "essence": "Expresión organizada, práctica y confiable.",
                "manifestation": """Te manifiestas construyendo estructuras sólidas y siendo un pilar de 
confianza. Tu destino involucra crear fundamentos duraderos.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de constructor natural. Cuando entras a un espacio, 
tu presencia comunica estabilidad y orden. Hablas con precisión y practicidad. Actúas con 
método y disciplina. Tu estilo es sistemático, confiable, paso a paso. Construyes todo lo que 
tocas: proyectos, relaciones, rutinas.

TALENTOS NATURALES:
- Capacidad organizativa excepcional: ves cómo las piezas encajan
- Disciplina férrea: terminas lo que comienzas sin importar obstáculos
- Pensamiento práctico: conviertes ideas abstractas en planes ejecutables
- Confiabilidad absoluta: cuando prometes, cumples
- Paciencia para trabajos de largo plazo que otros abandonarían

TU DESTINO Y PROPÓSITO: Estás aquí para CONSTRUIR, no para improvisar. Tu nombre te programa 
para crear estructuras, sistemas y fundamentos que perduren más allá de tu vida. Tu legado 
será lo que construiste con tus manos, tu mente y tu determinación.

EN EL TRABAJO: Te destacas en gestión de proyectos, ingeniería, administración, construcción, 
contabilidad, o cualquier rol donde el orden, la precisión y la confiabilidad sean críticos.

EN RELACIONES: Te expresas con lealtad y compromiso profundo. Valoras la estabilidad y las 
rutinas compartidas. Necesitas una pareja que valore tu constancia sin aburrirse de tu estructura.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de tierra: sostiene, construye, perdura. 
Cada vez que alguien pronuncia tu nombre, invoca energía de estabilidad y estructura."""
            },
            5: {
                "essence": "Expresión libre, versátil y amante de la diversidad.",
                "manifestation": """Te manifiestas con libertad, adaptabilidad y magnetismo. Tu destino 
involucra expandir horizontes y conectar diferentes mundos.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de explorador natural. Cuando entras a un espacio, 
tu presencia trae aire fresco y posibilidad. Hablas con versatilidad y entusiasmo. Actúas con 
espontaneidad y adaptabilidad. Tu estilo es libre, variado, impredecible. No te quedas en un 
solo lugar, estilo o idea.

TALENTOS NATURALES:
- Versatilidad extrema: puedes hacer casi cualquier cosa si te interesa
- Adaptabilidad única: prosperas en cualquier ambiente o circunstancia
- Magnetismo personal natural: atraes personas de todos los ámbitos
- Curiosidad insaciable: aprendes constantemente cosas nuevas
- Capacidad de conectar mundos diversos: eres puente entre culturas, ideas, personas

TU DESTINO Y PROPÓSITO: Estás aquí para EXPLORAR y CONECTAR, no para estancarte. Tu nombre 
te programa para expandir horizontes, tuyos y de otros, mostrando que hay infinitas formas de 
vivir, pensar y ser. Tu legado serán los mundos que uniste y las mentes que liberaste.

EN EL TRABAJO: Te destacas en ventas, viajes, periodismo, comunicación multicultural, traducción, 
marketing, o cualquier campo que requiera versatilidad, adaptación y conexión entre diferentes 
mundos.

EN RELACIONES: Te expresas con pasión intensa pero necesitas libertad. Valoras la aventura 
compartida. Necesitas una pareja que vuele contigo sin intentar enjaularte o limitarte.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de aire: mueve, circula, conecta. Cada 
vez que alguien pronuncia tu nombre, invoca energía de libertad y cambio."""
            },
            6: {
                "essence": "Expresión responsable, amorosa y protectora.",
                "manifestation": """Te manifiestas nutriendo, embelleciendo y creando hogar. Tu destino 
involucra servir desde el amor y crear armonía familiar.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de cuidador natural. Cuando entras a un espacio, 
tu presencia crea calidez y seguridad. Hablas con amor y responsabilidad. Actúas pensando en 
el bienestar de otros. Tu estilo es acogedor, protector, armonizador. Creas “hogar” donde 
quiera que estés.

TALENTOS NATURALES:
- Capacidad de cuidado y nutrición excepcional: física, emocional, espiritual
- Sentido estético natural: embelleces todo lo que tocas
- Responsabilidad afectiva profunda: sostienes a quienes amas
- Habilidad para crear armonía en grupos y familias
- Consejería natural: otros buscan tu guía y consuelo

TU DESTINO Y PROPÓSITO: Estás aquí para NUTRIR y ARMONIZAR, no para vivir solo para ti. Tu 
nombre te programa para crear espacios de amor, belleza y sanación donde otros puedan florecer. 
Tu legado serán las vidas que nutriste y los corazones que sanaste con tu amor.

EN EL TRABAJO: Te destacas en educación, sanación, consejería, diseño de interiores, gastronomía, 
trabajo social, o cualquier campo donde cuidar del bienestar y crear belleza sean centrales.

EN RELACIONES: Te expresas con devoción y amor profundo. Valoras la familia y el hogar. Necesitas 
una pareja que valore tu cuidado sin aprovecharse, y que también te cuide a ti.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de corazón: ama, nutre, sana. Cada vez 
que alguien pronuncia tu nombre, invoca energía de amor y armonía."""
            },
            7: {
                "essence": "Expresión introspectiva, analítica y espiritual.",
                "manifestation": """Te manifiestas con profundidad, sabiduría y misterio. Tu destino involucra 
buscar verdad y enseñar desde la experiencia interior.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de sabio natural. Cuando entras a un espacio, tu 
presencia comunica profundidad y misterio. Hablas con precisión filosófica. Actúas con 
introspección y análisis. Tu estilo es reservado, observador, profundo. No te muestras 
completamente; siempre hay capas por descubrir.

TALENTOS NATURALES:
- Mente analítica excepcional: penetras bajo la superficie de todo
- Intuición profunda combinada con lógica rigurosa
- Conexión natural con dimensiones espirituales o filosóficas
- Capacidad de investigación exhaustiva y descubrimiento de verdades ocultas
- Sabiduría que viene de experiencia interior profunda

TU DESTINO Y PROPÓSITO: Estás aquí para BUSCAR VERDAD y ENSEÑAR SABIDURÍA, no para vivir 
superficialmente. Tu nombre te programa para profundizar en misterios que otros evitan, 
descubrir verdades que otros temen, y compartir sabiduría desde tu experiencia. Tu legado 
será el conocimiento que descubriste y la consciencia que elevaste.

EN EL TRABAJO: Te destacas en investigación, filosofía, ciencias, espiritualidad, análisis, 
psicología profunda, o cualquier campo que requiera penetrar bajo la superficie visible.

EN RELACIONES: Te expresas con profundidad selectiva. Valoras la conexión intelectual y espiritual. 
Necesitas una pareja que respete tu necesidad de soledad y comprenda tu naturaleza contemplativa.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de espíritu: busca, comprende, trasciende. 
Cada vez que alguien pronuncia tu nombre, invoca energía de sabiduría y misterio."""
            },
            8: {
                "essence": "Expresión ejecutiva, ambiciosa y orientada al éxito material.",
                "manifestation": """Te manifiestas con poder, autoridad y visión de negocios. Tu destino 
involucra gestionar grandes recursos y crear impacto material.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de ejecutivo natural. Cuando entras a un espacio, 
tu presencia comunica poder y competencia. Hablas con autoridad y visión estratégica. Actúas 
con determinación y orientación a resultados. Tu estilo es ambicioso, eficiente, orientado al 
logro. Transformas ideas en imperios.

TALENTOS NATURALES:
- Visión estratégica para negocios y gestión de recursos
- Capacidad de liderazgo ejecutivo y toma de decisiones de alto impacto
- Comprensión natural de poder, dinero y sistemas materiales
- Ambición sana combinada con determinación férrea
- Habilidad para crear abundancia material sostenible

TU DESTINO Y PROPÓSITO: Estás aquí para GESTIONAR PODER y CREAR ABUNDANCIA, no para vivir 
pequeño. Tu nombre te programa para manejar grandes recursos, liderar organizaciones importantes, 
y crear impacto material significativo. Tu legado será lo que construiste y el poder que usaste 
éticamente.

EN EL TRABAJO: Te destacas en negocios, finanzas, dirección ejecutiva, bienes raíces, consultoría 
estratégica, o cualquier posición de alto poder donde gestionar recursos y personas sea esencial.

EN RELACIONES: Te expresas con lealtad y generosidad material. Valoras el respeto mutuo y el 
éxito compartido. Necesitas una pareja que sea tu igual en ambición o que apoye tu misión sin 
resentimiento.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de poder: construye, gestiona, logra. Cada 
vez que alguien pronuncia tu nombre, invoca energía de abundancia y autoridad."""
            },
            9: {
                "essence": "Expresión compasiva, humanitaria y universal.",
                "manifestation": """Te manifiestas con generosidad, sabiduría y amor global. Tu destino 
involucra servir a la humanidad y cerrar ciclos kármicos.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de humanitario natural. Cuando entras a un espacio, 
tu presencia comunica compasión universal. Hablas con sabiduría y perspectiva global. Actúas 
con generosidad desinteresada. Tu estilo es inclusivo, compasivo, trascendente. Ves a toda la 
humanidad como familia.

TALENTOS NATURALES:
- Compasión que trasciende fronteras personales, culturales o nacionales
- Sabiduría emocional y espiritual profunda
- Capacidad de perdón y liberación de rencores
- Visión global: entiendes problemas desde perspectiva universal
- Generosidad auténtica sin necesidad de reconocimiento

TU DESTINO Y PROPÓSITO: Estás aquí para SERVIR A LA HUMANIDAD y COMPLETAR CICLOS, no para 
vivir egoístamente. Tu nombre te programa para aliviar sufrimiento colectivo, enseñar compasión, 
y cerrar ciclos kármicos tuyos y de otros. Tu legado será el amor que diste y las almas que 
liberaste.

EN EL TRABAJO: Te destacas en trabajo humanitario, ONGs, medicina sin fronteras, arte con mensaje 
social, educación transformadora, o cualquier campo donde servir al bien mayor sea el objetivo.

EN RELACIONES: Te expresas con amor universal. Valoras la conexión profunda sin posesividad. 
Necesitas una pareja que comprenda que tu amor por la humanidad no disminuye tu amor por ella/él.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de compasión: ama, perdona, libera. Cada 
vez que alguien pronuncia tu nombre, invoca energía de servicio y completación."""
            },
            11: {
                "essence": "Expresión maestra de visionario e inspirador.",
                "manifestation": """Te manifiestas con luz espiritual intensa y capacidad de elevar consciencias. 
Tu destino involucra ser guía e iluminar caminos.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de iluminador natural. Cuando entras a un espacio, 
tu presencia eleva la frecuencia energética. Hablas con inspiración canalizada. Actúas como 
puente entre dimensiones. Tu estilo es visionario, inspirador, magnético a nivel espiritual. 
No eres ordinario; tu sola presencia transforma.

TALENTOS NATURALES:
- Intuición profética que te conecta con guía superior
- Capacidad de inspirar transformación profunda en otros
- Visión de posibilidades que otros no perciben
- Canal natural de energía e información elevada
- Liderazgo espiritual auténtico basado en experiencia vivida

TU DESTINO Y PROPÓSITO: Estás aquí para ILUMINAR y ELEVAR, no para vivir ordinariamente. Tu 
nombre te programa para ser faro de luz en tiempos oscuros, mostrar caminos de evolución, y 
recordar a otros su naturaleza divina. Tu legado serán las consciencias que elevaste y la luz 
que irradiaste.

EN EL TRABAJO: Te destacas en liderazgo espiritual, coaching transformacional, arte visionario, 
enseñanza evolutiva, o cualquier campo donde tu capacidad de elevar consciencias sea tu 
contribución principal.

EN RELACIONES: Te expresas con intensidad espiritual. Valoras conexión de alma profunda. Necesitas 
una pareja que pueda sostener tu intensidad sin asustarse y que comprenda tu misión elevada.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de luz pura: ilumina, eleva, transforma. 
Cada vez que alguien pronuncia tu nombre, invoca energía de inspiración divina."""
            },
            22: {
                "essence": "Expresión maestra de gran organizador y manifestador.",
                "manifestation": """Te manifiestas convirtiendo visiones en grandes realidades tangibles. Tu 
destino involucra crear legados de impacto colectivo.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de arquitecto maestro. Cuando entras a un espacio, 
tu presencia comunica capacidad excepcional. Hablas con visión de gran escala pero pragmatismo 
concreto. Actúas construyendo imperios desde cimientos sólidos. Tu estilo es magistral, ambicioso 
a nivel colectivo, constructor de legados. Haces realidad lo que otros solo sueñan.

TALENTOS NATURALES:
- Capacidad única de manifestar visiones espirituales en realidades materiales masivas
- Liderazgo organizacional de nivel maestro
- Visión de largo plazo (décadas) combinada con ejecución impecable
- Habilidad de coordinar sistemas complejos y equipos grandes
- Pragmatismo elevado que hace posible lo imposible

TU DESTINO Y PROPÓSITO: Estás aquí para CONSTRUIR LEGADOS COLECTIVOS, no solo éxito personal. 
Tu nombre te programa para crear organizaciones, movimientos, sistemas o proyectos que 
transformen la vida de muchos y perduren generaciones. Tu legado será lo grande que construiste 
al servicio de todos.

EN EL TRABAJO: Te destacas en fundación de organizaciones de impacto, liderazgo de movimientos 
globales, arquitectura de sistemas transformadores, o cualquier campo donde tu capacidad de 
manifestar a gran escala sea necesaria.

EN RELACIONES: Te expresas con compromiso profundo hacia tu misión. Valoras socios que compartan 
tu visión grande. Necesitas una pareja que sea aliada en tu misión, no competencia por tu tiempo.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de manifestación maestra: construye imperios, 
crea legados, materializa visiones. Cada vez que alguien pronuncia tu nombre, invoca energía de 
construcción a escala masiva."""
            },
            33: {
                "essence": "Expresión maestra de servicio amoroso y guía compasiva.",
                "manifestation": """Te manifiestas como presencia sanadora de alta vibración. Tu destino 
involucra sanar y elevar masivamente.

CÓMO TE EXPRESAS EN EL MUNDO: Tu energía es de sanador maestro. Cuando entras a un espacio, 
tu presencia genera transformación sanadora inmediata. Hablas con amor incondicional que cura. 
Actúas desde compasión elevada. Tu estilo es de servicio puro, amor universal, presencia que 
sostiene y sana. Eres medicina viviente.

TALENTOS NATURALES:
- Amor incondicional auténtico que transforma profundamente
- Presencia naturalmente sanadora que actúa sin necesidad de técnicas
- Capacidad de sostener el dolor ajeno sin quebrarte
- Maestría emocional y espiritual combinadas
- Vocación de servicio que trasciende el ego personal

TU DESTINO Y PROPÓSITO: Estás aquí para SANAR Y AMAR A NIVEL COLECTIVO, no solo individual. 
Tu nombre te programa para ser presencia sanadora en tiempos de crisis colectiva, para recordar 
a la humanidad que el amor incondicional es real y posible. Tu legado será el amor que encarnaste 
y las almas que sanaste.

EN EL TRABAJO: Te destacas en sanación holística de alto nivel, maestría espiritual compasiva, 
liderazgo basado en amor, o cualquier campo donde tu presencia sanadora sea tu contribución 
principal, más allá de técnicas.

EN RELACIONES: Te expresas con amor incondicional. Valoras unión de almas profunda. Necesitas 
una pareja que pueda recibir tu amor sin sentirse abrumada y que también te nutra profundamente.

VIBRACIÓN DE TU NOMBRE: Tu nombre vibra con energía de amor puro: sana, eleva, transforma a nivel 
de alma. Cada vez que alguien pronuncia tu nombre, invoca energía de sanación divina."""
            },
        },
    },

    # ============================================================
    # DESEO DEL ALMA (SOUL URGE)
    # ============================================================
    "SOUL_URGE_MEANINGS": {
        "label": "Deseo del Alma / Soul Urge",
        "description": (
            "Revela lo que tu corazón realmente anhela vivir: tus motivaciones "
            "profundas, deseos emocionales y la experiencia interna que buscas en esta vida."
        ),
        "numbers": {
            1: {
                "essence": "Deseo profundo de independencia, liderazgo y autoafirmación.",
                "manifestation": """En lo más hondo, tu alma desea ser protagonista de su propia historia.
Buscas sentir que tu vida te pertenece, tomar decisiones por ti mismo y abrir camino donde no lo hay.

Tu corazón anhela:
- Ser visto como alguien único, auténtico y valiente.
- Tomar la iniciativa en tus proyectos, relaciones y decisiones importantes.
- Tener libertad para explorar tus ideas sin que otros te controlen.

Cuando honras este deseo:
- Te sientes vivo cuando lideras, emprendes o inicias algo nuevo.
- Te motivan los retos que te permiten demostrar tu fuerza interior.
- Tu autoestima crece al asumir riesgos conscientes y defender tus convicciones.

Desafío interno:
- El miedo a depender de otros o a ser controlado puede volverte terco o demasiado autosuficiente.
- Tu alma sufre cuando te adaptas demasiado a las expectativas ajenas y dejas de escuchar tu propio impulso.

Clave de armonía:
Aprender a liderar sin dominar, a ser independiente sin aislarte, y a usar tu fuerza interior como guía,
no como armadura."""
            },
            2: {
                "essence": "Deseo profundo de conexión, armonía emocional y cooperación.",
                "manifestation": """En lo más hondo, tu alma anhela relaciones cálidas, cercanas y auténticas.
Más que éxito externo, buscas sentir paz, comprensión y equilibrio emocional.

Tu corazón anhela:
- Conexiones donde puedas ser escuchado y también escuchar.
- Entornos tranquilos, sin conflicto innecesario ni agresividad.
- Sentir que eres un puente entre personas, no parte de la división.

Cuando honras este deseo:
- Disfrutas ayudar a otros a entenderse y reconciliarse.
- Brillas en espacios donde la empatía y la sensibilidad son valoradas.
- Te sientes pleno cuando colaboras en lugar de competir.

Desafío interno:
- Puedes sacrificar tu propia voz para “no generar problemas”.
- El miedo al conflicto puede hacer que toleres situaciones injustas o desgastantes.

Clave de armonía:
Aprender a decir lo que sientes sin temor, poniendo límites sanos y recordando que la verdadera paz incluye tu propia paz."""
            },
            3: {
                "essence": "Deseo profundo de expresarte creativamente y disfrutar la vida.",
                "manifestation": """En lo más hondo, tu alma quiere expresarse, crear, jugar y compartir alegría.
Tu esencia busca belleza, humor y libertad para ser quien eres sin máscaras.

Tu corazón anhela:
- Espacios donde puedas hablar, cantar, escribir, actuar o crear libremente.
- Relaciones donde se valore tu espontaneidad y sensibilidad artística.
- Momentos de disfrute, risa y ligereza que rompan la rutina.

Cuando honras este deseo:
- Tu creatividad fluye y contagia inspiración a quienes te rodean.
- Tu comunicación se vuelve magnética y conectas fácilmente con otros.
- Sientes que la vida tiene color, ritmo y propósito.

Desafío interno:
- Cuando reprimes tu expresión, puedes caer en tristeza, apatía o drama.
- Puedes usar el humor o la distracción para evitar temas emocionales profundos.

Clave de armonía:
Darte permiso para crear y expresarte, pero también para profundizar en tus emociones sin miedo.
Tu alegría es medicina, pero también mereces sostener tu propia vulnerabilidad."""
            },
            4: {
                "essence": "Deseo profundo de seguridad, orden y bases sólidas.",
                "manifestation": """En lo más hondo, tu alma anhela estabilidad, estructura y resultados concretos.
Buscas sentir que tu vida está bien construida, con pies en la tierra y metas claras.

Tu corazón anhela:
- Rutinas que te den seguridad y sensación de control sano.
- Trabajo y proyectos donde veas frutos tangibles de tu esfuerzo.
- Compromisos y vínculos duraderos donde haya lealtad y coherencia.

Cuando honras este deseo:
- Te sientes bien al cumplir, organizar y construir algo paso a paso.
- Encuentras paz en el esfuerzo constante y disciplinado.
- Tu entorno se vuelve más funcional, ordenado y confiable.

Desafío interno:
- El miedo al caos o a lo desconocido puede volverte rígido, controlador o excesivamente perfeccionista.
- Puedes sentir culpa al descansar o cambiar de rumbo, aunque tu alma lo necesite.

Clave de armonía:
Recordar que la verdadera estabilidad incluye flexibilidad. Las estructuras más fuertes
son las que pueden adaptarse sin romperse."""
            },
            5: {
                "essence": "Deseo profundo de libertad, cambio y experiencias intensas.",
                "manifestation": """En lo más hondo, tu alma anhela movimiento, variedad y expansión.
Te aburre la monotonía; buscas sentirte vivo explorando lo nuevo.

Tu corazón anhela:
- Viajes, cambios, aprendizajes constantes y escenarios distintos.
- Espacios donde puedas reinventarte sin ser juzgado.
- Relaciones y trabajos que respeten tu necesidad de independencia y aventura.

Cuando honras este deseo:
- Te sientes vibrante cuando exploras ideas, lugares y personas nuevas.
- Tu mente se mantiene despierta y creativa frente a la diversidad.
- Inspiras a otros a salir de su zona de confort y probar caminos diferentes.

Desafío interno:
- El miedo a sentirte atrapado puede llevarte a sabotear compromisos valiosos.
- Puedes dispersarte, empezar mucho y terminar poco, o escapar cuando algo se vuelve profundo.

Clave de armonía:
Encontrar formas de vivir cambio y libertad dentro de algunos compromisos elegidos conscientemente.
Tu alma no quiere jaulas, pero sí necesita un centro interno al que volver."""
            },
            6: {
                "essence": "Deseo profundo de amar, cuidar y crear belleza y hogar.",
                "manifestation": """En lo más hondo, tu alma anhela vínculos de amor profundo, familia (de sangre o elegida)
y espacios donde la gente se sienta segura y contenida.

Tu corazón anhela:
- Relaciones donde puedas dar y recibir cuidado genuino.
- Crear ambientes armoniosos, bellos, cálidos y llenos de significado.
- Sentir que eres importante para tu círculo cercano y que tu presencia sostiene.

Cuando honras este deseo:
- Disfrutas cuidar, ayudar, aconsejar y acompañar amorosamente.
- Te llenas al ver a otros crecer, sanar o sentirse mejor gracias a tu presencia.
- Tu sentido estético se expresa en lo que decoras, cocinas, organizas o proteges.

Desafío interno:
- Puedes caer en el sacrificio excesivo, olvidándote de ti mismo.
- Tu necesidad de que todo esté “bien” puede llevarte a controlar o a no dejar que otros se equivoquen.

Clave de armonía:
Entender que cuidarte también es parte del cuidado. El amor auténtico incluye decir “no” cuando es necesario,
y permitir que los demás asuman su propio aprendizaje."""
            },
            7: {
                "essence": "Deseo profundo de comprender, ir hacia adentro y buscar verdad.",
                "manifestation": """En lo más hondo, tu alma anhela silencio, profundidad y sentido.
No te basta con lo superficial; buscas respuestas verdaderas más allá de las apariencias.

Tu corazón anhela:
- Tiempo a solas para pensar, estudiar, meditar o investigar.
- Espacios donde puedas compartir ideas profundas sin ser juzgado.
- Una conexión auténtica con lo espiritual, filosófico o metafísico.

Cuando honras este deseo:
- Tu intuición y tu mente analítica se afinan y se complementan.
- Encuentras paz en la contemplación, la lectura, la reflexión o la práctica espiritual.
- Te conviertes en fuente de consejo sabio para otros.

Desafío interno:
- El exceso de introspección puede llevarte al aislamiento o al escepticismo extremo.
- Puedes sentirte incomprendido o “diferente”, cerrando aún más tu mundo interior.

Clave de armonía:
Equilibrar momentos de retiro con vínculos significativos donde puedas compartir tu mundo interno.
Tu sabiduría nació para ser vivida y compartida, no solo analizada."""
            },
            8: {
                "essence": "Deseo profundo de logros, impacto y dominio responsable del poder.",
                "manifestation": """En lo más hondo, tu alma anhela construir éxito tangible, influencia y abundancia
que tengan un propósito.

Tu corazón anhela:
- Sentir que tu esfuerzo genera resultados concretos y reconocibles.
- Manejar recursos (dinero, proyectos, personas) con maestría y propósito.
- Ser visto como alguien capaz, sólido y respetado.

Cuando honras este deseo:
- Tienes energía para trabajar duro y sostener grandes responsabilidades.
- Encuentras satisfacción en ver crecer proyectos, empresas o estructuras bajo tu liderazgo.
- Puedes usar el poder como herramienta para mejorar la vida de otros.

Desafío interno:
- El miedo a perder control o estatus puede llevarte a volverte duro, inflexible o materialista.
- Puedes confundir tu valor interno con tus logros externos o tu nivel económico.

Clave de armonía:
Recordar que el verdadero poder es servicio. Tu alma se satisface más cuando tu éxito
también eleva a otros, no cuando solo alimenta el ego."""
            },
            9: {
                "essence": "Deseo profundo de servir, sanar y cerrar ciclos desde el amor.",
                "manifestation": """En lo más hondo, tu alma anhela contribuir al bien mayor.
Te mueve el deseo de aliviar sufrimiento, ayudar y vivir con sentido humanitario.

Tu corazón anhela:
- Formar parte de causas, proyectos o trabajos que tengan impacto social o espiritual.
- Perdonar, soltar y cerrar historias pendientes para vivir más liviano.
- Ver a la humanidad avanzar hacia más consciencia, justicia y compasión.

Cuando honras este deseo:
- Te sientes pleno cuando ayudas, acompañas o inspiras a otros a sanar.
- Tu corazón se expande con el servicio desinteresado, las causas nobles o el arte sanador.
- Desarrollas una sabiduría amorosa que nace de tus propias experiencias de dolor y transformación.

Desafío interno:
- Puedes cargar con el dolor ajeno como si fuera tuyo y agotarte.
- Te cuesta soltar relaciones, historias o culpas que ya cumplieron su ciclo.

Clave de armonía:
Aprender a servir sin perderte, a amar sin salvar, y a soltar sin culpa.
Tu alma vino a cerrar ciclos con amor, no a cargar eternamente con ellos."""
            },
            11: {
                "essence": "Deseo profundo de vivir guiado por la intuición y la inspiración espiritual.",
                "manifestation": """En lo más hondo, tu alma anhela conexión directa con lo sutil, lo divino,
lo invisible. Deseas que tu vida tenga un sentido espiritual profundo y que tu camino esté lleno de señales
y propósito elevado.

Tu corazón anhela:
- Sentir que no estás solo, que hay una guía superior acompañándote.
- Vivir experiencias significativas que confirmen tu sensibilidad e intuición.
- Compartir mensajes, arte o enseñanzas que despierten consciencia en otros.

Cuando honras este deseo:
- Tu intuición se vuelve brújula clara para tus decisiones.
- Tu vida se llena de sincronicidades, sueños significativos y momentos de lucidez espiritual.
- Te conviertes en faro de luz para quienes buscan sentido.

Desafío interno:
- La intensidad de tu sensibilidad puede abrumarte y llevarte a querer “apagar” lo que sientes.
- Puedes dudar de ti mismo, alternando entre sentirte muy especial y profundamente inseguro.

Clave de armonía:
Cultivar prácticas espirituales y de enraizamiento que te permitan canalizar tu sensibilidad sin colapsar.
Tu alma vino a escuchar y transmitir mensajes de luz, pero también a cuidar su propio cuerpo y sistema nervioso."""
            },
            22: {
                "essence": "Deseo profundo de construir algo grande, útil y trascendente.",
                "manifestation": """En lo más hondo, tu alma anhela manifestar proyectos de impacto masivo que
unan lo espiritual con lo práctico. No te basta con una vida pequeña: deseas que tu existencia deje una huella.

Tu corazón anhela:
- Crear estructuras (empresas, organizaciones, sistemas) que ayuden a muchas personas.
- Ver tus ideales elevados convertidos en realidades concretas.
- Usar tu capacidad de organización al servicio de algo más grande que tú.

Cuando honras este deseo:
- Te sientes energizado cuando trabajas en proyectos de largo plazo y alto impacto.
- Tu liderazgo se vuelve herramienta poderosa para el bien colectivo.
- Logras alinear visión espiritual con ejecución impecable.

Desafío interno:
- Puedes sentir una presión interna enorme por “hacer algo grande” y paralizarte.
- El perfeccionismo puede llevarte al agotamiento o a sentir que nunca es suficiente.

Clave de armonía:
Aceptar que los grandes legados se construyen paso a paso.
Tu alma vino a ser arquitecto de algo mayor, pero también a disfrutar el proceso y a cuidarse en el camino."""
            },
            33: {
                "essence": "Deseo profundo de sanar, amar y sostener a otros a nivel muy elevado.",
                "manifestation": """En lo más hondo, tu alma anhela encarnar amor incondicional y ser canal de sanación
para muchas personas. Tu vocación interna es servir desde el corazón.

Tu corazón anhela:
- Ser instrumento de alivio, consuelo y transformación para quienes sufren.
- Crear espacios seguros donde otros puedan llorar, sanar y recomenzar.
- Vivir una vida guiada por la compasión, el servicio y el amor profundo.

Cuando honras este deseo:
- Tu presencia se vuelve medicina para quienes te rodean.
- Tu forma de amar inspira a otros a abrir su corazón.
- Te conviertes en guía, sanador o maestro natural, incluso sin proponértelo.

Desafío interno:
- Puedes olvidarte de ti mismo, dando hasta vaciarte.
- Atraes personas muy heridas que buscan en ti un salvador.

Clave de armonía:
Recordar que tu primer paciente eres tú. Tu alma vino a sanar, pero también a aprender a recibir,
a poner límites y a honrar su propia humanidad mientras encarna una vibración de amor muy alta."""
            },
        },
    },

    # ============================================================
    # NÚMERO DE PERSONALIDAD (PERSONALITY)
    # ============================================================
    "PERSONALITY_MEANINGS": {
        "label": "Número de Personalidad",
        "description": (
            "Se calcula a partir de las consonantes de tu nombre completo. Muestra la impresión que causas al inicio, "
            "tu estilo externo, tu “máscara social” y cómo otros te perciben antes de conocerte en profundidad."
        ),
        "numbers": {
            1: {
                "essence": "Imagen de líder, persona fuerte y directa.",
                "expanded": """Otros te perciben como alguien seguro, decidido y con carácter. 
Aunque por dentro puedas dudar, hacia afuera sueles mostrar firmeza.

CÓMO TE VEN:
- Dominante, con energía de mando
- Independiente, autosuficiente
- Competitivo o muy orientado a objetivos

PRIMERA IMPRESIÓN TÍPICA:
“Esta persona sabe lo que quiere y no viene a perder el tiempo.”

CUIDADO CON:
- Parecer autoritario o poco accesible
- Asustar a personas más sensibles con tu intensidad directa."""
            },
            2: {
                "essence": "Imagen suave, amable y cooperativa.",
                "expanded": """Otros te perciben como alguien sensible, diplomático y de buen corazón. 
Sueles irradiar calma y disposición a ayudar.

CÓMO TE VEN:
- Amable, empático y comprensivo
- Buen oyente, con tacto
- Poco conflictivo y conciliador

PRIMERA IMPRESIÓN TÍPICA:
“Es alguien con quien se puede hablar y confiar.”

CUIDADO CON:
- Que otros te vean como demasiado débil o siempre disponible
- Atraer personas que se aprovechen de tu suavidad."""
            },
            3: {
                "essence": "Imagen carismática, expresiva y social.",
                "expanded": """Otros te perciben como alguien alegre, interesante y creativo. 
Tu energía suele destacar en grupos.

CÓMO TE VEN:
- Divertido(a), entretenido(a), comunicativo(a)
- Con facilidad para hablar con cualquiera
- Con chispa, estilo y presencia llamativa

PRIMERA IMPRESIÓN TÍPICA:
“Qué persona tan simpática / creativa / interesante.”

CUIDADO CON:
- Ser percibido como poco serio o superficial
- Que otros no tomen en serio tu profundidad real por tu estilo ligero."""
            },
            4: {
                "essence": "Imagen seria, responsable y estructurada.",
                "expanded": """Otros te perciben como alguien confiable, trabajador y estable. 
Tu presencia transmite orden y realismo.

CÓMO TE VEN:
- Responsable, disciplinado(a)
- Práctico(a), organizado(a)
- Quizá reservado(a) o poco demostrativo(a)

PRIMERA IMPRESIÓN TÍPICA:
“Es alguien en quien se puede confiar.”

CUIDADO CON:
- Parecer demasiado rígido o cerrado
- Que otros te vean como “frío” cuando en realidad solo eres reservado."""
            },
            5: {
                "essence": "Imagen libre, dinámica y algo impredecible.",
                "expanded": """Otros te perciben como alguien inquieto, curioso y con espíritu aventurero. 
Tu energía es de cambio y movimiento.

CÓMO TE VEN:
- Interesante, versátil, abierto(a) a nuevas experiencias
- De mente abierta, poco convencional
- Algo inquieto(a) o difícil de “atrapar”

PRIMERA IMPRESIÓN TÍPICA:
“Parece alguien con mil historias y cosas por hacer.”

CUIDADO CON:
- Ser percibido como inconstante o poco confiable
- Que otros crean que nunca te comprometes de verdad."""
            },
            6: {
                "essence": "Imagen cálida, protectora y estética.",
                "expanded": """Otros te perciben como alguien acogedor, responsable y con buen gusto. 
Tu presencia suele sentirse “hogareña” y armonizadora.

CÓMO TE VEN:
- Cuidando detalles, tanto emocionales como estéticos
- Responsable con la familia, el grupo o el equipo
- Agradable, con energía de “casa” o “refugio”

PRIMERA IMPRESIÓN TÍPICA:
“Es alguien con quien me siento cómodo/a inmediatamente.”

CUIDADO CON:
- Ser percibido como entrometido(a) si te metes demasiado en la vida de otros
- Cargar demasiado rol de “mamá/papá” del grupo."""
            },
            7: {
                "essence": "Imagen reservada, profunda y algo enigmática.",
                "expanded": """Otros te perciben como alguien serio, observador y difícil de descifrar. 
Tu energía invita a la introspección.

CÓMO TE VEN:
- Pensativo(a), analítico(a), intelectual
- Reservado(a) con tu vida personal
- Con aire de misterio o profundidad

PRIMERA IMPRESIÓN TÍPICA:
“No sé bien qué piensa, pero se nota que observa todo.”

CUIDADO CON:
- Ser percibido como distante, frío o poco accesible
- Que otros se intimiden y no se acerquen por verte “demasiado serio(a)”."""
            },
            8: {
                "essence": "Imagen poderosa, ambiciosa y profesional.",
                "expanded": """Otros te perciben como alguien fuerte, capaz y orientado al éxito. 
Tu presencia impone respeto.

CÓMO TE VEN:
- Seguro(a) de ti mismo(a)
- Con aire ejecutivo o de autoridad
- Competente, estratégico(a), influyente

PRIMERA IMPRESIÓN TÍPICA:
“Esta persona está en otro nivel / sabe lo que hace.”

CUIDADO CON:
- Ser percibido como duro, materialista o intimidante
- Que otros te teman más de lo que te respetan, si no equilibras con humanidad."""
            },
            9: {
                "essence": "Imagen comprensiva, humanitaria y algo idealista.",
                "expanded": """Otros te perciben como alguien empático, sensible y con conciencia social. 
Tu energía inspira confianza y apertura.

CÓMO TE VEN:
- Comprensivo(a), buen consejero(a)
- Amable con todo tipo de personas
- Con cierta tristeza o nostalgia en la mirada, como si hubieras vivido mucho

PRIMERA IMPRESIÓN TÍPICA:
“Es alguien muy humano y sabio.”

CUIDADO CON:
- Ser percibido como demasiado sacrificado o siempre disponible
- Atraer personas que buscan ser “rescatadas” constantemente."""
            },
            11: {
                "essence": "Imagen espiritual, intensa y magnética.",
                "expanded": """Otros te perciben como alguien diferente, con “algo especial” difícil de explicar. 
Tu presencia tiene un impacto energético notable.

CÓMO TE VEN:
- Profundo(a), intuitivo(a), muy sensible
- Carismático(a) de forma sutil, no necesariamente ruidosa
- Inspirador(a), con mirada que parece ver más allá

PRIMERA IMPRESIÓN TÍPICA:
“No sé qué tiene, pero se siente especial / distinto.”

CUIDADO CON:
- Ser percibido como inestable emocionalmente si tu energía no está enraizada
- Despertar proyecciones (idealización o rechazo) muy fuertes en otros."""
            },
            22: {
                "essence": "Imagen de gran capacidad, visión y poder constructivo.",
                "expanded": """Otros te perciben como alguien que puede “hacer cosas muy grandes”. 
Tu presencia comunica seriedad y potencial de logro masivo.

CÓMO TE VEN:
- Competente a un nivel superior
- Organizado(a), visionario(a) y estratégico(a)
- Alguien cuyo tiempo y atención “valen mucho”

PRIMERA IMPRESIÓN TÍPICA:
“Es alguien importante o que llegará muy lejos.”

CUIDADO CON:
- Ser percibido como inaccesible o demasiado ocupado para lo humano
- Que otros se acerquen solo por interés en tu capacidad de lograr cosas."""
            },
            33: {
                "essence": "Imagen profundamente amorosa, contenedora y sanadora.",
                "expanded": """Otros te perciben como alguien con un corazón enorme. 
Tu presencia hace que las personas se abran, lloren, se sinceren o se sientan abrazadas sin saber por qué.

CÓMO TE VEN:
- Muy comprensivo(a), casi “angelical”
- Con energía de sanador(a) o guía
- Como alguien que entiende el dolor humano sin juzgar

PRIMERA IMPRESIÓN TÍPICA:
“Con esta persona siento que puedo ser yo mismo/a y ser aceptado/a.”

CUIDADO CON:
- Ser percibido como disponible 24/7 para sostener a todos
- Atraer relaciones donde solo te buscan para alivio y nunca para compartir tu propia carga."""
            },
        },
    },
}

# ============================================================
# NÚMEROS MAESTROS ESPECIALES (MASTER_MEANINGS)
# ============================================================

MASTER_MEANINGS = {
    11: {
        "title": "El Mensajero Iluminado - El Visionario Intuitivo",
        "essence": "El 11 es un Número Maestro de intuición, sensibilidad extrema e inspiración espiritual.",
        "expanded": """El 11 es el primer y más elevado de los números maestros, conocido como el "Mensajero 
Iluminado". Representa la puerta entre el mundo material y el espiritual, la capacidad de percibir lo 
invisible y traer luz de dimensiones superiores. 

Quienes llevan este número son almas antiguas con una misión evolutiva: elevar la consciencia colectiva 
y ser canales de inspiración divina. No están aquí para vivir una vida ordinaria; su propósito es 
trascendental y su impacto profundo. El 11 vibra en una frecuencia mucho más alta que su reducción (2), 
lo cual trae dones extraordinarios pero también desafíos intensísimos.

DUALIDAD INTENSA: Los 11 experimentan la vida en extremos. Pueden alcanzar estados de iluminación 
profunda donde todo tiene sentido, para luego caer en crisis existenciales donde nada lo tiene. Esta 
montaña rusa emocional y espiritual es parte de su camino de maestría.

SENSIBILIDAD EXTREMA: Son como antenas hipersensibles que captan todo: emociones ajenas, energías 
sutiles, presagios, sincronicidades. Esta sensibilidad puede ser un don profético o una carga 
abrumadora. Deben aprender a filtrar, protegerse energéticamente y no absorber el dolor del mundo.

NERVIOSISMO Y ANSIEDAD: El sistema nervioso de un 11 está constantemente sobrecargado. La ansiedad 
no es opcional; es parte de canalizar tanta energía sutil a través de un cuerpo humano. El desafío 
es aprender a manejarla sin medicarse en exceso o escapar mediante adicciones.

MISIÓN DE INSPIRACIÓN: Los 11 no están aquí para hacer, sino para SER e INSPIRAR. Su sola presencia 
puede cambiar la energía de un espacio. Hablan y otros sienten que algo en ellos despierta. Son 
catalizadores de transformación, maestros que enseñan más por lo que encarnan que por lo que dicen.

EL RETO DEL ENRAIZAMIENTO: Su mayor desafío es mantenerse enraizados en lo terrenal mientras vuelan 
en lo espiritual. Muchos 11 se pierden en idealismo, fantasía o espiritualidad sin anclaje. Deben 
aprender que la verdadera maestría incluye pagar las cuentas, cuidar el cuerpo y vivir responsablemente.

RELACIONES COMPLEJAS: Amar a un 11 es amar a alguien intenso, impredecible y profundo. Necesitan 
parejas que comprendan su necesidad de soledad, respeten su sensibilidad y no intenten "normalizarlos". 
Sus relaciones más exitosas son con quienes honran su naturaleza excepcional.

POTENCIAL DE LIDERAZGO ESPIRITUAL: Cuando un 11 acepta su camino, puede convertirse en guía, maestro, 
sanador o líder espiritual de gran impacto. Su palabra tiene peso porque viene de experiencia vivida, 
no de teoría.""",
        "shadow": """- Nerviosismo extremo y ansiedad crónica que puede derivar en ataques de pánico
- Tendencia a adicciones (alcohol, drogas, comida) para escapar de la intensidad
- Delirios espirituales, pensamiento mágico desconectado de la realidad
- Exceso de idealismo que lleva a decepciones constantes
- Mártir espiritual que se sacrifica hasta el agotamiento
- Arrogancia espiritual: sentirse "más evolucionado" que otros
- Inestabilidad emocional severa, cambios de humor dramáticos
- Dificultad para funcionar en la vida práctica y cotidiana""",
        "light": """- Intuición profética: saben cosas sin explicación lógica
- Capacidad de inspirar transformación profunda en otros
- Conexión directa con la guía espiritual y sabiduría superior
- Presencia magnética que atrae y eleva a las personas
- Visión clara de verdades universales y patrones kármicos
- Habilidad para canalizar creatividad, arte o mensajes elevados
- Compasión profunda y comprensión de la condición humana
- Liderazgo espiritual auténtico basado en experiencia personal""",
        "purpose": """Ser faro de luz en tiempos oscuros, inspirar despertar de consciencia, guiar con ejemplo 
vivido, enseñar que lo imposible es posible, recordar a la humanidad su naturaleza divina.""",
        "advice": """1. Acepta que eres diferente y deja de intentar ser "normal"
2. Desarrolla prácticas de enraizamiento: ejercicio, naturaleza, rutinas
3. Protege tu energía: aprende a decir no, establece límites claros
4. Encuentra tu tribu: rodéate de personas que entiendan tu sensibilidad
5. Canaliza la intensidad creativamente: arte, escritura, música, enseñanza
6. No huyas de tu misión por miedo; el mundo necesita tu luz
7. Cuida tu sistema nervioso: meditación, descanso, alimentación consciente
8. Busca terapia o guía que comprenda tu naturaleza espiritual"""
    },

    22: {
        "title": "El Arquitecto del Mundo - El Maestro Constructor",
        "essence": "El 22 es un Número Maestro constructor: une visión espiritual con logros muy concretos.",
        "expanded": """El 22 es el número del "Maestro Arquitecto", el constructor de sueños imposibles y el 
manifestador de visiones a gran escala. Si el 11 trae la visión, el 22 la convierte en realidad tangible. 
Este es el número de los grandes líderes, visionarios y constructores que dejan legados duraderos.

El 22 combina la inspiración espiritual del 11 con la disciplina práctica del 4 (su reducción), creando 
una de las fuerzas más poderosas en numerología. No se trata solo de soñar grande, sino de tener la 
capacidad, determinación y visión estratégica para manifestar esos sueños en la realidad material.

VISIÓN DE LARGO PLAZO: Los 22 no piensan en años, piensan en décadas o incluso generaciones. Ven 
posibilidades donde otros ven imposibles. Pueden imaginar sistemas completos, organizaciones masivas, 
proyectos que cambiarán industrias enteras. Su mente trabaja en dimensiones que otros no alcanzan.

CAPACIDAD DE MANIFESTACIÓN EXCEPCIONAL: Mientras muchos se quedan en la fantasía, los 22 tienen el 
don raro de convertir ideas en imperios. Poseen una combinación única de idealismo inspirador y 
pragmatismo brutal. Saben soñar Y saben ejecutar. Esta dualidad los hace extraordinariamente efectivos.

PRESIÓN INMENSA: Ser un 22 es llevar un peso existencial enorme. Sienten internamente que están aquí 
para algo grande, y esa sensación puede ser paralizante. La brecha entre su visión y su realidad actual 
puede generar frustración profunda, especialmente en la juventud. Muchos 22 se sienten "diferentes" 
desde niños, sabiendo que tienen una misión importante pero sin saber cuál es.

EL DESAFÍO DEL PERFECCIONISMO: Los 22 tienen estándares imposiblemente altos. Si no están construyendo 
algo "suficientemente grande o significativo", sienten que están fracasando. Este perfeccionismo puede 
paralizarlos completamente o llevarlos al agotamiento total. Deben aprender que los grandes legados se 
construyen paso a paso, no de un salto.

LIDERAZGO NATURAL PERO SOLITARIO: Los 22 son líderes natos, pero su visión a menudo los adelanta tanto 
que pocos pueden seguirles el ritmo. Esto puede generar soledad profunda. Necesitan aprender a comunicar 
su visión de manera que otros puedan comprenderla y unirse, en lugar de aislarse en su grandeza.

MATERIALIZACIÓN CON PROPÓSITO: A diferencia del 8 (que busca poder y riqueza personal), el 22 construye 
para el bien colectivo. Su motivación más profunda no es el ego sino el legado. Quieren dejar el mundo 
mejor de lo que lo encontraron, y piensan en grande sobre cómo lograrlo.

RELACIONES COMPLEJAS: Amar a un 22 es amar a alguien casado con una misión. Sus relaciones personales 
a menudo sufren porque su obra consume su energía. Necesitan parejas que comprendan su necesidad de 
construir algo grande y que puedan ser socios en esa visión, no competencia por atención.

POTENCIAL DE IMPACTO MASIVO: Cuando un 22 encuentra su proyecto de vida y se compromete totalmente, 
puede literalmente cambiar el mundo. Son los fundadores de movimientos, organizaciones globales, 
innovaciones que transforman industrias. Su legado trasciende su vida física.""",
        "shadow": """- Perfeccionismo paralizante que impide comenzar o terminar proyectos
- Presión autoimpuesta brutal que lleva al agotamiento y burnout severo
- Megalomanía: visiones tan grandes que se vuelven irreales o egocéntricas
- Adicción al trabajo que destruye salud, relaciones y vida personal
- Frustración crónica cuando la realidad no alcanza la visión
- Tendencia a manipular o controlar para lograr sus objetivos
- Frialdad emocional: sacrificar humanidad por eficiencia
- Colapso nervioso cuando el peso de la misión se vuelve insoportable""",
        "light": """- Capacidad única de manifestar visiones en realidades tangibles masivas
- Liderazgo inspirador que mueve a personas hacia objetivos colectivos
- Visión estratégica excepcional que ve 10-20 años adelante
- Disciplina y determinación férreas para sostener proyectos largos
- Habilidad de organizar sistemas complejos y gestionar grandes equipos
- Pragmatismo elevado: combinan espiritualidad con acción concreta
- Potencial de crear legados que benefician a generaciones
- Capacidad de convertir lo imposible en inevitable""",
        "purpose": """Construir estructuras, organizaciones, sistemas o proyectos que transformen positivamente 
la vida de muchas personas. Dejar un legado tangible que perdure más allá de su vida. Demostrar que las 
grandes visiones espirituales pueden manifestarse materialmente.""",
        "advice": """1. Abraza que eres un constructor de legados, no de gratificación instantánea
2. Divide tu gran visión en pasos manejables para evitar parálisis
3. Rodéate de un equipo sólido; no puedes construir imperios solo
4. Establece límites entre trabajo y vida personal o te quemarás
5. Celebra pequeños logros en el camino, no solo el destino final
6. Encuentra mentores que hayan construido a gran escala
7. Cuida tu salud física: tu cuerpo es el vehículo de tu misión
8. Recuerda que los legados más grandes se construyen con paciencia"""
    },

    33: {
        "title": "El Maestro Sanador - El Avatar del Amor Universal",
        "essence": "El 33 es un Número Maestro de amor incondicional, servicio elevado y sanación colectiva.",
        "expanded": """El 33 es el más raro y elevado de los números maestros, conocido como el "Maestro 
Sanador" o "Avatar del Amor Universal". Representa la vibración más alta de servicio espiritual, la 
capacidad de amar incondicionalmente y la vocación de sanar el sufrimiento humano a gran escala.

Si el 11 ilumina y el 22 construye, el 33 SANA. Este número combina la sensibilidad del 11 con la 
capacidad de manifestación del 22, enfocándolo todo en servicio amoroso. Los 33 son almas muy antiguas 
que han encarnado específicamente para ser agentes de sanación colectiva en momentos críticos de la 
humanidad.

CORAZÓN EXCEPCIONAL: Los 33 poseen una capacidad de amor que va más allá de lo humano normal. Pueden 
amar a extraños como familia, perdonar lo imperdonable, ver luz donde otros ven solo oscuridad. Su 
corazón es un portal de compasión infinita, capaz de sostener el dolor ajeno sin quebrarse (aunque a 
veces sí se quiebran). 

PRESENCIA SANADORA: Simplemente ESTAR cerca de un 33 es terapéutico. Su energía tiene una cualidad 
sanadora natural que otros perciben instantáneamente. La gente se siente segura, vista y amada en su 
presencia. Pueden entrar a una habitación llena de tensión y su sola presencia calma el ambiente.

EL PESO DEL SERVICIO EXTREMO: Ser un 33 es cargar una cruz emocional pesadísima. Sienten el dolor del 
mundo de manera visceral. No pueden ver sufrimiento sin querer aliviarlo. Esta compasión sin límites 
puede llevarlos al agotamiento extremo, al sacrificio destructivo de sí mismos, o a la codependencia 
severa. Su mayor lección es aprender que no pueden salvar a todos.

MAESTROS DEL AMOR INCONDICIONAL: Los 33 enseñan a otros lo que significa amar sin condiciones. No 
solo hablan de amor; lo encarnan. Son el ejemplo viviente de que es posible amar profundamente sin 
apego, servir sin esperar nada a cambio, y perdonar lo imperdonable. Su vida misma es su enseñanza 
más poderosa.

VULNERABILIDAD EXTREMA: Su apertura de corazón los hace extremadamente vulnerables a heridas profundas. 
Muchos 33 han sufrido traumas emocionales severos, traiciones devastadoras o pérdidas que romperían a 
otros. Pero precisamente estas heridas los convierten en sanadores auténticos: sanan porque conocen el 
dolor desde dentro.

EL DESAFÍO DE LOS LÍMITES: Los 33 deben aprender la lección más difícil: que el amor verdadero incluye 
límites. Decir "no" no es falta de amor; es amor maduro. Cuidarse a sí mismos no es egoísmo; es 
necesidad. La paradoja del 33 es que para servir más, deben aprender a dar menos. Para amar mejor, 
deben amarse primero.

VOCACIÓN DE MAESTROS ESPIRITUALES: Cuando un 33 madura espiritualmente, se convierte en maestro, 
sanador, guía espiritual o líder de movimientos de sanación colectiva. No necesitan títulos formales; 
su autoridad viene de su presencia amorosa y su sabiduría vivida.

RELACIONES INTENSAS: Amar a un 33 es ser amado de una manera que puede asustarte por su profundidad. 
Pero también es estar con alguien que puede agotarse dando a otros. Sus relaciones más exitosas son 
con quienes también cuidan del cuidador y le recuerdan que merece recibir amor también.

LEGADO DE SANACIÓN: Los 33 están aquí en momentos de crisis colectiva para recordar a la humanidad 
que el amor es real, poderoso y transformador. Su legado no es material sino energético: las vidas 
que tocaron, las almas que sanaron, el amor que irradiaron.""",
        "shadow": """- Codependencia severa: necesitan sentirse necesarios para validar su existencia
- Síndrome del mártir: se sacrifican destructivamente hasta el agotamiento total
- Incapacidad de poner límites: dicen sí cuando deberían decir no
- Agotamiento emocional y físico crónico por dar sin recibir
- Tendencia a atraer relaciones tóxicas donde "rescatan" a otros
- Depresión profunda cuando sienten que no pueden ayudar suficiente
- Negación de sus propias necesidades emocionales y físicas
- Fantasías de salvador: creer que pueden o deben salvar a todos""",
        "light": """- Amor incondicional auténtico que transforma a quienes lo reciben
- Presencia naturalmente sanadora que calma y eleva
- Compasión infinita sin juicio ni condiciones
- Habilidad de ver lo mejor en cada persona, incluso en "los peores"
- Capacidad de perdonar profundamente y liberar rencores
- Maestría en sostener espacios emocionales seguros para otros
- Sabiduría emocional y espiritual profunda ganada por experiencia
- Impacto sanador que trasciende lo individual hacia lo colectivo""",
        "purpose": """Sanar el sufrimiento humano a través del amor incondicional. Ser ejemplo viviente de 
compasión sin límites. Enseñar que el amor es la fuerza más poderosa del universo. Recordar a la 
humanidad su capacidad de amar y perdonar. Elevar la vibración colectiva con su sola presencia.""",
        "advice": """1. Tu primer acto de servicio es cuidarte a ti mismo: no puedes dar desde el vacío
2. Aprende a decir no sin culpa; los límites son amor maduro
3. Busca terapia profunda para sanar tus propias heridas antes de sanar a otros
4. Rodéate de personas que también te nutran; mereces recibir amor
5. Reconoce que no puedes (ni debes) salvar a todos
6. Desarrolla prácticas de autocuidado NO negociables
7. Encuentra tu tribu de otros sanadores que comprendan tu camino
8. Recuerda: tu valor no depende de cuánto des o a cuántos ayudes"""
    },
}

# Por ahora dejamos los números kármicos vacíos, pero la variable debe existir
KARMIC_MEANINGS = {}
