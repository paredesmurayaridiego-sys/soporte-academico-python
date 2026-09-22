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
