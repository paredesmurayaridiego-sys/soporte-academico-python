# Sistema de Orientación y Registro de Atenciones
# Soporte Académico

import json
import os
from datetime import datetime


ARCHIVO_JSON = "solicitudes.json"


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
        json.dump(solicitudes, archivo, indent=4, ensure_ascii=False)


def validar_codigo(codigo):
    codigo = codigo.strip()

    if codigo == "":
        print("[ERROR] El código no puede estar vacío.")
        print("Debe ingresar un código de estudiante.")
        return False

    if len(codigo) < 5:
        print("[ERROR] El código debe tener como mínimo 5 caracteres.")
        print("Ejemplo: N00530756")
        return False

    if not codigo.isalnum():
        print("[ERROR] El código solo debe contener letras y números.")
        print("No debe ingresar espacios ni símbolos.")
        return False

    return True


def validar_nombre(nombre):
    nombre = nombre.strip()

    if nombre == "":
        print("[ERROR] El nombre no puede estar vacío.")
        print("Debe ingresar el nombre completo del estudiante.")
        return False

    nombre_sin_espacios = nombre.replace(" ", "")

    if not nombre_sin_espacios.isalpha():
        print("[ERROR] El nombre solo debe contener letras y espacios.")
        print("No debe ingresar números ni símbolos.")
        return False

    return True


def validar_detalle(detalle):
    detalle = detalle.strip()

    if detalle == "":
        print("[ERROR] El detalle de la solicitud no puede estar vacío.")
        print("Debe explicar brevemente el problema o consulta.")
        return False

    if len(detalle) < 5:
        print("[ERROR] El detalle es demasiado corto.")
        print("Ingrese al menos 5 caracteres para explicar la solicitud.")
        return False

    return True


def validar_consulta(consulta):
    consulta = consulta.strip()

    if consulta == "":
        print("[ERROR] La consulta no puede estar vacía.")
        print("Debe indicar el tipo de consulta.")
        return False

    if len(consulta) < 4:
        print("[ERROR] El tipo de consulta es demasiado corto.")
        print("Ingrese al menos 4 caracteres.")
        return False

    return True


def validar_prioridad(prioridad):
    prioridad = prioridad.strip()

    if prioridad == "":
        print("[ERROR] La prioridad no puede estar vacía.")
        print("Debe ingresar Alta, Media o Baja.")
        return False

    prioridades = ["Alta", "Media", "Baja"]

    if prioridad.capitalize() not in prioridades:
        print("[ERROR] La prioridad ingresada no es válida.")
        print("Solo se permite: Alta, Media o Baja.")
        return False

    return True


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
    print("   Permite registrar una nueva atención académica.")

    print("\n2. Buscar solicitud:")
    print("   Permite buscar solicitudes por código o nombre.")

    print("\n3. Actualizar estado:")
    print("   Permite cambiar el estado de una solicitud.")

    print("\n4. Mostrar solicitudes:")
    print("   Permite visualizar solicitudes según diferentes filtros.")

    print("\n5. Salir:")
    print("   Permite cerrar el sistema.")

    print("\n6. Mostrar estadísticas:")
    print("   Muestra un resumen de las solicitudes registradas.")

    print("\n7. Ayuda del sistema:")
    print("   Muestra información sobre las opciones disponibles.")


def registrar_solicitud(solicitudes):
    print("\n===== REGISTRAR SOLICITUD =====")

    while True:
        nombre = input("Ingrese el nombre del estudiante: ")

        if validar_nombre(nombre):
            break

    while True:
        codigo = input("Ingrese el código del estudiante: ")

        if validar_codigo(codigo):
            break

    while True:
        consulta = input("Ingrese la consulta: ")

        if validar_consulta(consulta):
            break

    while True:
        detalle = input("Ingrese el detalle de la solicitud: ")

        if validar_detalle(detalle):
            break

    while True:
        prioridad = input("Ingrese la prioridad (Alta/Media/Baja): ")

        if validar_prioridad(prioridad):
            break

    for solicitud in solicitudes:
        if solicitud["codigo"].lower() == codigo.strip().lower():
            print("\nEl código del estudiante ya está registrado.")
            print("No se puede registrar otra solicitud con el mismo código.")
            return

    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")

    solicitud = {
        "nombre": nombre.strip(),
        "codigo": codigo.strip(),
        "consulta": consulta.strip(),
        "detalle": detalle.strip(),
        "prioridad": prioridad.strip().capitalize(),
        "estado": "Pendiente",
        "fecha": fecha_actual,
        "ultima_actualizacion": fecha_actual
    }

    print("\n===== CONFIRMAR SOLICITUD =====")
    print("Nombre:", solicitud["nombre"])
    print("Código:", solicitud["codigo"])
    print("Consulta:", solicitud["consulta"])
    print("Detalle:", solicitud["detalle"])
    print("Prioridad:", solicitud["prioridad"])
    print("Estado:", solicitud["estado"])
    print("Fecha y hora:", solicitud["fecha"])
    print("Última actualización:", solicitud["ultima_actualizacion"])

    confirmacion = input("\n¿Desea registrar esta solicitud? (S/N): ")

    if confirmacion.strip().lower() == "s":
        solicitudes.append(solicitud)
        guardar_solicitudes(solicitudes)

        print("\n[SUCCESS] Solicitud registrada correctamente.")
        print("Código:", solicitud["codigo"])
        print("Estado:", solicitud["estado"])
        print("Fecha:", solicitud["fecha"])

    elif confirmacion.strip().lower() == "n":
        print("\nRegistro cancelado.")

    else:
        print("\nOpción inválida.")
        print("La solicitud no fue registrada.")


