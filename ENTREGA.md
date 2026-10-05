# Entrega individual — Parte práctica

- Nombre y código: Luciana Soza
- URL del repositorio privado: https://github.com/luci-solar34/Examen-Primer-Parcial.git
- Rama entregada: rama_luci
- Commit final: se presenta en el formulario/mensaje de entrega después del último commit.

## Resultado inicial

- Comando ejecutado:
- Resumen real de pytest antes de cambiar el código:
- No se sabia concretamente si se verificaba si habia conflicto o no.

## Cambios y requisitos

Se agrego la funcion de ver conflicto para ver si habia anteriromente una reserva en donde se quiere modificar.

## Trazabilidad de sus pruebas

| Nombre de la prueba | Requisito | Resultado esperado |
|---|---|---|
| def test_se_puede_reservar_sin_conflicto| Poder modificar una reserva y no hay conflicto| Devolver "OK|
| def test_existe_conflicto_los_datos_no_se_modifican()| Los datos no se deben cambiar si existe un conflicto en el cambio de reserva| No modifica los datos|
| def test_existe_conflicto_no_se_puede_reservar| Si existe un conflicto debe devolver el mensaje de "Conflicto"| Devolver "CONFLICTO"|
| | | |

## Resultado final y límites

- Comando ejecutado:
- Resumen real de pytest (passed/failed y otros resultados si aparecen):
- Mencionando sobre esto lo principal era observa si existia un conflictp al modificar reserva lo detecta
- ¿Qué comportamiento sigue sin comprobar? Escriba una limitación concreta:
- Talvez verificar el tema de las salas si realmente existen

No presente una prueba fallida como aprobada. Conserve y explique cualquier pendiente.
