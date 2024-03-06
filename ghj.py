
from collections import deque

def round_robin(procesos, quantum):
    tiempo_actual = 0
    cola_procesos = deque(procesos)
    tiempos_espera = {proceso['nombre']: 0 for proceso in procesos}
    tiempos_ejecucion = {proceso['nombre']: 0 for proceso in procesos}
    while cola_procesos:
        proceso_actual = cola_procesos.popleft()
        print(f"Ejecutando proceso {proceso_actual['nombre']} en el tiempo {tiempo_actual}")
        if proceso_actual['tiempo_restante'] > quantum:
            tiempo_actual += quantum
            proceso_actual['tiempo_restante'] -= quantum
            print(f"Proceso {proceso_actual['nombre']} aún en ejecución. Tiempo restante: {proceso_actual['tiempo_restante']}")
            cola_procesos.append(proceso_actual)
            for proceso in cola_procesos:
                if proceso != proceso_actual:
                    tiempos_espera[proceso['nombre']] += quantum
        else:
            tiempo_actual += proceso_actual['tiempo_restante']
            tiempos_ejecucion[proceso_actual['nombre']] = tiempo_actual
            proceso_actual['tiempo_restante'] = 0
            print(f"Proceso {proceso_actual['nombre']} completado en el tiempo {tiempo_actual}")
            for proceso in cola_procesos:
                tiempos_espera[proceso['nombre']] += tiempo_actual - proceso['tiempo_llegada']

    tiempo_promedio = sum(tiempos_ejecucion.values()) / len(tiempos_ejecucion)
    return tiempo_promedio, tiempos_espera, tiempos_ejecucion


def first_come_first_served(processes):
    time = 0
    completion_times = []
    process_names = []
    for process in processes:
        completion_times.append(time + min(process[1], 15))
        process_names.append(process[0])
        time += min(process[1], 15)
    return sum(completion_times) / len(completion_times), process_names


def shortest_job_first(processes):
    processes.sort(key=lambda x: x[1])
    time = 0
    completion_times = []
    process_names = []
    for process in processes:
        completion_times.append(time + min(process[1], 15))
        process_names.append(process[0])
        time += min(process[1], 15)
    return sum(completion_times) / len(completion_times), process_names


def menu():
    while True:
        print("Planification Algorithms")
        print("1. Round Robin")
        print("2. First Come First Served")
        print("3. Shortest Job First")
        print("4. Salir")
        opc = int(input("Ingrese una opción: "))

        # Validar opciones
        if opc < 1 or opc > 4:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            continue

        if opc == 4:
            print("Saliendo...")
            return False

        # Opción 1: Round Robin
        if opc == 1:
            while True:
                cant_procesos = int(input("Cuantos procesos desea ingresar: "))
                if cant_procesos < 1 or cant_procesos > 5:
                    print("Número de procesos inválido. Debe ser entre 1 y 5.")
                    continue

                while True:
                    quantum = int(input("Ingrese el quantum (2, 3, o 4): "))
                    if quantum not in [2, 3, 4]:
                        print("Quantum inválido. Debe ser 2, 3 o 4.")
                        continue

                    processes = []
                    for i in range(cant_procesos):
                        process_name = input("Ingrese el nombre del proceso: ")
                        while True:
                            burst_time = int(input("Ingrese el tiempo de ráfaga (1 - 15) para el proceso {}: ".format(process_name)))
                            if burst_time < 1 or burst_time > 15:
                                print("Tiempo de ráfaga inválido. Debe estar entre 1 y 15.")
                                continue
                            while True:
                                wait_time = int(input("Ingrese el tiempo de llegada (0 - 15) para el proceso {}: ".format(process_name)))
                                if wait_time < 0 or wait_time > 15:
                                    print("Tiempo de llegada inválido. Debe estar entre 0 y 15.")
                                    continue
                                else:
                                    processes.append({'nombre': process_name, 'tiempo_llegada': wait_time, 'tiempo_restante': burst_time})
                                    break
                            break
                    impresion= round_robin(processes, quantum)
                    print("El tiempo promedio de completación es: ", impresion[0], "Tiempo de espera: ", impresion[1], "Tiempo de ejecución: ", impresion[2])
                    break  # Sale del bucle de procesos

                break  # Sale del bucle de quantum

        # Sale del bucle de cantidad de procesos
        # Sale del bucle de cantidad de procesos

        # Opción 2: First Come First Served
        elif opc == 2:
            while True:
                cant_procesos = int(input("Cuantos procesos desea ingresar: "))
                if cant_procesos < 1 or cant_procesos > 5:
                    print("Número de procesos inválido. Debe ser entre 1 y 5.")
                    continue

                processes = []
                for i in range(cant_procesos):
                    process_name = input("Ingrese el nombre del proceso: ")
                    burst_time = int(input("Ingrese el tiempo de ráfaga (1 - 15): "))
                    processes.append((process_name, burst_time))
                print("El tiempo promedio de completación es: ", first_come_first_served(processes))
                break

        # Opción 3: Shortest Job First
        elif opc == 3:
            while True:
                cant_procesos = int(input("Cuantos procesos desea ingresar: "))
                if cant_procesos < 1 or cant_procesos > 5:
                    print("Número de procesos inválido. Debe ser entre 1 y 5.")
                    continue

                processes = []
                for i in range(cant_procesos):
                    process_name = input("Ingrese el nombre del proceso: ")
                    burst_time = int(input("Ingrese el tiempo de ráfaga (1 - 15): "))
                    processes.append((process_name, burst_time))
                print("El tiempo promedio de completación es: ", shortest_job_first(processes))
                break

        # Terminar programa
        return True


valido = True
while valido:
    valido = menu()