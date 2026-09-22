# PRUEBAS DEL SISTEMA

## Sistema de Orientación y Registro de Atenciones

Este documento presenta las pruebas realizadas al Sistema de Soporte Académico desarrollado en Python.

## 1. Prueba de datos válidos

**Objetivo:** Verificar que el sistema permita registrar correctamente una solicitud con datos válidos.

**Datos utilizados:**

* Código: `n12345`
* Nombre: `Diego Paredes`
* Tipo de consulta: `Matrícula`
* Detalle: `problema con mi matricula`

**Resultado esperado:**
El sistema debe aceptar los datos y registrar la solicitud correctamente.

**Resultado obtenido:**
La solicitud fue registrada correctamente y se asignó la prioridad **Alta**.

**Estado:** APROBADA.

---

## 2. Prueba de código vacío

**Objetivo:** Verificar que el sistema no permita registrar una solicitud cuando el código está vacío.

**Dato utilizado:**

* Código: vacío.

**Resultado esperado:**
El sistema debe mostrar un mensaje de error indicando que el código no puede estar vacío.

**Resultado obtenido:**
El sistema mostró el mensaje:

`[ERROR] El código no puede estar vacío.`

**Estado:** APROBADA.

---

## 3. Prueba de tipo de consulta incorrecto

**Objetivo:** Verificar que el sistema rechace una opción de consulta que no pertenece a la lista permitida.

**Dato utilizado:**

* Opción ingresada: `9`

**Resultado esperado:**
El sistema debe rechazar la opción y solicitar una opción válida.

**Resultado obtenido:**
El sistema mostró:

`[ERROR] Seleccione una opción válida. Ingrese un número del 1 al 5.`

**Estado:** APROBADA.

---

## 4. Prueba de prioridad alta

**Objetivo:** Verificar que el sistema asigne correctamente una prioridad alta.

**Dato utilizado:**

* Tipo de consulta: `Matrícula`

**Resultado esperado:**
La consulta de matrícula debe recibir prioridad **Alta**.

**Resultado obtenido:**
El sistema asignó correctamente la prioridad:

`Alta`

**Estado:** APROBADA.

---

## 5. Prueba de prioridad baja

**Objetivo:** Verificar que el sistema asigne correctamente una prioridad baja.

**Dato utilizado:**

* Tipo de consulta: `Constancia`

**Resultado esperado:**
La consulta de constancia debe recibir prioridad **Baja**.

**Resultado obtenido:**
El sistema asignó correctamente la prioridad:

`Baja`

**Estado:** APROBADA.

---

## 6. Prueba de múltiples solicitudes

**Objetivo:** Verificar que el sistema permita registrar al menos tres solicitudes durante una misma ejecución.

**Solicitudes registradas durante las pruebas:**

| N.º | Código   | Tipo de consulta | Prioridad |
| --- | -------- | ---------------- | --------- |
| 1   | `n12345` | Matrícula        | Alta      |
| 2   | `n67890` | Constancia       | Baja      |
| 3   | `n54321` | Plataforma       | Media     |

**Resultado esperado:**
El sistema debe permitir registrar tres o más solicitudes durante una ejecución.

**Resultado obtenido:**
Se registraron correctamente tres solicitudes y el sistema permitió continuar utilizando el menú principal.

**Estado:** APROBADA.

---

## 7. Resumen de pruebas

| N.º | Prueba                      | Resultado |
| --- | --------------------------- | --------- |
| 1   | Datos válidos               | APROBADA  |
| 2   | Código vacío                | APROBADA  |
| 3   | Tipo de consulta incorrecto | APROBADA  |
| 4   | Prioridad alta              | APROBADA  |
| 5   | Prioridad baja              | APROBADA  |
| 6   | Múltiples solicitudes       | APROBADA  |

## Conclusión

Las pruebas realizadas permitieron comprobar el funcionamiento de las principales validaciones y funcionalidades del Sistema de Soporte Académico.

El sistema permite registrar solicitudes, validar los datos ingresados, asignar prioridades según el tipo de consulta, buscar solicitudes, actualizar estados y mostrar información de las solicitudes registradas.
