# Sistema de Orientación y Registro de Atenciones

## Información del proyecto

**Caso práctico:** Sistema de orientación y registro de atenciones para el módulo de soporte académico.

**Lenguaje utilizado:** Python

**Curso:** Fundamentos de Programación

**Integrantes:**

* [Completar con nombres y códigos de los integrantes]

## Descripción

El proyecto desarrolla un sistema de soporte académico que permite registrar, buscar y actualizar solicitudes realizadas por estudiantes.

El sistema almacena información como código, nombre, tipo de consulta, detalle, prioridad, estado y fecha de atención.

Las solicitudes se guardan en un archivo JSON para conservar la información durante diferentes ejecuciones del programa.

## Funcionalidades principales

* Registrar solicitudes de estudiantes.
* Validar el código del estudiante.
* Validar el nombre del estudiante.
* Validar el tipo de consulta.
* Validar información obligatoria.
* Asignar automáticamente una prioridad según el tipo de consulta.
* Mostrar el resumen de una solicitud.
* Buscar solicitudes por código o nombre.
* Actualizar el estado de una solicitud.
* Mostrar solicitudes mediante filtros.
* Mostrar estadísticas.
* Guardar y cargar información mediante JSON.
* Mostrar ayuda del sistema.

## Funciones principales

### `cargar_solicitudes()`

Carga las solicitudes almacenadas en el archivo JSON.

### `guardar_solicitudes(solicitudes)`

Guarda las solicitudes registradas en el archivo JSON.

### `validar_codigo(codigo)`

Valida que el código no esté vacío, tenga como mínimo cinco caracteres y utilice solamente letras y números.

### `validar_nombre(nombre)`

Valida que el nombre no esté vacío y que contenga solamente letras y espacios.

### `validar_texto_obligatorio(texto, campo)`

Valida que un campo obligatorio no esté vacío y tenga una longitud mínima.

### `validar_detalle(detalle)`

Utiliza la función de validación de texto obligatorio para comprobar el detalle de la solicitud.

### `validar_consulta(consulta)`

Comprueba que el tipo de consulta pertenezca a las opciones permitidas: Matrícula, Pagos, Constancia, Plataforma u Otro.

### `normalizar_consulta(consulta)`

Permite mantener una escritura uniforme del tipo de consulta.

### `calcular_prioridad(consulta)`

Función con retorno que asigna una prioridad de acuerdo con el tipo de consulta.

* Matrícula → Alta
* Pagos → Alta
* Plataforma → Media
* Constancia → Baja
* Otro → Baja

### `mostrar_encabezado()`

Muestra el encabezado principal del sistema.

### `mostrar_menu()`

Muestra las opciones disponibles del programa.

### `mostrar_ayuda()`

Explica las principales opciones y tipos de consulta del sistema.

### `mostrar_resumen(solicitud)`

Muestra de forma organizada los datos de una solicitud registrada.

### `registrar_solicitud(solicitudes)`

Recibe la lista de solicitudes mediante un parámetro y permite registrar una nueva solicitud.

### `buscar_solicitud(solicitudes)`

Permite buscar solicitudes por código o nombre.

### `actualizar_estado(solicitudes)`

Permite modificar el estado de una solicitud y registrar su última actualización.

### `mostrar_solicitudes(solicitudes)`

Permite mostrar las solicitudes utilizando diferentes filtros.

### `mostrar_estadisticas(solicitudes)`

Calcula y muestra estadísticas de las solicitudes registradas.

### `main()`

Controla el funcionamiento general del sistema y contiene el menú principal.

## Relación entre requisitos y funciones

| Requisito                           | Implementación                                         |
| ----------------------------------- | ------------------------------------------------------ |
| 1. Registrar datos básicos          | `registrar_solicitud()`                                |
| 2. Validar código                   | `validar_codigo()`                                     |
| 3. Validar tipo de consulta         | `validar_consulta()`                                   |
| 4. Función sin retorno para menú    | `mostrar_menu()`                                       |
| 5. Asignar prioridad según consulta | `calcular_prioridad()`                                 |
| 6. Validar texto obligatorio        | `validar_texto_obligatorio()` y `validar_detalle()`    |
| 7. Mostrar resumen                  | `mostrar_resumen()`                                    |
| 8. Uso de parámetros                | Funciones que reciben `solicitudes` y otros parámetros |
| 9. Alcance de variables             | Variables locales y parámetros dentro de las funciones |
| 10. Registrar múltiples solicitudes | `registrar_solicitud()` dentro del ciclo principal     |
| 11. Realizar pruebas                | Pruebas de datos válidos, vacíos e incorrectos         |
| 12. Documentación                   | Este archivo `README.md`                               |

## Pruebas realizadas

Se realizaron pruebas durante la ejecución del sistema.

### Prueba 1: Registro válido

Se registró una solicitud de tipo Matrícula.

**Resultado:** solicitud registrada correctamente.

**Prioridad obtenida:** Alta.

### Prueba 2: Registro válido con Constancia

Se registró una solicitud de tipo Constancia.

**Resultado:** solicitud registrada correctamente.

**Prioridad obtenida:** Baja.

### Prueba 3: Registro válido con Plataforma

Se registró una solicitud de tipo Plataforma.

**Resultado:** solicitud registrada correctamente.

**Prioridad obtenida:** Media.

### Prueba 4: Código vacío

Se dejó vacío el código del estudiante.

**Resultado:** el sistema rechazó el dato y solicitó nuevamente el código.

### Prueba 5: Código demasiado corto

Se ingresó un código con menos de cinco caracteres.

**Resultado:** el sistema rechazó el dato y mostró el mensaje de validación.

### Prueba 6: Tipo de consulta incorrecto

Se ingresó la opción `9`.

**Resultado:** el sistema rechazó la opción porque solamente acepta las opciones del 1 al 5.

### Prueba 7: Múltiples solicitudes

Se registraron tres solicitudes durante una misma ejecución.

**Resultado:** el sistema permitió registrar las solicitudes y almacenarlas en el archivo JSON.

### Prueba 8: Estadísticas

Se utilizó la opción de estadísticas.

**Resultado:** el sistema mostró las cantidades de solicitudes por estado y prioridad.

## Control de versiones

El proyecto utiliza Git y GitHub para registrar los cambios realizados durante el desarrollo.

Los commits utilizan mensajes descriptivos para identificar las mejoras.

También se utilizaron ramas `feature/` para realizar cambios importantes antes de integrarlos a `main`.

## Repositorio

Repositorio del proyecto:

https://github.com/paredesmurayaridiego-sys/soporte-academico-python.git

## Ejecución

Para ejecutar el programa:

```bash
python main.py
```
