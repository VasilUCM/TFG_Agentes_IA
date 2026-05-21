from crewai import Task

def tarea_analisis_entorno(agente):
    return Task(
        description="""
        Utiliza tus herramientas para leer los documentos base y buscar datos macroeconómicos actualizados sobre Japón y el aceite de oliva.
        
        ALGORITMO DE EJECUCIÓN (Aplica rigor APA 7 en cada paso):
        1. PESTEL: Extrae 3 variables empíricas por cada una de las 6 dimensiones. Puntúa de 1 a 5. Justifica exhaustivamente el impacto.
        2. CAGE: Analiza las 4 distancias. Determina si es Alto/Bajo Contexto (Hall, 1976) y explica por qué.
        3. PORTER: Evalúa las 5 fuerzas y explica la dinámica competitiva.
        """,
        expected_output="""Un informe académico denso que contenga: 
        1. Análisis PESTEL justificado y citado (Autor, Año). 
        2. Análisis CAGE y Hall justificados. 
        3. 5 Fuerzas de Porter explicadas. 
        *REGLA*: Formato estricto [Variable/Nota] -> [Justificación profunda] -> [Cita APA 7].""",
        agent=agente,
        output_file="1_informe_analista_limpio.md"
    )

def tarea_auditoria_operativa(agente):
    return Task(
        description="""
        Lee los hallazgos del Analista. Usa tus herramientas para buscar en los documentos locales e internet regulaciones japonesas reales.
        
        ALGORITMO DE EJECUCIÓN (Aplica rigor APA 7):
        1. ARANCEL: Especifica el código HS y el arancel exacto bajo el EPA UE-Japón.
        2. NTMs: Identifica y justifica las [BARRERAS INTRÍNSECAS] y [BARRERAS EXTRÍNSECAS].
        3. ESCALADA Y LOGÍSTICA: Selecciona Incoterm para cadena de frío. Elabora Matriz de Escalada de Precios.
        """,
        expected_output="""Un informe técnico auditor que contenga:
        1. Datos arancelarios.
        2. Clasificación de NTMs.
        3. Matriz de Escalada de Precios e Incoterm.
        *REGLA*: Cada decisión justificada causalmente y referenciada en APA 7 (Autor, Año).""",
        agent=agente,
        output_file="2_informe_operaciones_limpio.md"
    )

def tarea_marketing(agente):
    return Task(
        description="""
        Lee las restricciones de PESTEL, CAGE, NTMs y Costes de los agentes anteriores.
        
        ALGORITMO DE EJECUCIÓN (Aplica rigor APA 7):
        1. SEGMENTACIÓN: Define un nicho justificado por la distancia cultural.
        2. 4Ps y COO: 
           - Justifica la adaptación del Producto por las NTMs detectadas.
           - Justifica el Precio basándote en la Escalada de Precios operativa.
           - Justifica el Canal para neutralizar a las Shoshas.
           - Justifica el mensaje promocional basándote en el Efecto País de Origen y contexto cultural.
        """,
        expected_output="""Un Plan Go-to-Market que contenga:
        1. Segmentación STP.
        2. Políticas de las 4Ps.
        *REGLA*: CADA política referenciando una restricción de los agentes previos, con cita APA 7.""",
        agent=agente,
        output_file="3_informe_marketing_limpio.md"
    )

def tarea_decision_ceo(agente):
    return Task(
        description="""
        Sintetiza de forma ejecutiva y académica los informes de todo el equipo.
        
        ALGORITMO DE EJECUCIÓN (Aplica rigor APA 7):
        1. TOWS: Construye estrategias CAME cruzando los datos reportados.
        2. S.A.F.: Somete la estrategia al triple filtro justificando [Cumple] o [No Cumple].
        3. DICTAMEN RUMELT: Redacta Diagnóstico, Política Rectora y Acciones Coherentes.
        """,
        expected_output="""Dictamen final corporativo que contenga:
        1. Matriz TOWS/CAME justificada.
        2. Evaluación S.A.F. explicada.
        3. Veredicto de Rumelt y "## RESOLUCIÓN FINAL: GO" o "NO-GO".
        *REGLA*: Profundidad analítica citada según APA 7.""",
        agent=agente,
        output_file="4_dictamen_ceo_limpio.md"
    )