# Parte II — Modificar una reserva sin perder la original

**Examen individual · 60 minutos · 50 puntos · Sin IA.**

Adapte **solo `modificar_reserva` en `reservas.py`**, agregue pruebas en
`tests/test_estudiante.py` y complete `ENTREGA.md`. Conserve las funciones
auxiliares, las firmas, `pytest.ini` y las pruebas base sin cambios.

El sistema es deliberadamente pequeño: listas y diccionarios en memoria,
sin base de datos, interfaz, archivos de datos, servicios externos ni concurrencia.
Todas las reglas que necesita están aquí. No debe conocer políticas de los
proyectos del semestre. Este ejercicio aplica requisitos, pruebas y Git
de las presentaciones 1–7; se proporcionan la sintaxis y las ayudas operativas.

## Preparación del entorno — antes de iniciar el examen

Necesita Python **3.11 o posterior**, Git y una cuenta de GitHub con acceso
comprobado y conexión a internet para instalar pytest. `requirements.txt` declara
solo pytest; pip descarga automáticamente sus dependencias internas.
Una carpeta `.venv` no es portable: créela en su computadora.

Desde esta carpeta, en macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest --version
.venv/bin/python -m pytest -q
```

En Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest --version
.\.venv\Scripts\python.exe -m pytest -q
```

No se calificará la memorización de comandos. No actualice paquetes durante el examen.

## Organización de los 60 minutos

| Minutos | Trabajo |
|---|---|
| 0–10 | Leer contratos, ejecutar pruebas base y registrar el resultado inicial. |
| 10–30 | Adaptar la función usando las ayudas proporcionadas. |
| 30–45 | Agregar pruebas, investigar fallos y corregir. |
| 45–50 | Completar la explicación y trazabilidad en ENTREGA.md. |
| 50–60 | Commit, push, verificación del repositorio y entrega del enlace y commit. |

## Datos y contrato de la función

```python
modificar_reserva(reservas, id_reserva, nuevo_inicio, nuevo_fin)
```

`reservas` es una lista de diccionarios como este:

```python
{"id": "R1", "sala": "A", "inicio": 540, "fin": 600,
 "estado": "confirmada"}
```

- `id` y `sala`: cadenas; los IDs son únicos.
- `inicio` y `fin`: minutos enteros desde medianoche de un mismo día.
  09:00 = 540; 10:00 = 600; 10:30 = 630; 11:00 = 660; 11:30 = 690.
- `estado`: `"confirmada"` o `"cancelada"`.
- `id_reserva`: cadena que identifica la reserva que se desea modificar.
- `nuevo_inicio` y `nuevo_fin`: enteros. No se evalúan otros tipos de datos.
- La lista inicial tiene registros bien formados e intervalos válidos.
- No se comprueban fecha actual, permisos, capacidad, duración mínima ni horario
  comercial. El intervalo solo debe cumplir la regla RF-03.

La función devuelve **una cadena exacta**, no un diccionario ni una excepción
para estos casos. Evalúe los rechazos en el siguiente orden:

| ID | Condición y resultado obligatorio |
|---|---|
| RF-01 | Si el ID no existe, devolver `"NO_EXISTE"`. No cambiar ningún dato. |
| RF-02 | Si la reserva objetivo está cancelada, devolver `"CANCELADA"`. No cambiar ningún dato. |
| RF-03 | Si no se cumple `0 <= nuevo_inicio < nuevo_fin <= 1440`, devolver `"HORARIO_INVALIDO"`. No cambiar ningún dato. |
| RF-04 | Si el intervalo propuesto se superpone con **otra** reserva **confirmada de la misma sala**, devolver `"CONFLICTO"`. Conservar íntegramente la lista y todos sus registros. |
| RF-05 | Si se cumplen las condiciones, devolver `"OK"` y actualizar únicamente `inicio` y `fin` de la reserva objetivo. Conservar identidad, sala, estado, orden, cantidad de registros y todas las demás reservas. |

Los intervalos adyacentes están permitidos: 09:00–10:00 y 10:00–11:00
no entran en conflicto. La reserva objetivo no entra en conflicto consigo misma.
Las canceladas y las de otras salas no ocupan el intervalo de la sala objetivo.
Pedir el mismo horario de la reserva objetivo puede devolver `"OK"` si no hay
conflicto con otra reserva confirmada.

**Ayuda lista para usar:**
`hay_conflicto(reservas, id_reserva, nuevo_inicio, nuevo_fin)` devuelve `True`
si existe el conflicto de RF-04 y `False` si no existe. No cambia datos.
Se llama cuando el ID existe y el intervalo propuesto es válido.
La función `se_superponen` también está implementada; no debe reescribirla.

### Escenario de referencia

