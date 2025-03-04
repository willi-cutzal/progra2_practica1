import statistics


def analizar_datos(datos):
    """
    Calcula el promedio y la desviación estándar de una lista de números.
    :param datos: Lista de números.
    :return: Diccionario con promedio y desviación estándar.
    """
    if not datos:
        return {"error": "Lista vacía"}
    return {
        "promedio": statistics.mean(datos),
        "desviacion_estandar": statistics.stdev(datos) if len(datos) > 1 else 0
    }
    
