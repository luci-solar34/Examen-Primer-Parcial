"""Pruebas proporcionadas: conservarlas sin cambios."""
from reservas import modificar_reserva, se_superponen


def test_ejemplo_intervalos_adyacentes():
    # Preparar: 09:00-10:00 y 10:00-11:00, en minutos desde medianoche.
    resultado = se_superponen(540, 600, 600, 660)
    # Comprobar una expectativa explícita: tocar un extremo no es conflicto.
    assert resultado is False


def test_intervalos_con_superposicion():
    assert se_superponen(540, 600, 570, 630) is True


def test_modificacion_sin_otras_reservas():
    datos = [dict(id="R1", sala="A", inicio=540, fin=600,
                  estado="confirmada")]
    assert modificar_reserva(datos, "R1", 720, 780) == "OK"
    assert datos[0]["inicio"] == 720
    assert datos[0]["fin"] == 780
