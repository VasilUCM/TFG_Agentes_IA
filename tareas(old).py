from crewai import Task

def tarea_analisis_entorno(agente, texto_documentos):
    # Usamos una f-string (f"") para poder inyectar la variable texto_documentos directamente en el texto
    return Task(
        description=f"""
        REGLA DE ORO: Basa tu análisis EXCLUSIVAMENTE en la siguiente información extraída de nuestros documentos oficiales:
        
        [INICIO DE DOCUMENTOS]
        {texto_documentos}
        [FIN DE DOCUMENTOS]
        
        EJECUTA EL SIGUIENTE ALGORITMO SECUENCIAL:
        Fase 1: Extrae datos para las 6 dimensiones PESTEL del mercado japonés enfocado al Aceite de Oliva. Asigna a cada variable una puntuación del 1 (Amenaza) al 5 (Oportunidad) y calcula la media matemática.
        Fase 2: Aplica el modelo CAGE de Ghemawat. Compara España y Japón en distancia Cultural, Administrativa, Geográfica y Económica. 
        Fase 2.1: Basándote en los datos, determina si Japón es una Cultura de "Alto Contexto" o "Bajo Contexto" (Hall, 1976).
        Fase 3: Aplica las 5 Fuerzas de Porter para el aceite de oliva, asignando una intensidad (Baja, Media, Alta) justificada estrictamente con los documentos.
        """,
        expected_output="Informe estructurado con: 1. PESTEL Ponderado con nota media, 2. CAGE y clasificación de Hall, 3. Matriz de Porter. Cita siempre que puedas de qué documento extraes cada dato.",
        agent=agente
    )

def tarea_auditoria_operativa(agente, texto_documentos):
    return Task(
        description=f"""
        REGLA DE ORO: Basa tu auditoría EXCLUSIVAMENTE en el siguiente texto de nuestros documentos oficiales:
        
        [INICIO DE DOCUMENTOS]
        {texto_documentos}
        [FIN DE DOCUMENTOS]
        
        EJECUTA EL SIGUIENTE ÁRBOL DE DECISIÓN:
        Fase 1: Busca el arancel aplicable bajo el Tratado EPA UE-Japón para el AOVE. Si no está, escribe "DATO NO ENCONTRADO EN FUENTE".
        Fase 2: Rastrea Barreras No Arancelarias (NTMs) y clasifícalas en [BARRERAS INTRÍNSECAS] (ej. LMR, pesticidas) y [BARRERAS EXTRÍNSECAS] (ej. etiquetado JAS, embalaje).
        Fase 3: Elabora una Matriz de Fricción Operativa identificando qué elementos logísticos generarán "Escalada de Precios" (ej. cadena de frío, tiempos de aduana en Japón).
        """,
        expected_output="Matriz de riesgos logísticos y clasificación estricta de barreras Intrínsecas/Extrínsecas respaldadas por los documentos.",
        agent=agente
    )

def tarea_marketing(agente):
    return Task(
        description="""
        Lee los outputs de los Agentes Analista y Operaciones. Formula el plan comercial bajo la teoría de estandarización vs adaptación:
        1. PRODUCTO: Basándote en las NTMs del Agente de Operaciones, decide de forma vinculante si la adaptación debe ser Intrínseca o si basta con Extrínseca (Packaging).
        2. PRECIO: Lee la Escalada de Precios. Justifica teóricamente la aplicación de un "Precio de Prestigio (Skimming)" para absorber esos costes logísticos. Tienes prohibido usar estrategia de penetración.
        3. DISTRIBUCIÓN: Propón un canal Selectivo o Exclusivo (ej. canal HORECA premium o tiendas gourmet Depachika).
        4. PROMOCIÓN: Lee la clasificación de Hall del Analista. Si es "Alto Contexto", diseña un mensaje visual, sutil y centrado en la confianza y el Efecto País de Origen.
        """,
        expected_output="Plan Comercial (4Ps) donde CADA variable esté justificada basándose en las restricciones operativas de los agentes previos.",
        agent=agente
    )

def tarea_decision_ceo(agente):
    return Task(
        description="""
        Lee todos los reportes de los agentes 1, 2 y 3. Ejecuta la consolidación final:
        Fase 1: Construye una Matriz TOWS cruzando las Fortalezas/Debilidades del AOVE Español con Oportunidades/Amenazas detectadas en Japón por los agentes anteriores. Formula estrategias CAME.
        Fase 2: Pasa el triple filtro estratégico (S.A.F. - Idoneidad, Factibilidad, Aceptabilidad), indicando expresamente [Cumple] o [No Cumple] en cada una.
        Fase 3: Emite el DICTAMEN VINCULANTE FINAL según Rumelt (Diagnóstico, Política Rectora, Acciones). Finaliza obligatoriamente el documento con "## RESOLUCIÓN FINAL: GO" o "## RESOLUCIÓN FINAL: NO-GO".
        """,
        expected_output="Dictamen corporativo final con Matriz TOWS, evaluación del Filtro S.A.F. y resolución clara de GO/NO-GO.",
        agent=agente
    )