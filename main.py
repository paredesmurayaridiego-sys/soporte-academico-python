# Sistema de Orientación y Registro de Atenciones
# Soporte Académico
# Fundamentos de Programación

import json
import os
from datetime import datetime


ARCHIVO_JSON = "solicitudes.json"


# ==========================================================
# 1. CARGAR Y GUARDAR SOLICITUDES
# ==========================================================

def cargar_solicitudes():
    if not os.path.exists(ARCHIVO_JSON):
        return []

    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []


def guardar_solicitudes(solicitudes):
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(
            solicitudes,
            archivo,
            indent=4,
            ensure_ascii=False
        )


# ==========================================================
# 2. FUNCIONES DE VALIDACIÓN
# ==========================================================

def validar_codigo(codigo):
    codigo = codigo.strip()

    if codigo == "":
        print("\n[ERROR] El código no puede estar vacío.")
        print("Debe ingresar un código de estudiante.")
        return False

    if len(codigo) < 5:
        print("\n[ERROR] El código debe tener como mínimo 5 caracteres.")
        print("Ejemplo: N00530756")
        return False

    if not codigo.isalnum():
        print("\n[ERROR] El código solo debe contener letras y números.")
        print("No debe ingresar espacios ni símbolos.")
        return False

    return True


def validar_nombre(nombre):
    nombre = nombre.strip()

    if nombre == "":
        print("\n[ERROR] El nombre no puede estar vacío.")
        print("Debe ingresar el nombre completo del estudiante.")
        return False

    nombre_sin_espacios = nombre.replace(" ", "")

    if not nombre_sin_espacios.isalpha():
        print("\n[ERROR] El nombre solo debe contener letras y espacios.")
        print("No debe ingresar números ni símbolos.")
        return False

    return True


def validar_texto_obligatorio(texto, campo):
    texto = texto.strip()

    if texto == "":
        print(f"\n[ERROR] El {campo} no puede estar vacío.")
        print(f"Debe ingresar información en el campo {campo}.")
        return False

    if len(texto) < 4:
        print(f"\n[ERROR] El {campo} es demasiado corto.")
        print("Debe ingresar al menos 4 caracteres.")
        return False

    return True


def validar_detalle(detalle):
    return validar_texto_obligatorio(
        detalle,
        "detalle de la solicitud"
    )


# ==========================================================
# 3. VALIDACIÓN DEL TIPO DE CONSULTA
# ==========================================================

def validar_consulta(consulta):
    consulta = consulta.strip().lower()

    consultas_validas = [
        "matrícula",
        "matricula",
        "pagos",
        "constancia",
        "plataforma",
        "otro"
    ]

    if consulta == "":
        print("\n[ERROR] La consulta no puede estar vacía.")
        print("Debe indicar el tipo de consulta.")
        return False

    if consulta not in consultas_validas:
        print("\n[ERROR] El tipo de consulta no es válido.")
        print("Opciones permitidas:")
        print("Matrícula")
        print("Pagos")
        print("Constancia")
        print("Plataforma")
        print("Otro")
        return False

    return True


def normalizar_consulta(consulta):
    consulta = consulta.strip().lower()

    if consulta == "matricula":
        return "Matrícula"

    if consulta == "matrícula":
        return "Matrícula"

    if consulta == "pagos":
        return "Pagos"

    if consulta == "constancia":
        return "Constancia"

    if consulta == "plataforma":
        return "Plataforma"

    if consulta == "otro":
        return "Otro"

    return consulta.capitalize()


# ==========================================================
# 4. ASIGNACIÓN DE PRIORIDAD
# ==========================================================

def calcular_prioridad(consulta):
    """
    Función con retorno que asigna una prioridad
    dependiendo del tipo de consulta.
    """

    consulta = normalizar_consulta(consulta)

    if consulta == "Pagos":
        return "Alta"

    if consulta == "Matrícula":
        return "Alta"

    if consulta == "Plataforma":
        return "Media"

    if consulta == "Constancia":
        return "Baja"

    return "Baja"


# ==========================================================
# 5. ENCABEZADO Y MENÚ
# ==========================================================

def mostrar_encabezado():
    print("\n========================================")
    print("     SISTEMA DE SOPORTE ACADÉMICO")
    print("========================================")
    print(" Sistema de Orientación y Registro")
    print("          de Atenciones")
    print("========================================")


def mostrar_menu():
    print("\n===== SOPORTE ACADÉMICO =====")
    print("1. Registrar solicitud")
    print("2. Buscar solicitud")
    print("3. Actualizar estado")
    print("4. Mostrar solicitudes")
    print("5. Salir")
    print("6. Mostrar estadísticas")
    print("7. Ayuda del sistema")


