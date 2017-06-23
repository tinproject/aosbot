import yaml


emoji = {
    "coffee": b"",
    "alarm_clock": b"\xE2\x8F\xB0",
    "watch": b"\xE2\x8C\x9A",
    "hourglass_flowing_sand": b"\xE2\x8F\xB3",
    "calendar": b"\xF0\x9F\x93\x85",
    "fork_and_knife": b"\xF0\x9F\x8D\xB4",
    "raising_hand": b"\xF0\x9F\x99\x8B",
    "footprints": b"\xF0\x9F\x91\xA3",
    "speech_balloon": b"\xF0\x9F\x92\xAC",
    "thought_balloon": b"\xF0\x9F\x92\xAD",
    "pig": b"\xF0\x9F\x90\x96",
    "pig_nose": b"\xF0\x9F\x90\xBD",
    "ghost": b"\xF0\x9F\x91\xBB",
    "gift": b"",
    "closed_book": b"\xF0\x9F\x93\x95",
    "blue_book": b"\xF0\x9F\x93\x98",
    "orange_book": b"\xF0\x9F\x93\x99",
    "notebook": b"\xF0\x9F\x93\x93",
    "space_invader": b"",
    "cookie": b"\xF0\x9F\x8D\xAA",

    "thinking": b"	\xF0\x9F\x93\x98",
    "deiser": b"\xF0\x9F\x93\x93",
    "ust_global": b"\xF0\x9F\x93\x95",
    "jeronimo_palacios": b"\xF0\x9F\x93\x99",
    "agile_spain": b"\xF0\x9F\x93\x97",
    "agile_torrezno": b"\xF0\x9F\x93\x92",
}


# Talk types: session, general, break, extra
# Session rooms:
# Thinking with you
# Deiser
# UST Global
# Jerónimo Palacios
# Agile Spain
# Agile Torrezno


def get_emoji(emoji_name):
    return emoji[emoji_name].decode('utf-8')


