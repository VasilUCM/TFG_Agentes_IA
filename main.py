import sys
import time
from crewai import Crew, Process
from agentes import crear_agente_analista, crear_agente_operaciones, crear_agente_marketing, crear_agente_ceo
from tareas import tarea_analisis_entorno, tarea_auditoria_operativa, tarea_marketing, tarea_decision_ceo

# --- CLASE MÁGICA PARA CAPTURAR EL RAZONAMIENTO EN BRUTO ---
class RegistroTerminal:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)  
        self.log.write(message)       
        self.log.flush()              

    def flush(self):
        self.terminal.flush()
        self.log.flush()

if __name__ == "__main__":
    # Generamos un nombre único con la fecha y hora para no pisar ejecuciones anteriores
    nombre_archivo = f"output_terminal_{time.strftime('%Y%m%d_%H%M%S')}.txt"
    sys.stdout = RegistroTerminal(nombre_archivo)

    print("==================================================")
    print(" INICIANDO SIMULACIÓN AGÉNTICA (TIER 1 - ALTO RENDIMIENTO)")
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

    # 3. Lanzar Crew (Velocidad máxima, sin límites artificiales)
    comite_direccion = Crew(
        agents=[a_analista, a_operaciones, a_marketing, a_ceo],
        tasks=[t_entorno, t_operaciones, t_marketing, t_ceo],
        process=Process.sequential,
        verbose=True 
    )

    try:
        resultado_final = comite_direccion.kickoff()
        print("\n==================================================")
        print(" SIMULACIÓN COMPLETADA CON ÉXITO")
        print("==================================================")
        print(f"\n[SISTEMA] El log de la terminal se ha guardado en '{nombre_archivo}'.")
        print("[SISTEMA] Los informes limpios para el TFG se han generado en los archivos .md.")
        
    except Exception as e:
        print("\n[ERROR DE EJECUCIÓN]:", e)