def mostrar_ayuda():
    print("\n===== AYUDA DEL SISTEMA =====")
    print("1. Registrar solicitud:")
    print("   Permite registrar una nueva atención.")

    print("\n2. Buscar solicitud:")
    print("   Permite buscar por código o nombre.")

    print("\n3. Actualizar estado:")
    print("   Permite cambiar el estado de una solicitud.")

    print("\n4. Mostrar solicitudes:")
    print("   Permite visualizar solicitudes utilizando filtros.")

    print("\n5. Salir:")
    print("   Finaliza la ejecución del sistema.")

    print("\n6. Estadísticas:")
    print("   Muestra cantidades de solicitudes por estado y prioridad.")

    print("\n7. Ayuda:")
    print("   Muestra información sobre las opciones del sistema.")

    print("\nTipos de consulta permitidos:")
    print("- Matrícula")
    print("- Pagos")
    print("- Constancia")
    print("- Plataforma")
    print("- Otro")


# ==========================================================
# 6. MOSTRAR RESUMEN DE UNA SOLICITUD
# ==========================================================

def mostrar_resumen(solicitud):
    print("\n===== RESUMEN DE LA SOLICITUD =====")
    print("Nombre:", solicitud["nombre"])
    print("Código:", solicitud["codigo"])
    print("Consulta:", solicitud["consulta"])
    print("Detalle:", solicitud["detalle"])
    print("Prioridad:", solicitud["prioridad"])
    print("Estado:", solicitud["estado"])

    if "fecha" in solicitud:
        print("Fecha y hora:", solicitud["fecha"])
    else:
        print("Fecha y hora: No registrada")

    if "ultima_actualizacion" in solicitud:
        print(
            "Última actualización:",
            solicitud["ultima_actualizacion"]
        )
    else:
        print("Última actualización: No registrada")


# ==========================================================
# 7. REGISTRAR SOLICITUD
# ==========================================================

def registrar_solicitud(solicitudes):
    print("\n===== REGISTRAR SOLICITUD =====")

    # ------------------------------------------------------
    # Código
    # ------------------------------------------------------

    while True:
        codigo = input(
            "Ingrese el código del estudiante: "
        )

        if validar_codigo(codigo):
            break

    # ------------------------------------------------------
    # Nombre
    # ------------------------------------------------------

    while True:
        nombre = input(
            "Ingrese el nombre del estudiante: "
        )

        if validar_nombre(nombre):
            break

    # ------------------------------------------------------
    # Consulta
    # ------------------------------------------------------

    print("\nTipos de consulta disponibles:")
    print("1. Matrícula")
    print("2. Pagos")
    print("3. Constancia")
    print("4. Plataforma")
    print("5. Otro")

    while True:
        opcion_consulta = input(
            "Seleccione el tipo de consulta: "
        )

        opciones = {
            "1": "Matrícula",
            "2": "Pagos",
            "3": "Constancia",
            "4": "Plataforma",
            "5": "Otro"
        }

        if opcion_consulta in opciones:
            consulta = opciones[opcion_consulta]
            break

        print("\n[ERROR] Seleccione una opción válida.")
        print("Ingrese un número del 1 al 5.")

    # ------------------------------------------------------
    # Detalle
    # ------------------------------------------------------

    while True:
        detalle = input(
            "Ingrese el detalle de la solicitud: "
        )

        if validar_detalle(detalle):
            break

    # ------------------------------------------------------
    # Verificar código duplicado
    # ------------------------------------------------------

    for solicitud in solicitudes:
        if solicitud["codigo"].lower() == codigo.strip().lower():
            print("\n[ERROR] El código del estudiante ya está registrado.")
            print(
                "No se puede registrar otra solicitud "
                "con el mismo código."
            )
            return

    # ------------------------------------------------------
    # Asignar prioridad automáticamente
    # ------------------------------------------------------

    prioridad = calcular_prioridad(consulta)

    fecha_actual = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    solicitud = {
        "nombre": nombre.strip(),
        "codigo": codigo.strip(),
        "consulta": consulta,
        "detalle": detalle.strip(),
        "prioridad": prioridad,
        "estado": "Pendiente",
        "fecha": fecha_actual,
        "ultima_actualizacion": fecha_actual
    }

    # ------------------------------------------------------
    # Mostrar resumen
    # ------------------------------------------------------

    mostrar_resumen(solicitud)

    # ------------------------------------------------------
    # Confirmación
    # ------------------------------------------------------

    confirmacion = input(
        "\n¿Desea registrar esta solicitud? (S/N): "
    )

    if confirmacion.strip().lower() == "s":

        solicitudes.append(solicitud)

        guardar_solicitudes(solicitudes)

        print("\nSolicitud registrada correctamente.")
        print(
            "La prioridad fue asignada automáticamente:",
            prioridad
        )

    elif confirmacion.strip().lower() == "n":

        print("\nRegistro cancelado.")

    else:

        print("\n[ERROR] Opción inválida.")
        print("La solicitud no fue registrada.")