En sala A, R1 ocupa 540–600 y R2 ocupa 600–660; ambas están confirmadas.
Solicitar el cambio de R1 a 630–690 devuelve `"CONFLICTO"`.
R1 sigue en 540–600 y R2 sigue en 600–660, con todos sus demás datos intactos.
Si se solicita 720–780 y no hay otra reserva en ese intervalo, devuelve `"OK"`
y solo cambia el horario de R1.

## Pruebas que debe escribir

Conserve las tres pruebas de `tests/test_base.py`. Que pasen no significa que
se satisfagan todos los requisitos. Escriba **al menos cuatro pruebas propias**:

1. Cambio válido: compruebe `"OK"`, el nuevo horario y la conservación de otra reserva.
2. Conflicto: compruebe la devolución exacta de `"CONFLICTO"`.
3. Conservación ante conflicto: compare la **lista completa** con una copia
   independiente anterior. Puede reutilizar los datos del caso 2 en una prueba separada.
4. Límite adyacente: compruebe que un intervalo que comienza exactamente cuando
   termina otra reserva es aceptado y deja el horario esperado.

Use datos nuevos en cada prueba. `deepcopy`, ya importado en el archivo de
pruebas del estudiante, permite crear una copia independiente:

```python
antes = deepcopy(datos)
# Ejecutar aquí la operación que se va a comprobar.
assert datos == antes  # Adecuado para un rechazo que no debe cambiar datos.
```

Los resultados esperados se obtienen de RF-01 a RF-05, no copiando la salida
actual. No se exigen fixtures, parametrización, mocks ni un porcentaje de cobertura.
El docente puede comprobar cualquiera de las reglas publicadas; no hay reglas ocultas.

### Ejemplo simple de pytest proporcionado

```python
from reservas import se_superponen

def test_ejemplo_intervalos_adyacentes():
    resultado = se_superponen(540, 600, 600, 660)
    assert resultado is False
```

`test_` permite identificar una prueba; `assert` comprueba la expectativa.
Este ejemplo ya está en la suite base y no cuenta como prueba propia.

**Comando exacto para toda la suite:**

- macOS/Linux: `.venv/bin/python -m pytest -q`
- Windows: `.\.venv\Scripts\python.exe -m pytest -q`

## Referencia breve de Git y entrega

Antes del examen, tenga un repositorio **privado y vacío** llamado, por ejemplo,
`parcial1-codigo`. No agregue README, licencia ni .gitignore desde GitHub al crearlo.
Conceda acceso al usuario que indique el docente. Use sus credenciales normales;
no escriba tokens ni contraseñas en archivos, comandos compartidos o documentación.

Para comenzar desde el ZIP proporcionado, dentro de esta carpeta:

```bash
git init
git branch -M main
git add .gitignore README.md requirements.txt pytest.ini reservas.py tests ENTREGA.md
git commit -m "Registra proyecto inicial del examen"
```

Configure una sola vez el remoto, reemplazando la URL de ejemplo por la suya:

```bash
git remote add origin https://github.com/USUARIO/parcial1-CODIGO.git
```

Al terminar el trabajo:

```bash
git status
git diff
git add reservas.py tests/test_estudiante.py ENTREGA.md
git commit -m "Adapta modificacion de reservas y agrega pruebas"
git push -u origin main
git rev-parse HEAD
```

Si ya inicializó Git y configuró `origin` durante la preparación, no repita esos
pasos. Este examen usa una entrega individual directa en `main`; no requiere un
pull request ni crear un repositorio a través de comandos nuevos.

Abra GitHub y compruebe que aparecen el código, las pruebas y `ENTREGA.md`.
Entregue por el canal indicado por el docente:

- URL del repositorio y rama `main`.
- Hash del commit final obtenido con `git rev-parse HEAD`.

El hash final se pega en el mensaje/formulario de entrega **después** del último
commit; no intente guardar dentro de ese mismo commit su propio hash.
No incluya `.venv`, cachés ni credenciales en Git. Si GitHub no está
disponible, avise y entregue un ZIP de los archivos de código, pruebas y
documentación, sin esas carpetas, dentro del plazo. No retrase la entrega por red.

## Calificación de la parte práctica

| Criterio | Puntos |
|---|---:|
| Comportamiento conforme a RF-01–RF-05, incluida la conservación ante rechazo | 25 |
| Pruebas propias con expectativas correctas y aserciones útiles | 15 |
| Explicación, trazabilidad y resultados reales en ENTREGA.md | 5 |
| Repositorio revisable, archivos necesarios y versión identificada | 5 |
| **Total** | **50** |

Se otorga crédito parcial a pruebas correctas aunque detecten un fallo que no
alcance a corregir. No se premia el número bruto de commits o líneas de código.
