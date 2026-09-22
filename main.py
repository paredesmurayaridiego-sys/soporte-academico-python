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
        return False

    if len(codigo) < 5:
        return False

    if not codigo.isalnum():
        return False

    return True


def validar_nombre(nombre):
    nombre = nombre.strip()

    if nombre == "":
        return False

    nombre_sin_espacios = nombre.replace(" ", "")

    if not nombre_sin_espacios.isalpha():
        return False

    return True


def validar_detalle(detalle):
    return detalle.strip() != ""


def validar_consulta(consulta):
    return consulta.strip() != ""


def validar_prioridad(prioridad):
    prioridades_validas = ["Alta", "Media", "Baja"]
    return prioridad.strip().capitalize() in prioridades_validas


def mostrar_encabezado():
    print("\n")
    print("==============================================")
    print("       SISTEMA DE SOPORTE ACADÉMICO")
    print("==============================================")
    print("    Sistema de Orientación y Registro")
    print("             de Atenciones")
    print("==============================================")


def mostrar_menu():
    print("\n----------------------------------------------")
    print("              MENÚ PRINCIPAL")
    print("----------------------------------------------")
    print("1. Registrar solicitud")
    print("2. Buscar solicitud")
    print("3. Actualizar estado")
    print("4. Mostrar solicitudes")
    print("5. Salir")
    print("6. Mostrar estadísticas")
    print("7. Ayuda del sistema")
    print("----------------------------------------------")


def mostrar_ayuda():
    print("\n==============================================")
    print("              AYUDA DEL SISTEMA")
    print("==============================================")
    print("1. Registrar solicitud")
    print("   Permite ingresar una nueva solicitud")
    print("   de un estudiante.")

    print("\n2. Buscar solicitud")
    print("   Permite buscar una solicitud por")
    print("   código o nombre del estudiante.")

    print("\n3. Actualizar estado")
    print("   Permite cambiar el estado de una")
    print("   solicitud a Pendiente, En proceso")
    print("   o Atendido.")

    print("\n4. Mostrar solicitudes")
    print("   Permite visualizar solicitudes aplicando")
    print("   filtros por estado o prioridad.")

    print("\n5. Salir")
    print("   Permite cerrar el sistema.")

    print("\n6. Mostrar estadísticas")
    print("   Muestra un resumen de las solicitudes")
    print("   registradas por estado y prioridad.")

    print("\n7. Ayuda del sistema")
    print("   Muestra información sobre las opciones")
    print("   disponibles en el sistema.")

    print("\n==============================================")


def registrar_solicitud(solicitudes):
    print("\n==============================================")
    print("           REGISTRAR SOLICITUD")
    print("==============================================")

    nombre = input("Ingrese el nombre del estudiante: ")
    codigo = input("Ingrese el código del estudiante: ")
    consulta = input("Ingrese la consulta: ")
    detalle = input("Ingrese el detalle de la solicitud: ")
    prioridad = input("Ingrese la prioridad (Alta/Media/Baja): ")

    if not validar_nombre(nombre):
        print("\n[ERROR] El nombre no es válido.")
        print("El nombre no puede estar vacío y solo debe contener letras.")
        return

    if not validar_codigo(codigo):
        print("\n[ERROR] El código no es válido.")
        print("El código debe tener al menos 5 caracteres y no contener símbolos.")
        return

    if not validar_consulta(consulta):
        print("\n[ERROR] La consulta no puede estar vacía.")
        return

    if not validar_detalle(detalle):
        print("\n[ERROR] El detalle no puede estar vacío.")
        return

    if not validar_prioridad(prioridad):
        print("\n[ERROR] La prioridad no es válida.")
        print("Debe ser Alta, Media o Baja.")
        return

    for solicitud in solicitudes:
        if solicitud["codigo"].lower() == codigo.strip().lower():
            print("\n[ERROR] El código del estudiante ya está registrado.")
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

    print("\n----------------------------------------------")
    print("             CONFIRMAR SOLICITUD")
    print("----------------------------------------------")
    print("Nombre:", solicitud["nombre"])
    print("Código:", solicitud["codigo"])
    print("Consulta:", solicitud["consulta"])
    print("Detalle:", solicitud["detalle"])
    print("Prioridad:", solicitud["prioridad"])
    print("Estado:", solicitud["estado"])
    print("Fecha y hora:", solicitud["fecha"])
    print("Última actualización:", solicitud["ultima_actualizacion"])
    print("----------------------------------------------")

    confirmacion = input("\n¿Desea registrar esta solicitud? (S/N): ")

    if confirmacion.strip().lower() == "s":
        solicitudes.append(solicitud)
        guardar_solicitudes(solicitudes)

        print("\n[OK] Solicitud registrada correctamente.")

    elif confirmacion.strip().lower() == "n":
        print("\n[INFO] Registro cancelado.")

    else:
        print("\n[ERROR] Opción inválida.")
        print("La solicitud no fue registrada.")