talks_data = yaml.safe_load("""
---

talks:
  # - session_type: session
  #   from_time: "2017-06-24T09:00:00+0200"
  #   to_time: "2017-06-24T10:00:00+0200"
  #   room:
  #   icon:
  #   title:
  #   proposer:
  #   description:

# Viernes 23

  - session_type: extra
    from_time: "2017-06-23T11:00:00+0200"
    to_time: "2017-06-23T13:00:00+0200"
    room: Campus María Zambrano
    icon: ghost
    title: Let's Play Agile Games
    proposer: Amalia Hernández y Delia Estebaranz
    description: |
        Juegos acerca de la formación de equipos y la confianza
        Apto para todo tipo de públicos.

  - session_type: extra
    from_time: "2017-06-23T11:00:00+0200"
    to_time: "2017-06-23T13:00:00+0200"
    room: Campus María Zambrano
    icon: ghost
    title: AOS Code Jam
    proposer: José Doval y Agustín Herranz
    description: |
        Sesión abierta sobre programación en la que practicar, plantear dudas, enseñar código, debatir...
        podrás traer tu portátil para trabajar sobre código y aprender un montón de cosas..

  - session_type: general
    from_time: "2017-06-23T16:00:00+0200"
    to_time: "2017-06-23T17:30:00+0200"
    room: Campus María Zambrano
    icon: raising_hand
    title: Apertura del AOS 2017
    proposer: AOS
    description: |
        ¿En qué consiste el AOS 2017?
        Presentación y actividades previas.

  - session_type: general
    from_time: "2017-06-23T17:30:00+0200"
    to_time: "2017-06-23T19:30:00+0200"
    room: Campus María Zambrano
    icon: raising_hand
    title: Creación del panel y votación de las sesiones
    proposer: AOS
    description: |
        Las personas que lo deseen proponen una sesión o un tema del que hablar explicando brevemente el contenido y enfoque de la sesión.
        Tras proponer todas las sesiones, los asistentes votan aquellas que sean de su interés.
        Las más votadas se repartirán en el panel final estableciendo la agenda del sábado.

# Sábado 24

  - session_type: break
    from_time: "2017-06-24T08:45:00+0200"
    to_time: "2017-06-24T09:00:00+0200"
    room: Ágora
    icon: cookie
    title: Desayuno
    proposer: AOS
    description:

  - session_type: general
    from_time: "2017-06-24T09:00:00+0200"
    to_time: "2017-06-24T10:00:00+0200"
    room: Ágora
    icon: raising_hand
    title: Apertura de las sesiones
    proposer: AOS
    description:

  - session_type: session
    from_time: "2017-06-24T10:00:00+0200"
    to_time: "2017-06-24T11:00:00+0200"
    room: Thinking with you
    icon: thinking
    title: Empresas de servicios, ¿Qué vendemos en un proyecto Agile?
    proposer: Sergio Fernández
    description: ...
  - session_type: session
    from_time: "2017-06-24T10:00:00+0200"
    to_time: "2017-06-24T11:00:00+0200"
    room: Deiser
    icon: deiser
    title: Equipos multidisciplinares vs. departamentos
    proposer: Jordi Gómez
    description: ...
  - session_type: session
    from_time: "2017-06-24T10:00:00+0200"
    to_time: "2017-06-24T11:00:00+0200"
    room: UST Global
    icon: ust_global
    title: La interminable historia de las priorizaciones
    proposer: "@rquel_lerones y @josep_riudavets"
    description:
  - session_type: session
    from_time: "2017-06-24T10:00:00+0200"
    to_time: "2017-06-24T11:00:00+0200"
    room: Jerónimo Palacios
    icon: jeronimo_palacios
    title: Devops! ¿Cómo lo lleváis?
    proposer: "@leodmurillo"
    description: ...
  - session_type: session
    from_time: "2017-06-24T10:00:00+0200"
    to_time: "2017-06-24T11:00:00+0200"
    room: Agile Spain
    icon: agile_spain
    title: "Parallel Change (Cómo hacer cambios grandes en pasos pequeños)"
    proposer: "@eferro"
    description: ...
  - session_type: session
    from_time: "2017-06-24T10:00:00+0200"
    to_time: "2017-06-24T11:00:00+0200"
    room: Agile Torrezno
    icon: agile_torrezno
    title: "#NoEstimates ¿Cómo medir \\"velocidad\\"/rendimiento?"
    proposer: Guillermo Rocha
    description: ...

  - session_type: session
    from_time: "2017-06-24T11:00:00+0200"
    to_time: "2017-06-24T12:00:00+0200"
    room: Thinking with you
    icon: thinking
    title: "#MakeMeHappyAtWork"
    proposer: "Susana Morcuende @yosoytumadre"
    description: ...
  - session_type: session
    from_time: "2017-06-24T11:00:00+0200"
    to_time: "2017-06-24T12:00:00+0200"
    room: Deiser
    icon: deiser
    title: Como combatir el efecto Pokémon.
    proposer: "Javier Martínez @lasdelpulpo"
    description: ...
  - session_type: session
    from_time: "2017-06-24T11:00:00+0200"
    to_time: "2017-06-24T12:00:00+0200"
    room: UST Global
    icon: ust_global
    title: Después de Nexus, Less, SAFE... ¡ARGOS! Creando un universo de productos
    proposer: Alberto Serrano
    description:
  - session_type: session
    from_time: "2017-06-24T11:00:00+0200"
    to_time: "2017-06-24T12:00:00+0200"
    room: Jerónimo Palacios
    icon: jeronimo_palacios
    title: De JP a P.O. (Del látigo al Postit)
    proposer: Jose Ángel Gómez
    description: ...
  - session_type: session
    from_time: "2017-06-24T11:00:00+0200"
    to_time: "2017-06-24T12:00:00+0200"
    room: Agile Spain
    icon: agile_spain
    title: The Roadmap Journey
    proposer: "@vanesa_tejada"
    description: ...
  - session_type: session
    from_time: "2017-06-24T11:00:00+0200"
    to_time: "2017-06-24T12:00:00+0200"
    room: Agile Torrezno
    icon: agile_torrezno
    title: ¿En que consiste exactamente el Mindset Agile?
    proposer: "@MaicaTrinidad"
    description: ...

  - session_type: break
    from_time: "2017-06-24T12:00:00+0200"
    to_time: "2017-06-24T12:30:00+0200"
    room: room
    icon: fork_and_knife
    title: Coffe break
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T12:30:00+0200"
    to_time: "2017-06-24T13:30:00+0200"
    room: Thinking with you
    icon: thinking
    title: "\\"The 3 4 Amigos\\" Fishbowl o Lean Coffee"
    proposer: "@Gastonvalle"
    description: ...
  - session_type: session
    from_time: "2017-06-24T12:30:00+0200"
    to_time: "2017-06-24T13:30:00+0200"
    room: Deiser
    icon: deiser
    title: Agile fuera de I.T.
    proposer: Juan Carlos Sánchez
    description: ...
  - session_type: session
    from_time: "2017-06-24T12:30:00+0200"
    to_time: "2017-06-24T13:30:00+0200"
    room: UST Global
    icon: ust_global
    title: Comunicación No Violenta, Más allá del método
    proposer: Francisco Javier García Orduña
    description:
  - session_type: session
    from_time: "2017-06-24T12:30:00+0200"
    to_time: "2017-06-24T13:30:00+0200"
    room: Jerónimo Palacios
    icon: jeronimo_palacios
    title: Remotamente Ágiles
    proposer: "@merybere"
    description: ...
  - session_type: session
    from_time: "2017-06-24T12:30:00+0200"
    to_time: "2017-06-24T13:30:00+0200"
    room: Agile Spain
    icon: agile_spain
    title: Facilitación Gráfica en el mundo #agile
    proposer: "Janire Paskua y Bea Zarzo"
    description: ...
  - session_type: session
    from_time: "2017-06-24T12:30:00+0200"
    to_time: "2017-06-24T14:30:00+0200"
    room: Agile Torrezno
    icon: agile_torrezno
    title: "Competencias en equipo scrum en entorno de escalado"
    proposer: "Juanma Gomez y Edu Cabrera"
    description: ...

  - session_type: session
    from_time: "2017-06-24T13:30:00+0200"
    to_time: "2017-06-24T14:30:00+0200"
    room: Thinking with you
    icon: thinking
    title: "Agile en la Administración Pública"
    proposer: "Gertru"
    description: ...
  - session_type: session
    from_time: "2017-06-24T13:30:00+0200"
    to_time: "2017-06-24T14:30:00+0200"
    room: Deiser
    icon: deiser
    title: Sobreviviendo al sprint review
    proposer: "Vicente Amorós"
    description: ...
  - session_type: session
    from_time: "2017-06-24T13:30:00+0200"
    to_time: "2017-06-24T14:30:00+0200"
    room: UST Global
    icon: ust_global
    title: "Agile Universities"
    proposer: "@nhpatt"
    description:
  - session_type: session
    from_time: "2017-06-24T13:30:00+0200"
    to_time: "2017-06-24T14:30:00+0200"
    room: Jerónimo Palacios
    icon: jeronimo_palacios
    title: Gestión de conflictos
    proposer: Diego Rojas
    description: ...
  - session_type: session
    from_time: "2017-06-24T13:30:00+0200"
    to_time: "2017-06-24T14:30:00+0200"
    room: Agile Spain
    icon: agile_spain
    title: Disciplina positiva y Agile Kids
    proposer: "@aquiestathai y @pedroserranot"
    description: ...

  - session_type: break
    from_time: "2017-06-24T14:30:00+0200"
    to_time: "2017-06-24T16:00:00+0200"
    room: room
    icon: fork_and_knife
    title: Comida
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T16:00:00+0200"
    to_time: "2017-06-24T17:00:00+0200"
    room: Thinking with you
    icon: thinking
    title: "Mindfulness y Agile"
    proposer: "Marta San Martin"
    description: ...
  - session_type: session
    from_time: "2017-06-24T16:00:00+0200"
    to_time: "2017-06-24T17:00:00+0200"
    room: Deiser
    icon: deiser
    title: Refinando el refinamiento
    proposer: "Gabi Salamanca"
    description: ...
  - session_type: session
    from_time: "2017-06-24T16:00:00+0200"
    to_time: "2017-06-24T17:00:00+0200"
    room: UST Global
    icon: ust_global
    title: Design Thinking para crear dinámicas
    proposer: Roberto A, Roberto Cruz, David Fernandez, David Jimenez
    description:
  - session_type: session
    from_time: "2017-06-24T16:00:00+0200"
    to_time: "2017-06-24T17:00:00+0200"
    room: Jerónimo Palacios
    icon: jeronimo_palacios
    title: Scrum en el Aula (Otra alternativa)
    proposer: Marisa
    description: ...
  - session_type: session
    from_time: "2017-06-24T16:00:00+0200"
    to_time: "2017-06-24T17:00:00+0200"
    room: Agile Spain
    icon: agile_spain
    title: Kanban, ¡No me salen las cuentas!
    proposer: "Laura Portilla"
    description: ...
  - session_type: session
    from_time: "2017-06-24T16:00:00+0200"
    to_time: "2017-06-24T17:00:00+0200"
    room: Agile Torrezno
    icon: agile_torrezno
    title: Slow
    proposer: "@WalletThomas"
    description: ...

  - session_type: session
    from_time: "2017-06-24T17:00:00+0200"
    to_time: "2017-06-24T18:00:00+0200"
    room: Thinking with you
    icon: thinking
    title: "Estamos ganando la batalla del cambio cultural cuando \\"recursos humanos\\" se hace cargo de la \\"oficina agile\\""
    proposer: "Gerardo Ponte"
    description: ...
  - session_type: session
    from_time: "2017-06-24T17:00:00+0200"
    to_time: "2017-06-24T18:00:00+0200"
    room: Deiser
    icon: deiser
    title: Construyendo productos con Nexus framework
    proposer: "@unairoldan"
    description: ...
  - session_type: session
    from_time: "2017-06-24T17:00:00+0200"
    to_time: "2017-06-24T18:00:00+0200"
    room: UST Global
    icon: ust_global
    title: Impros Ágiles
    proposer: "@lasdelpulpo y @merybene"
    description:
  - session_type: session
    from_time: "2017-06-24T17:00:00+0200"
    to_time: "2017-06-24T18:00:00+0200"
    room: Jerónimo Palacios
    icon: jeronimo_palacios
    title: Comunidades de aprendizaje en la empresa
    proposer: "Modesto San Juan @msanjuan"
    description: ...
  - session_type: session
    from_time: "2017-06-24T17:00:00+0200"
    to_time: "2017-06-24T18:00:00+0200"
    room: Agile Spain
    icon: agile_spain
    title: Kanban, Autoexigencia de los equipos, ¿Se trabaja?
    proposer: "Aritz Suescun @artzis"
    description: ...
  - session_type: session
    from_time: "2017-06-24T17:00:00+0200"
    to_time: "2017-06-24T18:00:00+0200"
    room: Agile Torrezno
    icon: agile_torrezno
    title: "Matar al unicornio (mesa redonda)"
    proposer: "Miriam orejana, Sara de Pablos y Rubén Plaza"
    description: ...

  - session_type: general
    from_time: "2017-06-24T18:00:00+0200"
    to_time: "2017-06-24T19:00:00+0200"
    room:
    icon: raising_hand
    title: Retrospectiva y cierre AOS 2017
    proposer: AOS
    description:

""")  # NoQA E501, W291
