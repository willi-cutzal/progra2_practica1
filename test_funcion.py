import pytest
from funcion import analizar_datos

def test_analizar_datos():
    """
    pruebas de la función analizar datos
    """
    assert analizar_datos([1, 2, 3, 4, 5]) == {"promedio": 3, "desviacion_estandar": pytest.approx(1.58, 0.01)}
    assert analizar_datos([10]) == {"promedio": 10, "desviacion_estandar": 0}
    assert analizar_datos([]) == {"error": "Lista vacía"}