# ==========================================================
# 8. BUSCAR SOLICITUD
# ==========================================================

def buscar_solicitud(solicitudes):
    print("\n===== BUSCAR SOLICITUD =====")
    print("1. Buscar por código")
    print("2. Buscar por nombre")

    opcion = input("\nSeleccione una opción: ")

    # ------------------------------------------------------
    # Buscar por código
    # ------------------------------------------------------

    if opcion == "1":

        codigo = input(
            "Ingrese el código del estudiante: "
        )

        if not validar_codigo(codigo):
            return

        encontrado = False

        for solicitud in solicitudes:

            if solicitud["codigo"].lower() == codigo.strip().lower():

                mostrar_resumen(solicitud)

                encontrado = True
                break

        if not encontrado:

            print(
                "\nNo se encontró ninguna solicitud "
                "con ese código."
            )

    # ------------------------------------------------------
    # Buscar por nombre
    # ------------------------------------------------------

    elif opcion == "2":

        nombre = input(
            "Ingrese el nombre del estudiante: "
        )

        if nombre.strip() == "":
            print(
                "\n[ERROR] El nombre de búsqueda "
                "no puede estar vacío."
            )
            print(
                "Debe ingresar un nombre para "
                "realizar la búsqueda."
            )
            return

        encontrado = False

        for solicitud in solicitudes:

            if nombre.strip().lower() in solicitud["nombre"].lower():

                mostrar_resumen(solicitud)

                print("------------------------------")

                encontrado = True

        if not encontrado:

            print(
                "\nNo se encontró ninguna solicitud "
                "con ese nombre."
            )

    else:

        print("\nOpción inválida.")


# ==========================================================
# 9. ACTUALIZAR ESTADO
# ==========================================================

def actualizar_estado(solicitudes):
    print("\n===== ACTUALIZAR ESTADO =====")

    codigo = input(
        "Ingrese el código del estudiante: "
    )

    if not validar_codigo(codigo):
        return

    for solicitud in solicitudes:

        if solicitud["codigo"].lower() == codigo.strip().lower():

            print("\nEstados disponibles:")
            print("1. Pendiente")
            print("2. En proceso")
            print("3. Atendido")

            opcion = input(
                "Seleccione el nuevo estado: "
            )

            if opcion == "1":
                nuevo_estado = "Pendiente"

            elif opcion == "2":
                nuevo_estado = "En proceso"

            elif opcion == "3":
                nuevo_estado = "Atendido"

            else:
                print("\nOpción inválida.")
                return

            if solicitud["estado"] == nuevo_estado:
                print(
                    "\nLa solicitud ya se encuentra "
                    "en este estado."
                )
                return

            solicitud["estado"] = nuevo_estado

            fecha_actualizacion = datetime.now().strftime(
                "%d/%m/%Y %H:%M"
            )

            solicitud["ultima_actualizacion"] = (
                fecha_actualizacion
            )

            guardar_solicitudes(solicitudes)

            print("\nEstado actualizado correctamente.")
            print("Nuevo estado:", nuevo_estado)
            print(
                "Última actualización:",
                fecha_actualizacion
            )

            return

    print(
        "\nNo se encontró ninguna solicitud "
        "con ese código."
    )


# ==========================================================
# 10. MOSTRAR SOLICITUDES
# ==========================================================

