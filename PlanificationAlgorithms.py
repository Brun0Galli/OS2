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
