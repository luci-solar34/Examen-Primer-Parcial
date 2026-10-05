"""Escriba aquí sus pruebas. No borre ni modifique tests/test_base.py.

Cada función de prueba comienza con test_ y usa assert.
Agregue al menos los cuatro casos descritos en el README.
Los imports ya están preparados; deepcopy crea una copia independiente
de la lista y de los diccionarios para comprobar que no se modificaron.
"""
from copy import deepcopy

from reservas import modificar_reserva


# Ejemplo de estructura, sin solución del caso:
def test_se_puede_reservar_sin_conflicto():
    datos = [{"id":"R1","sala":"A","inicio":540,"fin":600,"estado":"confirmada"}]
    antes = deepcopy(datos)
    resultado = modificar_reserva(datos, "R1",720,780)
    assert resultado == "OK"
    # assert datos == antes  # Cuando la operación debe conservar TODO.

def test_existe_conflicto_los_datos_no_se_modifican():
    datos = [{"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
             {"id": "R2", "sala": "A", "inicio": 600, "fin": 630, "estado": "confirmada"}]
    antes = deepcopy(datos)
    resultado = modificar_reserva(datos, "R1", 600, 630)
    # assert resultado == "OK"
    assert datos == antes  # Cuando la operación debe conservar TODO.

def test_existe_conflicto_no_se_puede_reservar():
    datos = [{"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
             {"id": "R2", "sala": "A", "inicio": 600, "fin": 630, "estado": "confirmada"}]
    antes = deepcopy(datos)
    resultado = modificar_reserva(datos, "R1", 600, 630)
    assert resultado == "CONFLICTO"