def buscar_solicitud(solicitudes):
    print("\n===== BUSCAR SOLICITUD =====")
    print("1. Buscar por código")
    print("2. Buscar por nombre")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        codigo = input("Ingrese el código del estudiante: ")

        if codigo.strip() == "":
            print("\n[ERROR] El código de búsqueda no puede estar vacío.")
            print("Debe ingresar un código para realizar la búsqueda.")
            return

        if not validar_codigo(codigo):
            return

        encontrado = False

        for solicitud in solicitudes:

            if solicitud["codigo"].lower() == codigo.strip().lower():

                print("\n===== SOLICITUD ENCONTRADA =====")
                print("Nombre:", solicitud["nombre"])
                print("Código:", solicitud["codigo"])
                print("Consulta:", solicitud["consulta"])
                print("Detalle:", solicitud["detalle"])
                print("Prioridad:", solicitud["prioridad"].strip().capitalize())
                print("Estado:", solicitud["estado"])

                if "fecha" in solicitud:
                    print("Fecha y hora:", solicitud["fecha"])
                else:
                    print("Fecha y hora: No registrada")

                if "ultima_actualizacion" in solicitud:
                    print("Última actualización:", solicitud["ultima_actualizacion"])
                else:
                    print("Última actualización: No registrada")

                encontrado = True
                break

        if not encontrado:
            print("\nNo se encontró ninguna solicitud con ese código.")

    elif opcion == "2":

        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre.strip() == "":
            print("\n[ERROR] El nombre de búsqueda no puede estar vacío.")
            print("Debe ingresar un nombre para realizar la búsqueda.")
            return

        encontrado = False

        for solicitud in solicitudes:

            if nombre.strip().lower() in solicitud["nombre"].lower():

                print("\n===== SOLICITUD ENCONTRADA =====")
                print("Nombre:", solicitud["nombre"])
                print("Código:", solicitud["codigo"])
                print("Consulta:", solicitud["consulta"])
                print("Detalle:", solicitud["detalle"])
                print("Prioridad:", solicitud["prioridad"].strip().capitalize())
                print("Estado:", solicitud["estado"])

                if "fecha" in solicitud:
                    print("Fecha y hora:", solicitud["fecha"])
                else:
                    print("Fecha y hora: No registrada")

                if "ultima_actualizacion" in solicitud:
                    print("Última actualización:", solicitud["ultima_actualizacion"])
                else:
                    print("Última actualización: No registrada")

                print("------------------------------")

                encontrado = True

        if not encontrado:
            print("\nNo se encontró ninguna solicitud con ese nombre.")

    else:
        print("\nOpción inválida.")


def actualizar_estado(solicitudes):
    print("\n===== ACTUALIZAR ESTADO =====")

    codigo = input("Ingrese el código del estudiante: ")

    if codigo.strip() == "":
        print("\nError: el código no puede estar vacío.")
        return

    if not validar_codigo(codigo):
        return

    for solicitud in solicitudes:

        if solicitud["codigo"].lower() == codigo.strip().lower():

            print("\nEstados disponibles:")
            print("1. Pendiente")
            print("2. En proceso")
            print("3. Atendido")

            opcion = input("Seleccione el nuevo estado: ")

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
                print("\nLa solicitud ya se encuentra en este estado.")
                return

            solicitud["estado"] = nuevo_estado

            fecha_actualizacion = datetime.now().strftime("%d/%m/%Y %H:%M")
            solicitud["ultima_actualizacion"] = fecha_actualizacion

            guardar_solicitudes(solicitudes)

            print("\nEstado actualizado correctamente.")
            print("Nuevo estado:", nuevo_estado)
            print("Última actualización:", fecha_actualizacion)

            return

    print("\nNo se encontró ninguna solicitud con ese código.")


def mostrar_solicitudes(solicitudes):
    print("\n===== MOSTRAR SOLICITUDES =====")
    print("1. Pendientes")
    print("2. En proceso")
    print("3. Atendidas")
    print("4. Prioridad Alta")
    print("5. Prioridad Media")
    print("6. Prioridad Baja")
    print("7. Todas")

    opcion = input("\nSeleccione una opción: ")

    if opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
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
    print("Total de solicitudes:", len(solicitudes))
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

                if estado != "atendido" and estado != "atendida":
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
        print("Prioridad:", solicitud["prioridad"].strip().capitalize())
        print("Estado:", solicitud["estado"])

        if "fecha" in solicitud:
            print("Fecha y hora:", solicitud["fecha"])
        else:
            print("Fecha y hora: No registrada")

        if "ultima_actualizacion" in solicitud:
            print("Última actualización:", solicitud["ultima_actualizacion"])
        else:
            print("Última actualización: No registrada")

        print("------------------------------")

    if contador == 0:
        print("\nNo hay solicitudes que coincidan con ese filtro.")


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

    print("\nTotal de solicitudes:", total)

    print("\n--- POR ESTADO ---")
    print("Pendientes:", pendientes)
    print("En proceso:", en_proceso)
    print("Atendidas:", atendidas)

    print("\n--- POR PRIORIDAD ---")
    print("Alta:", prioridad_alta)
    print("Media:", prioridad_media)
    print("Baja:", prioridad_baja)


def main():
    solicitudes = cargar_solicitudes()

    mostrar_encabezado()

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_solicitud(solicitudes)

        elif opcion == "2":
            buscar_solicitud(solicitudes)

        elif opcion == "3":
            actualizar_estado(solicitudes)

        elif opcion == "4":
            mostrar_solicitudes(solicitudes)

        elif opcion == "5":
            print("\nGracias por utilizar el sistema.")
            break

        elif opcion == "6":
            mostrar_estadisticas(solicitudes)

        elif opcion == "7":
            mostrar_ayuda()

        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
