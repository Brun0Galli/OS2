def round_robin(processes, quantum):
    n = len(processes)
    remaining_burst_time = [min(process[1], 15) for process in processes]  # Limitar la ráfaga a 15
    arrival_time = [process[2] for process in processes]  # Tiempos de llegada
    completion_times = [0] * n
    wait_times = [0] * n
    t = 0  # Tiempo actual
    process_names = [process[0] for process in processes]  # Lista de nombres de procesos

    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if arrival_time[i] <= t:  # Verificar si el proceso ha llegado
                    if remaining_burst_time[i] > quantum:
                        t += quantum
                        remaining_burst_time[i] -= quantum
                    else:
                        t += remaining_burst_time[i]
                        wait_times[i] = t - arrival_time[i] - remaining_burst_time[i]  # Calcular tiempo de espera
                        remaining_burst_time[i] = 0
                        completion_times[i] = t
        if done:
            break

    return sum(completion_times) / n, wait_times, process_names


def first_come_first_served(processes):
    time = 0
    completion_times = []
    wait_times = []
    process_names = []

    for process in sorted(processes, key=lambda x: x[2]):  # Ordenar por tiempo de llegada
        time = max(time, process[2])  # Actualizar el tiempo si el proceso llega más tarde
        wait_time = max(0, time - process[2])  # Calcular tiempo de espera
        wait_times.append(wait_time)
        completion_times.append(time + min(process[1], 15))  # Limitar la ráfaga a 15
        process_names.append(process[0])
        time += min(process[1], 15)  # Avanzar en el tiempo

    return sum(completion_times) / len(completion_times), wait_times, process_names



def shortest_job_first(processes):
    processes.sort(key=lambda x: (x[2], x[1]))  # Ordenar por tiempo de llegada y ráfaga
    time = 0
    completion_times = []
    wait_times = []
    process_names = []
    for process in processes:
        time = max(time, process[2])  # Actualizar el tiempo si el proceso llega más tarde
        wait_time = max(0, time - process[2])
        wait_times.append(wait_time)
        completion_times.append(time + min(process[1], 15))
        process_names.append(process[0])
        time += min(process[1], 15)
    return sum(completion_times) / len(completion_times), wait_times, process_names



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
                            burst_time = int(
                                input("Ingrese el tiempo de ráfaga (1 - 15) para el proceso {}: ".format(process_name)))
                            if burst_time < 1 or burst_time > 15:
                                print("Tiempo de ráfaga inválido. Debe estar entre 1 y 15.")
                                continue
                            while True:
                                wait_time = int(input(
                                    "Ingrese el tiempo de llegada (0 - 15) para el proceso {}: ".format(process_name)))
                                if wait_time < 0 or wait_time > 15:
                                    print("Tiempo de llegada inválido. Debe estar entre 0 y 15.")
                                    continue
                                else:
                                    processes.append((process_name, burst_time, wait_time))
                                    break
                            break

                    print("El tiempo promedio de completación es: ", round_robin(processes, quantum))
                    break  # Sale del bucle de procesos

                break  # Sale del bucle de quantum
            return True

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
                    while True:
                        burst_time = int(
                            input("Ingrese el tiempo de ráfaga (1 - 15) para el proceso {}: ".format(process_name)))
                        if burst_time < 1 or burst_time > 15:
                            print("Tiempo de ráfaga inválido. Debe estar entre 1 y 15.")
                            continue
                        while True:
                            wait_time = int(input(
                                "Ingrese el tiempo de llegada (0 - 15) para el proceso {}: ".format(process_name)))
                            if wait_time < 0 or wait_time > 15:
                                print("Tiempo de llegada inválido. Debe estar entre 0 y 15.")
                                continue
                            else:
                                processes.append((process_name, burst_time, wait_time))
                                break
                        break

                print("El tiempo promedio de completación es: ", first_come_first_served(processes))
                break
            return True

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
                    while True:
                        burst_time = int(
                            input("Ingrese el tiempo de ráfaga (1 - 15) para el proceso {}: ".format(process_name)))
                        if burst_time < 1 or burst_time > 15:
                            print("Tiempo de ráfaga inválido. Debe estar entre 1 y 15.")
                            continue
                        while True:
                            wait_time = int(input("Ingrese el tiempo de llegada (0 - 15) para el proceso {}: ".format(process_name)))
                            if wait_time < 0 or wait_time > 15:
                                print("Tiempo de llegada inválido. Debe estar entre 0 y 15.")
                                continue
                            else:
                                processes.append((process_name, burst_time, wait_time))
                                break
                        break

                print("El tiempo promedio de completación es: ", shortest_job_first(processes))
                break

            return True

        # Terminar programa
        return True


valido = True
while valido :
    os.system('cls')
    valido =  menu()
    input("Presione enter para continuar...")
