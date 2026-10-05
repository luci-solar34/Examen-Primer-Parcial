"""Ejercicio de examen: datos ficticios en memoria, sin red ni base de datos."""


def se_superponen(inicio_a, fin_a, inicio_b, fin_b):
    """Los extremos adyacentes NO se superponen: [inicio, fin)."""
    return inicio_a < fin_b and inicio_b < fin_a


def hay_conflicto(reservas, id_reserva, nuevo_inicio, nuevo_fin):
    """Ayuda proporcionada; no modificar.

    Requiere que id_reserva exista y que el intervalo propuesto sea válido.
    Consulta sin modificar datos. Omite la propia reserva, las canceladas
    y las reservas de otra sala.
    """
    objetivo = next(r for r in reservas if r["id"] == id_reserva)
    for otra in reservas:
        if (otra["id"] != id_reserva
                and otra["sala"] == objetivo["sala"]
                and otra["estado"] == "confirmada"
                and se_superponen(nuevo_inicio, nuevo_fin,
                                  otra["inicio"], otra["fin"])):
            return True
    return False


def modificar_reserva(reservas, id_reserva, nuevo_inicio, nuevo_fin):
    """Función que debe adaptar el estudiante según RF-01 a RF-05 del README.

    Devuelve una cadena de resultado. Solo una modificación aceptada puede
    cambiar inicio y fin de la reserva objetivo. Toda otra información
    debe conservarse. La versión inicial aún no cumple todas las reglas.
    """
    objetivo = next((r for r in reservas if r["id"] == id_reserva), None)
    if objetivo is None:
        return "NO_EXISTE"
    if objetivo["estado"] == "cancelada":
        return "CANCELADA"
    if not 0 <= nuevo_inicio < nuevo_fin <= 1440:
        return "HORARIO_INVALIDO"

    # TODO: adaptar este comportamiento a los requisitos del examen.

    if hay_conflicto(reservas, id_reserva, nuevo_inicio, nuevo_fin):
        return "CONFLICTO"

    objetivo["inicio"] = nuevo_inicio
    objetivo["fin"] = nuevo_fin

    return "OK"
