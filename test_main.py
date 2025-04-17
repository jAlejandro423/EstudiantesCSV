import unittest

from main import ControlEstudiantes, Estudiante


class TestEstudiantesCSV(unittest.TestCase):
    # Prueba 1: Procesar líneas con materias duplicadas
    def test_procesar_lineas_ignora_duplicados(self):
        procesador = ControlEstudiantes()
        lineas = [
            "123,Lulú López,1040,Cálculo",
            "123,Lulú López,1040,Cálculo"  # Línea duplicada
        ]
        procesador.procesar_lineas(lineas)
        estudiante = procesador.obtener_estudiantes()[0]
        self.assertEqual(estudiante.total_materias, 1)  # Verificación

    # Prueba 2: Agregar materia duplicada a Estudiante
    def test_agregar_materia_sin_duplicados(self):
        estudiante = Estudiante("123", "Lulú López")
        estudiante.agregar_materia("1040")
        estudiante.agregar_materia("1040")  # Intento duplicado
        self.assertEqual(estudiante.total_materias, 1)  # Verificación

if __name__ == "__main__":
    unittest.main()
