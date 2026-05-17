from crewai import Task

def tarea_analisis_entorno(agente):
    return Task(
        description="""
        REGLA DE ORO: Utiliza tu conocimiento experto sobre el mercado internacional y la macroeconomía japonesa para realizar este análisis sobre el Aceite de Oliva Virgen Extra (AOVE).
        
        EJECUTA EL SIGUIENTE ALGORITMO SECUENCIAL:
        Fase 1: Extrae datos empíricos para las 6 dimensiones PESTEL del mercado japonés enfocado al Aceite de Oliva. Asigna a cada variable una puntuación del 1 (Amenaza) al 5 (Oportunidad) y calcula la media matemática.
        Fase 2: Aplica el modelo CAGE de Ghemawat. Compara España y Japón en distancia Cultural, Administrativa, Geográfica y Económica. 
        Fase 2.1: Basándote en variables socioculturales, determina si Japón es una Cultura de "Alto Contexto" o "Bajo Contexto" (Hall, 1976).
        Fase 3: Aplica las 5 Fuerzas de Porter para el aceite de oliva en Japón, asignando una intensidad (Baja, Media, Alta) debidamente justificada.
        """,
        expected_output="Informe estructurado con: 1. PESTEL Ponderado con nota media, 2. CAGE y clasificación de Hall, 3. Matriz de Porter.",
        agent=agente
    )

def tarea_auditoria_operativa(agente):
    return Task(
        description="""
        REGLA DE ORO: Basa tu auditoría en tu conocimiento técnico sobre comercio exterior, aduanas japonesas y logística internacional. Lee detenidamente el informe del Analista antes de empezar.
        
        EJECUTA EL SIGUIENTE ÁRBOL DE DECISIÓN:
        Fase 1: Busca y detalla el arancel aplicable bajo el Tratado de Libre Comercio (EPA UE-Japón) para la exportación de AOVE.
        Fase 2: Rastrea Barreras No Arancelarias (NTMs) del sector agroalimentario en Japón y clasifícalas en [BARRERAS INTRÍNSECAS] (ej. LMR, pesticidas) y [BARRERAS EXTRÍNSECAS] (ej. normativas de etiquetado JAS, embalaje).
        Fase 3: Elabora una Matriz de Fricción Operativa identificando qué elementos logísticos generarán "Escalada de Precios" (ej. cadena de frío, controles sanitarios, tiempos de aduana en Yokohama/Tokio).
        """,
        expected_output="Matriz de riesgos logísticos y clasificación estricta de barreras Intrínsecas/Extrínsecas.",
        agent=agente
    )

def tarea_marketing(agente):
    return Task(
        description="""
        Lee los outputs de los Agentes Analista y Operaciones. Formula el plan comercial bajo la teoría de estandarización vs adaptación:
        1. PRODUCTO: Basándote en las NTMs del Agente de Operaciones, decide de forma vinculante si la adaptación debe ser Intrínseca o si basta con Extrínseca (Packaging).
        2. PRECIO: Lee la Escalada de Precios de Operaciones. Justifica teóricamente la aplicación de un "Precio de Prestigio (Skimming)" para absorber esos costes logísticos. Tienes estrictamente prohibido usar una estrategia de penetración.
        3. DISTRIBUCIÓN: Propón un canal Selectivo o Exclusivo (ej. canal HORECA premium o tiendas gourmet Depachika).
        4. PROMOCIÓN: Lee la clasificación de Hall del Analista. Si es "Alto Contexto", diseña un mensaje visual, sutil y centrado en la confianza y el Efecto País de Origen.
        """,
        expected_output="Plan Comercial (4Ps) donde CADA variable esté justificada basándose explícitamente en las restricciones operativas de los agentes previos.",
        agent=agente
    )

def tarea_decision_ceo(agente):
    return Task(
        description="""
        Lee todos los reportes de los agentes 1, 2 y 3. Ejecuta la consolidación final:
        Fase 1: Construye una Matriz TOWS cruzando las Fortalezas/Debilidades del AOVE Español Premium con las Oportunidades/Amenazas detectadas en Japón por los agentes anteriores. Formula estrategias CAME.
        Fase 2: Pasa el triple filtro estratégico (S.A.F. - Idoneidad, Factibilidad, Aceptabilidad), indicando expresamente [Cumple] o [No Cumple] en cada una.
        Fase 3: Emite el DICTAMEN VINCULANTE FINAL según Rumelt (Diagnóstico, Política Rectora, Acciones). Finaliza obligatoriamente el documento con "## RESOLUCIÓN FINAL: GO" o "## RESOLUCIÓN FINAL: NO-GO".
        """,
        expected_output="Dictamen corporativo final con Matriz TOWS, evaluación del Filtro S.A.F. y resolución clara de GO/NO-GO.",
        agent=agente
    )