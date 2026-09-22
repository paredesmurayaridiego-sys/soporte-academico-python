import json
from datetime import datetime

ARCHIVO = "solicitudes.json"


def cargar_solicitudes():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_solicitudes(solicitudes):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(solicitudes, archivo, indent=4, ensure_ascii=False)


def validar_codigo(codigo):
    codigo = codigo.strip()

    if codigo == "":
        print("[ERROR] El código no puede estar vacío.")
        return False

    if len(codigo) < 5:
        print("[ERROR] El código debe tener como mínimo 5 caracteres.")
        return False

    if not codigo.isalnum():
        print("[ERROR] El código solo debe contener letras y números.")
        return False

    return True


def validar_nombre(nombre):
    nombre = nombre.strip()

    if nombre == "":
        print("[ERROR] El nombre no puede estar vacío.")
        print("Debe ingresar el nombre completo del estudiante.")
        return False

    if not all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
        print("[ERROR] El nombre solo debe contener letras y espacios.")
        print("No debe ingresar números ni símbolos.")
        return False

    return True


def validar_detalle(detalle):
    if detalle.strip() == "":
        print("[ERROR] El detalle no puede estar vacío.")
        return False

    return True


def validar_consulta(consulta):
    if consulta.strip() == "":
        print("[ERROR] La consulta no puede estar vacía.")
        return False

    return True


def validar_prioridad(prioridad):
    prioridades = ["Alta", "Media", "Baja"]

    if prioridad.capitalize() not in prioridades:
        print("[ERROR] Prioridad inválida.")
        print("Debe ingresar: Alta, Media o Baja.")
        return False

    return True


def mostrar_encabezado():
    print("\n==========================================")
    print("     SISTEMA DE SOPORTE ACADÉMICO")
    print("==========================================")


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
    print("\n========== AYUDA DEL SISTEMA ==========")
    print("1. Registrar solicitud:")
    print("   Permite registrar una nueva atención académica.")
    print("\n2. Buscar solicitud:")
    print("   Permite buscar una solicitud por código o nombre.")
    print("\n3. Actualizar estado:")
    print("   Permite cambiar el estado de una solicitud.")
    print("\n4. Mostrar solicitudes:")
    print("   Permite visualizar las solicitudes registradas.")
    print("\n5. Salir:")
    print("   Permite cerrar el sistema.")
    print("\n6. Mostrar estadísticas:")
    print("   Muestra un resumen de las solicitudes.")
    print("\n7. Ayuda del sistema:")
    print("   Muestra información sobre las opciones disponibles.")
    print("=======================================")


def registrar_solicitud(solicitudes):
    print("\n===== REGISTRAR SOLICITUD =====")

    while True:
        codigo = input("Código del estudiante: ").strip()

        if not validar_codigo(codigo):
            continue

        if any(s["codigo"].lower() == codigo.lower() for s in solicitudes):
            print("[ERROR] Ya existe una solicitud con ese código.")
            continue

        break

    while True:
        nombre = input("Nombre del estudiante: ").strip()

        if validar_nombre(nombre):
            break

    while True:
        consulta = input("Tipo de consulta: ").strip()

        if validar_consulta(consulta):
            break

    while True:
        detalle = input("Detalle de la solicitud: ").strip()

        if validar_detalle(detalle):
            break

    while True:
        prioridad = input("Prioridad (Alta/Media/Baja): ").strip().capitalize()

        if validar_prioridad(prioridad):
            break

    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "consulta": consulta,
        "detalle": detalle,
        "prioridad": prioridad,
        "estado": "Pendiente",
        "fecha": fecha_actual,
        "ultima_actualizacion": fecha_actual
    }

    solicitudes.append(solicitud)
    guardar_solicitudes(solicitudes)

    print("\n[SUCCESS] Solicitud registrada correctamente.")
    print(f"Código: {codigo}")
    print(f"Estado: Pendiente")
    print(f"Fecha: {fecha_actual}")


def buscar_solicitud(solicitudes):
    print("\n===== BUSCAR SOLICITUD =====")

    if not solicitudes:
        print("[INFO] No existen solicitudes registradas.")
        return

    busqueda = input("Ingrese código o nombre: ").strip().lower()

    encontrados = []

    for solicitud in solicitudes:
        if (
            busqueda in solicitud["codigo"].lower()
            or busqueda in solicitud["nombre"].lower()
        ):
            encontrados.append(solicitud)

    if not encontrados:
        print("[INFO] No se encontraron solicitudes.")
        return

    for solicitud in encontrados:
        print("\n--------------------------------")
        print(f"Código: {solicitud['codigo']}")
        print(f"Nombre: {solicitud['nombre']}")
        print(f"Consulta: {solicitud['consulta']}")
        print(f"Detalle: {solicitud['detalle']}")
        print(f"Prioridad: {solicitud['prioridad']}")
        print(f"Estado: {solicitud['estado']}")
        print(f"Fecha: {solicitud.get('fecha', 'No registrada')}")
        print(
            f"Última actualización: "
            f"{solicitud.get('ultima_actualizacion', 'No registrada')}"
        )
        print("--------------------------------")


