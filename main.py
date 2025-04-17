from typing import Dict, Set

class Estudiante:
    def __init__(self, cedula: str, nombre: str):
        self.cedula = cedula
        self.nombre = nombre
        self.materias: Set[str] = set()  # Solo almacena códigos (ej: "1040")

    def agregar_materia(self, codigo: str) -> None:
        self.materias.add(codigo)  # El nombre de la materia se ignora

    @property
    def total_materias(self) -> int:
        return len(self.materias)

class LectorCSV:
    @staticmethod
    def leer_lineas(ruta: str) -> list[str]:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return archivo.read().splitlines()

class ControlEstudiantes:
    def __init__(self):
        self.estudiantes: Dict[str, Estudiante] = {}

    def procesar_lineas(self, lineas: list[str]) -> None:
        for linea in lineas:
            # Split de la línea: cedula, nombre, codigo_materia, nombre_materia (ignorado)
            campos = linea.strip().split(',')
            cedula = campos[0]
            nombre = campos[1]
            codigo_materia = campos[2]  # Se usa solo el código
            # El nombre de la materia (campos[3]) no se procesa

            if cedula not in self.estudiantes:
                self.estudiantes[cedula] = Estudiante(cedula, nombre)
            self.estudiantes[cedula].agregar_materia(codigo_materia)

    def obtener_estudiantes(self) -> list[Estudiante]:
        return list(self.estudiantes.values())

class ControlCSV:
    def __init__(self):
        self.lector = LectorCSV()
        self.procesador = ControlEstudiantes()

    def ejecutar(self, ruta: str) -> None:
        lineas = self.lector.leer_lineas(ruta)
        self.procesador.procesar_lineas(lineas)
        for estudiante in self.procesador.obtener_estudiantes():
            print(f"{estudiante.nombre}: {estudiante.total_materias} materias")

# Uso
if __name__ == "__main__":
    control = ControlCSV()
    ruta = "EstudiantesCSV.csv"
    try:
        control.ejecutar(ruta)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")