def buscar_solicitud(solicitudes):
    print("\n==============================================")
    print("             BUSCAR SOLICITUD")
    print("==============================================")
    print("1. Buscar por código")
    print("2. Buscar por nombre")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        codigo = input("Ingrese el código del estudiante: ")

        if codigo.strip() == "":
            print("\n[ERROR] El código no puede estar vacío.")
            return

        if not validar_codigo(codigo):
            print("\n[ERROR] El código no es válido.")
            print("El código debe tener al menos 5 caracteres y no contener símbolos.")
            return

        encontrado = False

        for solicitud in solicitudes:

            if solicitud["codigo"].lower() == codigo.strip().lower():

                print("\n----------------------------------------------")
                print("             SOLICITUD ENCONTRADA")
                print("----------------------------------------------")
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

                print("----------------------------------------------")

                encontrado = True
                break

        if not encontrado:
            print("\n[INFO] No se encontró ninguna solicitud con ese código.")

    elif opcion == "2":

        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre.strip() == "":
            print("\n[ERROR] El nombre no puede estar vacío.")
            return

        encontrado = False

        for solicitud in solicitudes:

            if nombre.strip().lower() in solicitud["nombre"].lower():

                print("\n----------------------------------------------")
                print("             SOLICITUD ENCONTRADA")
                print("----------------------------------------------")
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

                print("----------------------------------------------")

                encontrado = True

        if not encontrado:
            print("\n[INFO] No se encontró ninguna solicitud con ese nombre.")

    else:
        print("\n[ERROR] Opción inválida.")


def actualizar_estado(solicitudes):
    print("\n==============================================")
    print("             ACTUALIZAR ESTADO")
    print("==============================================")

    codigo = input("Ingrese el código del estudiante: ")

    if codigo.strip() == "":
        print("\n[ERROR] El código no puede estar vacío.")
        return

    if not validar_codigo(codigo):
        print("\n[ERROR] El código no es válido.")
        print("El código debe tener al menos 5 caracteres y no contener símbolos.")
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
                print("\n[ERROR] Opción inválida.")
                return

            if solicitud["estado"] == nuevo_estado:
                print("\n[INFO] La solicitud ya se encuentra en este estado.")
                return

            solicitud["estado"] = nuevo_estado

            fecha_actualizacion = datetime.now().strftime("%d/%m/%Y %H:%M")
            solicitud["ultima_actualizacion"] = fecha_actualizacion

            guardar_solicitudes(solicitudes)

            print("\n[OK] Estado actualizado correctamente.")
            print("Nuevo estado:", nuevo_estado)
            print("Última actualización:", fecha_actualizacion)

            return

    print("\n[INFO] No se encontró ninguna solicitud con ese código.")


def mostrar_solicitudes(solicitudes):
    print("\n==============================================")
    print("            MOSTRAR SOLICITUDES")
    print("==============================================")
    print("1. Pendientes")
    print("2. En proceso")
    print("3. Atendidas")
    print("4. Prioridad Alta")
    print("5. Prioridad Media")
    print("6. Prioridad Baja")
    print("7. Todas")

    opcion = input("\nSeleccione una opción: ")

    if opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\n[ERROR] Opción inválida.")
        return

    if len(solicitudes) == 0:
        print("\n[INFO] No hay solicitudes registradas.")
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
        print("----------------------------------------------")
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

        print("----------------------------------------------")

    if contador == 0:
        print("\n[INFO] No hay solicitudes que coincidan con ese filtro.")


def mostrar_estadisticas(solicitudes):
    print("\n==============================================")
    print("          ESTADÍSTICAS DEL SISTEMA")
    print("==============================================")

    if len(solicitudes) == 0:
        print("\n[INFO] No hay solicitudes registradas.")
        return

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
    print("Total de solicitudes:", total)
    print("Pendientes:", pendientes)
    print("En proceso:", en_proceso)
    print("Atendidas:", atendidas)

    print("\n----- POR PRIORIDAD -----")
    print("Prioridad Alta:", prioridad_alta)
    print("Prioridad Media:", prioridad_media)
    print("Prioridad Baja:", prioridad_baja)

    print("\n==============================================")
    print("       ESTADÍSTICAS GENERADAS CORRECTAMENTE")
    print("==============================================")


def main():
    solicitudes = cargar_solicitudes()

    mostrar_encabezado()

    print("\n¡Bienvenido al Sistema de Soporte Académico!")
    print("Aquí podrá registrar, consultar y gestionar solicitudes.")

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
            confirmacion = input(
                "\n¿Está seguro de que desea salir? (S/N): "
            )

            if confirmacion.strip().lower() == "s":
                print("\n==============================================")
                print(" Gracias por utilizar el Sistema de Soporte")
                print("             Académico.")
                print("==============================================")
                break

            elif confirmacion.strip().lower() == "n":
                print("\n[INFO] Regresando al menú principal.")

            else:
                print("\n[ERROR] Opción inválida.")
                print("Regresando al menú principal.")

        elif opcion == "6":
            mostrar_estadisticas(solicitudes)

        elif opcion == "7":
            mostrar_ayuda()

        else:
            print("\n[ERROR] Opción inválida.")
            print("Debe ingresar un número del 1 al 7.")
            print("Intente nuevamente.")


if __name__ == "__main__":
    main()