def mostrar_solicitudes(solicitudes):
    print("\n===== MOSTRAR SOLICITUDES =====")

    print("1. Pendientes")
    print("2. En proceso")
    print("3. Atendidas")
    print("4. Prioridad Alta")
    print("5. Prioridad Media")
    print("6. Prioridad Baja")
    print("7. Todas")

    opcion = input(
        "\nSeleccione una opción: "
    )

    opciones_validas = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7"
    ]

    if opcion not in opciones_validas:

        print("\nOpción inválida.")
        return

    if len(solicitudes) == 0:

        print("\nNo hay solicitudes registradas.")
        return

    if opcion == "1":

        tipo_filtro = "estado"
        filtro = "pendiente"
        titulo = "SOLICITUDES PENDIENTES"

    elif opcion == "2":

        tipo_filtro = "estado"
        filtro = "en proceso"
        titulo = "SOLICITUDES EN PROCESO"

    elif opcion == "3":

        tipo_filtro = "estado"
        filtro = "atendido"
        titulo = "SOLICITUDES ATENDIDAS"

    elif opcion == "4":

        tipo_filtro = "prioridad"
        filtro = "alta"
        titulo = "SOLICITUDES DE PRIORIDAD ALTA"

    elif opcion == "5":

        tipo_filtro = "prioridad"
        filtro = "media"
        titulo = "SOLICITUDES DE PRIORIDAD MEDIA"

    elif opcion == "6":

        tipo_filtro = "prioridad"
        filtro = "baja"
        titulo = "SOLICITUDES DE PRIORIDAD BAJA"

    else:

        tipo_filtro = "todas"
        filtro = "todas"
        titulo = "TODAS LAS SOLICITUDES"

    # ------------------------------------------------------
    # Contadores
    # ------------------------------------------------------

    pendientes = 0
    en_proceso = 0
    atendidas = 0

    for solicitud in solicitudes:

        estado = solicitud["estado"].strip().lower()

        if estado == "pendiente":
            pendientes += 1

        elif estado == "en proceso":
            en_proceso += 1

        elif estado == "atendido" or estado == "atendida":
            atendidas += 1

    print("\n===== RESUMEN DE SOLICITUDES =====")
    print(
        "Total de solicitudes:",
        len(solicitudes)
    )
    print("Pendientes:", pendientes)
    print("En proceso:", en_proceso)
    print("Atendidas:", atendidas)

    print("\n=====", titulo, "=====")

    contador = 0

    for solicitud in solicitudes:

        estado = solicitud["estado"].strip().lower()
        prioridad = solicitud["prioridad"].strip().lower()

        if tipo_filtro == "estado":

            if filtro == "atendido":

                if (
                    estado != "atendido"
                    and estado != "atendida"
                ):
                    continue

            elif estado != filtro:

                continue

        elif tipo_filtro == "prioridad":

            if prioridad != filtro:

                continue

        contador += 1

        print("\nSolicitud N.º", contador)
        print("------------------------------")

        print("Nombre:", solicitud["nombre"])
        print("Código:", solicitud["codigo"])
        print("Consulta:", solicitud["consulta"])
        print("Detalle:", solicitud["detalle"])
        print(
            "Prioridad:",
            solicitud["prioridad"]
        )
        print("Estado:", solicitud["estado"])

        if "fecha" in solicitud:
            print(
                "Fecha y hora:",
                solicitud["fecha"]
            )
        else:
            print(
                "Fecha y hora: No registrada"
            )

        if "ultima_actualizacion" in solicitud:
            print(
                "Última actualización:",
                solicitud["ultima_actualizacion"]
            )
        else:
            print(
                "Última actualización: "
                "No registrada"
            )

        print("------------------------------")

    if contador == 0:

        print(
            "\nNo hay solicitudes que coincidan "
            "con ese filtro."
        )


# ==========================================================
# 11. ESTADÍSTICAS
# ==========================================================

def mostrar_estadisticas(solicitudes):

    print("\n===== ESTADÍSTICAS DEL SISTEMA =====")

    total = len(solicitudes)

    pendientes = 0
    en_proceso = 0
    atendidas = 0

    prioridad_alta = 0
    prioridad_media = 0
    prioridad_baja = 0

    for solicitud in solicitudes:

        estado = solicitud["estado"].strip().lower()
        prioridad = solicitud["prioridad"].strip().lower()

        if estado == "pendiente":
            pendientes += 1

        elif estado == "en proceso":
            en_proceso += 1

        elif estado == "atendido" or estado == "atendida":
            atendidas += 1

        if prioridad == "alta":
            prioridad_alta += 1

        elif prioridad == "media":
            prioridad_media += 1

        elif prioridad == "baja":
            prioridad_baja += 1

    print("\n----- POR ESTADO -----")
    print("Total:", total)
    print("Pendientes:", pendientes)
    print("En proceso:", en_proceso)
    print("Atendidas:", atendidas)

    print("\n----- POR PRIORIDAD -----")
    print("Alta:", prioridad_alta)
    print("Media:", prioridad_media)
    print("Baja:", prioridad_baja)


# ==========================================================
# 12. PROGRAMA PRINCIPAL
# ==========================================================

def main():

    solicitudes = cargar_solicitudes()

    mostrar_encabezado()

    while True:

        mostrar_menu()

        opcion = input(
            "\nSeleccione una opción: "
        )

        if opcion == "1":

            registrar_solicitud(solicitudes)

        elif opcion == "2":

            buscar_solicitud(solicitudes)

        elif opcion == "3":

            actualizar_estado(solicitudes)

        elif opcion == "4":

            mostrar_solicitudes(solicitudes)

        elif opcion == "5":

            print(
                "\nGracias por utilizar "
                "el Sistema de Soporte Académico."
            )
            break

        elif opcion == "6":

            mostrar_estadisticas(solicitudes)

        elif opcion == "7":

            mostrar_ayuda()

        else:

            print(
                "\nOpción inválida. "
                "Intente nuevamente."
            )


# ==========================================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":
    main()