def actualizar_estado(solicitudes):
    print("\n===== ACTUALIZAR ESTADO =====")

    if not solicitudes:
        print("[INFO] No existen solicitudes registradas.")
        return

    codigo = input("Ingrese el código de la solicitud: ").strip()

    solicitud_encontrada = None

    for solicitud in solicitudes:
        if solicitud["codigo"].lower() == codigo.lower():
            solicitud_encontrada = solicitud
            break

    if solicitud_encontrada is None:
        print("[ERROR] No se encontró una solicitud con ese código.")
        return

    print(f"\nSolicitud encontrada: {solicitud_encontrada['nombre']}")
    print(f"Estado actual: {solicitud_encontrada['estado']}")

    print("\nEstados disponibles:")
    print("1. Pendiente")
    print("2. En proceso")
    print("3. Atendido")

    opcion = input("Seleccione el nuevo estado: ").strip()

    estados = {
        "1": "Pendiente",
        "2": "En proceso",
        "3": "Atendido"
    }

    if opcion not in estados:
        print("[ERROR] Opción de estado inválida.")
        return

    nuevo_estado = estados[opcion]

    if nuevo_estado == solicitud_encontrada["estado"]:
        print("[INFO] La solicitud ya se encuentra en ese estado.")
        return

    solicitud_encontrada["estado"] = nuevo_estado
    solicitud_encontrada["ultima_actualizacion"] = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    guardar_solicitudes(solicitudes)

    print("\n[SUCCESS] Estado actualizado correctamente.")
    print(f"Nuevo estado: {nuevo_estado}")


def mostrar_solicitudes(solicitudes):
    print("\n===== MOSTRAR SOLICITUDES =====")

    if not solicitudes:
        print("[INFO] No existen solicitudes registradas.")
        return

    print("\nFiltros disponibles:")
    print("1. Todas")
    print("2. Pendientes")
    print("3. En proceso")
    print("4. Atendidas")
    print("5. Prioridad Alta")
    print("6. Prioridad Media")
    print("7. Prioridad Baja")

    opcion = input("Seleccione un filtro: ").strip()

    solicitudes_filtradas = []

    for solicitud in solicitudes:
        estado = solicitud.get("estado", "")
        prioridad = solicitud.get("prioridad", "")

        if opcion == "1":
            solicitudes_filtradas.append(solicitud)

        elif opcion == "2" and estado == "Pendiente":
            solicitudes_filtradas.append(solicitud)

        elif opcion == "3" and estado == "En proceso":
            solicitudes_filtradas.append(solicitud)

        elif opcion == "4" and estado in ["Atendido", "Atendida"]:
            solicitudes_filtradas.append(solicitud)

        elif opcion == "5" and prioridad == "Alta":
            solicitudes_filtradas.append(solicitud)

        elif opcion == "6" and prioridad == "Media":
            solicitudes_filtradas.append(solicitud)

        elif opcion == "7" and prioridad == "Baja":
            solicitudes_filtradas.append(solicitud)

    if not solicitudes_filtradas:
        print("[INFO] No existen solicitudes para el filtro seleccionado.")
        return

    print("\n===== RESULTADOS =====")

    for solicitud in solicitudes_filtradas:
        print("\n--------------------------------")
        print(f"Código: {solicitud['codigo']}")
        print(f"Nombre: {solicitud['nombre']}")
        print(f"Consulta: {solicitud['consulta']}")
        print(f"Detalle: {solicitud['detalle']}")
        print(f"Prioridad: {solicitud['prioridad']}")
        print(f"Estado: {solicitud['estado']}")
        print(f"Fecha: {solicitud.get('fecha', 'No registrada')}")
        print(
            f"Última actualización: "
            f"{solicitud.get('ultima_actualizacion', 'No registrada')}"
        )
        print("--------------------------------")


def mostrar_estadisticas(solicitudes):
    print("\n===== ESTADÍSTICAS =====")

    total = len(solicitudes)

    pendientes = 0
    en_proceso = 0
    atendidas = 0

    alta = 0
    media = 0
    baja = 0

    for solicitud in solicitudes:
        estado = solicitud.get("estado", "")
        prioridad = solicitud.get("prioridad", "")

        if estado == "Pendiente":
            pendientes += 1
        elif estado == "En proceso":
            en_proceso += 1
        elif estado in ["Atendido", "Atendida"]:
            atendidas += 1

        if prioridad == "Alta":
            alta += 1
        elif prioridad == "Media":
            media += 1
        elif prioridad == "Baja":
            baja += 1

    print(f"\nTotal de solicitudes: {total}")

    print("\nPor estado:")
    print(f"- Pendientes: {pendientes}")
    print(f"- En proceso: {en_proceso}")
    print(f"- Atendidas: {atendidas}")

    print("\nPor prioridad:")
    print(f"- Alta: {alta}")
    print(f"- Media: {media}")
    print(f"- Baja: {baja}")


def main():
    solicitudes = cargar_solicitudes()

    mostrar_encabezado()

    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            registrar_solicitud(solicitudes)

        elif opcion == "2":
            buscar_solicitud(solicitudes)

        elif opcion == "3":
            actualizar_estado(solicitudes)

        elif opcion == "4":
            mostrar_solicitudes(solicitudes)

        elif opcion == "5":
            confirmar = input(
                "\n¿Está seguro que desea salir? (S/N): "
            ).strip().upper()

            if confirmar == "S":
                print("\nGracias por utilizar el sistema.")
                break
            else:
                print("\nRegresando al menú principal...")

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