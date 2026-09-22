# TRAZABILIDAD DE REQUISITOS

## Sistema de Orientación y Registro de Atenciones

Este documento relaciona los requisitos solicitados para el proyecto con las funciones implementadas en el programa Python y con las evidencias disponibles.

---

## Requisito 1: Registro de datos básicos

**Descripción:**
El sistema debe permitir registrar los datos básicos de una solicitud de atención.

**Implementación:**
La función `registrar_solicitud()` solicita:

* Código del estudiante.
* Nombre del estudiante.
* Tipo de consulta.
* Detalle de la solicitud.

**Evidencia:**
El sistema muestra un formulario mediante la consola y almacena la información en `solicitudes.json`.

**Estado:** Cumplido.

---

## Requisito 2: Validación del código del estudiante

**Descripción:**
El código del estudiante no debe estar vacío y debe cumplir una longitud mínima.

**Implementación:**
La función `validar_codigo()` verifica que:

* El código no esté vacío.
* Tenga como mínimo 5 caracteres.
* No contenga símbolos.

**Evidencia:**
Durante las pruebas se ingresó un código vacío y un código con menos de 5 caracteres. El sistema rechazó ambos casos.

**Estado:** Cumplido.

---

## Requisito 3: Validación del tipo de consulta

**Descripción:**
El tipo de consulta debe pertenecer a una lista básica de opciones.

**Implementación:**
El sistema permite seleccionar:

1. Matrícula.
2. Pagos.
3. Constancia.
4. Plataforma.
5. Otro.

La validación se realiza mediante `validar_consulta()` y mediante el menú de opciones.

**Evidencia:**
El sistema rechaza opciones diferentes de 1 a 5.

**Estado:** Cumplido.

**Commit relacionado**
---

## Requisito 4: Función para mostrar el menú principal

**Descripción:**
El sistema debe contar con una función sin retorno encargada de mostrar el menú principal.

**Implementación:**
La función `mostrar_menu()` muestra las opciones disponibles del sistema.

**Evidencia:**
El menú se muestra desde la función `main()` durante la ejecución del programa.

**Estado:** Cumplido.

---

## Requisito 5: Asignación de prioridad

**Descripción:**
El sistema debe asignar una prioridad según el tipo de consulta registrada.

**Implementación:**
La función `calcular_prioridad()` asigna automáticamente:

* Matrícula → Alta.
* Pagos → Alta.
* Plataforma → Media.
* Constancia → Baja.
* Otro → Baja.

**Evidencia:**
Las pruebas de prioridad alta y baja fueron registradas en `PRUEBAS.md`.

**Estado:** Cumplido.

**Commit relacionado:** `e7476df`

---

## Requisito 6: Validación de texto obligatorio

**Descripción:**
El sistema debe validar que los campos de texto obligatorios no estén vacíos.

**Implementación:**
La función `validar_texto_obligatorio()` verifica que el texto ingresado no esté vacío y tenga una longitud mínima.

La función `validar_detalle()` utiliza esta validación para comprobar el detalle de la solicitud.

**Evidencia:**
El sistema rechaza información obligatoria vacía durante el registro.

**Estado:** Cumplido.

---

## Requisito 7: Mostrar resumen de la solicitud

**Descripción:**
El sistema debe mostrar un resumen con la información de una solicitud registrada.

**Implementación:**
La función `mostrar_resumen()` muestra los datos principales de la solicitud, incluyendo código, nombre, consulta, detalle, prioridad, estado y fecha.

**Evidencia:**
El resumen se muestra antes de confirmar el registro de una solicitud.

**Estado:** Cumplido.

---

## Requisito 8: Uso de parámetros en las funciones

**Descripción:**
Las funciones deben recibir los datos necesarios mediante parámetros, evitando el uso innecesario de variables globales.

**Implementación:**
Las funciones principales reciben los datos que necesitan mediante parámetros.

Por ejemplo:

* `guardar_solicitudes(solicitudes)`
* `registrar_solicitud(solicitudes)`
* `buscar_solicitud(solicitudes)`
* `actualizar_estado(solicitudes)`
* `mostrar_solicitudes(solicitudes)`

**Evidencia:**
La lista de solicitudes se recibe como parámetro en las funciones que necesitan trabajar con ella.

**Estado:** Cumplido.

---

## Requisito 9: Control del alcance de variables

**Descripción:**
El programa debe diferenciar las variables utilizadas por el programa principal de las variables internas de cada función.

**Implementación:**
Las variables utilizadas dentro de las funciones se crean y utilizan dentro de su propio ámbito.

Por ejemplo, variables como `opcion`, `codigo`, `nombre`, `consulta` y `detalle` se utilizan dentro de las funciones correspondientes.

**Evidencia:**
Las funciones trabajan con variables locales y reciben mediante parámetros los datos que necesitan.

**Estado:** Cumplido.

---

## Requisito 10: Registro de múltiples solicitudes

**Descripción:**
El sistema debe permitir registrar al menos tres solicitudes durante una misma ejecución.

**Implementación:**
La función `main()` mantiene el menú dentro de un ciclo `while`, permitiendo regresar al menú después de cada operación.

La lista `solicitudes` conserva las solicitudes registradas durante la ejecución.

**Evidencia:**
En `PRUEBAS.md` se documentó el registro de tres solicitudes:

1. `n12345` — Matrícula.
2. `n67890` — Constancia.
3. `n54321` — Plataforma.

**Estado:** Cumplido.

---

## Requisito 11: Realización de pruebas

**Descripción:**
El proyecto debe incluir al menos cinco pruebas que permitan verificar el funcionamiento del sistema.

**Implementación:**
Se creó el archivo `PRUEBAS.md`, donde se documentan seis pruebas.

**Pruebas realizadas:**

1. Datos válidos.
2. Código vacío.
3. Tipo de consulta incorrecto.
4. Prioridad alta.
5. Prioridad baja.
6. Múltiples solicitudes.

**Evidencia:**
Todas las pruebas documentadas presentan el estado **APROBADA**.

**Estado:** Cumplido.

**Commit relacionado:** `b59a006`

---

## Requisito 12: Documentación de requisitos y funciones

**Descripción:**
El proyecto debe documentar la relación entre los requisitos solicitados y las funciones implementadas.

**Implementación:**
El archivo `README.md` documenta el proyecto, sus funciones principales y la relación entre los requisitos y la implementación.

Además, este documento presenta la trazabilidad de los requisitos.

**Evidencia:**
El archivo `README.md` contiene la documentación general del proyecto y `TRAZABILIDAD.md` relaciona los requisitos con las funciones correspondientes.

**Estado:** Cumplido.

**Commit relacionado:** `ec0925f`

---

## Matriz de trazabilidad

| Requisito | Función / evidencia | Estado |
|---|---|---|
| 1 | `registrar_solicitud()` | Cumplido |
| 2 | `validar_codigo()` | Cumplido |
| 3 | `validar_consulta()` | Cumplido |
| 4 | `mostrar_menu()` | Cumplido |
| 5 | `calcular_prioridad()` | Cumplido |
| 6 | `validar_texto_obligatorio()` | Cumplido |
| 7 | `mostrar_resumen()` | Cumplido |
| 8 | Parámetros de funciones | Cumplido |
| 9 | Ámbito de variables | Cumplido |
| 10 | `main()` y ciclo `while` | Cumplido |
| 11 | `PRUEBAS.md` | Cumplido |
| 12 | `README.md` y documentación | Cumplido |

## Conclusión

La matriz de trazabilidad permite relacionar los requisitos solicitados con las funciones y documentos que evidencian su implementación en el Sistema de Soporte Académico.
