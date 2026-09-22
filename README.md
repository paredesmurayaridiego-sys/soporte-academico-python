# Sistema de Orientación y Registro de Atenciones

## Información del proyecto

**Caso práctico:** Sistema de orientación y registro de atenciones para el módulo de soporte académico.

**Lenguaje utilizado:** Python

**Curso:** Fundamentos de Programación

**Integrantes:**

* [Completar con nombres y códigos de los integrantes]

## Descripción

Este proyecto desarrolla un sistema de soporte académico que permite registrar, buscar y actualizar solicitudes realizadas por estudiantes.

El sistema permite almacenar información como el código del estudiante, nombre, tipo de consulta, detalle, prioridad, estado y fecha de atención.

La información registrada se guarda en un archivo JSON para poder conservar las solicitudes durante diferentes ejecuciones del programa.

## Funcionalidades principales

* Registrar solicitudes de estudiantes.
* Validar los datos ingresados.
* Buscar solicitudes por código o nombre.
* Actualizar el estado de una solicitud.
* Mostrar solicitudes según diferentes filtros.
* Mostrar estadísticas de las solicitudes.
* Guardar y cargar información mediante un archivo JSON.
* Mostrar ayuda sobre el funcionamiento del sistema.

## Requisitos trabajados

El proyecto aplica los siguientes conceptos:

1. Registro de datos básicos del estudiante.
2. Validación del código del estudiante.
3. Validación del tipo de consulta.
4. Uso de funciones sin retorno.
5. Uso de funciones con retorno.
6. Validación de datos obligatorios.
7. Presentación del resumen de una solicitud.
8. Uso de parámetros en las funciones.
9. Control del alcance de las variables.
10. Registro de múltiples solicitudes durante una ejecución.
11. Realización de pruebas del sistema.
12. Documentación de las funciones utilizadas.

## Archivos principales

* `main.py` → Programa principal.
* `solicitudes.json` → Archivo donde se almacenan las solicitudes.
* `.gitignore` → Archivos y carpetas que Git no debe considerar.
* `README.md` → Documentación básica del proyecto.

## Ejecución

Para ejecutar el programa se utiliza:

```bash
python main.py
```

## Control de versiones

El proyecto utiliza Git y GitHub para registrar progresivamente los cambios realizados.

Se utilizan commits descriptivos para identificar las mejoras y modificaciones realizadas durante el desarrollo.

También se utilizan ramas `feature/` para realizar cambios importantes antes de integrarlos a la rama principal `main`.

## Repositorio

Repositorio del proyecto:

https://github.com/paredesmurayaridiego-sys/soporte-academico-python.git
