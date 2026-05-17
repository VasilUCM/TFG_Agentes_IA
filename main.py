import sys
from crewai import Crew, Process
from agentes import crear_agente_analista, crear_agente_operaciones, crear_agente_marketing, crear_agente_ceo
from tareas import tarea_analisis_entorno, tarea_auditoria_operativa, tarea_marketing, tarea_decision_ceo

# --- CLASE MÁGICA PARA CAPTURAR TODO EL RAZONAMIENTO ---
# Copia todo lo que sale por la terminal y lo va guardando en el archivo .txt en tiempo real
class RegistroTerminal:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)  # Muestra en la pantalla
        self.log.write(message)       # Guarda en el .txt
        self.log.flush()              # Fuerza a que se guarde al instante

    def flush(self):
        self.terminal.flush()
        self.log.flush()

if __name__ == "__main__":
    # Redirigimos la salida estándar de Python a nuestro interceptador
    sys.stdout = RegistroTerminal("output.txt")

    print("==================================================")
    print(" INICIANDO SIMULACIÓN AGÉNTICA (KNOWLEDGE BASE)")
    print("==================================================\n")

    # 1. Instanciar agentes
    a_analista = crear_agente_analista()
    a_operaciones = crear_agente_operaciones()
    a_marketing = crear_agente_marketing()
    a_ceo = crear_agente_ceo()

    # 2. Asignar Tareas
    t_entorno = tarea_analisis_entorno(a_analista)
    t_operaciones = tarea_auditoria_operativa(a_operaciones)
    t_marketing = tarea_marketing(a_marketing)
    t_ceo = tarea_decision_ceo(a_ceo)

    # 3. Lanzar Crew
    comite_direccion = Crew(
        agents=[a_analista, a_operaciones, a_marketing, a_ceo],
        tasks=[t_entorno, t_operaciones, t_marketing, t_ceo],
        process=Process.sequential,
        verbose=True # <-- Esto es lo que genera el razonamiento que ahora estamos capturando
    )

    try:
        resultado_final = comite_direccion.kickoff()
        print("\n==================================================")
        print(" SIMULACIÓN COMPLETADA CON ÉXITO")
        print("==================================================")
        print("\n[SISTEMA] El dictamen final y TODO el razonamiento de los agentes se ha guardado en 'output.txt'.")
        
    except Exception as e:
        print("\n[ERROR DE EJECUCIÓN]:", e)