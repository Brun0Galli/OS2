
def round_robin(processes, quantum):

    n = len(processes)
    remaining_burst_time = [process[1] for process in processes]
    completion_times = [0] * n
    t = 0  # tiempo actual
    process_names = [process[0] for process in processes]  # Lista de nombres de procesos
    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > quantum:
                    t += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    t += remaining_burst_time[i]
                    remaining_burst_time[i] = 0
                    completion_times[i] = t
        if done:
            break
    return sum(completion_times) / n, process_names


def first_come_first_served(processes):
    time = 0
    completion_times = []
    process_names = []
    for process in processes:
        completion_times.append(time + process[1])
        process_names.append(process[0])
        time += process[1]
    return sum(completion_times) / len(completion_times), process_names


def shortest_job_first(processes):
    processes.sort(key=lambda x: x[1])
    time = 0
    completion_times = []
    process_names = []
    for process in processes:
        completion_times.append(time + process[1])
        process_names.append(process[0])
        time += process[1]
    return sum(completion_times) / len(completion_times), process_names


def menu():
    print("Planification Algorithms")
    print("1. Round Robin")
    print("2. First Come First Served")
    print("3. Shortest Job First")
    print("4. Salir")
    opc = int(input("Ingrese una opción: "))
    match opc:
        case 1:
            print("Entering Round Robin...")
            cant_procesos = int(input("Cuantos procesos desea ingresar: "))
            quantum = int(input("Ingrese el quantum: "))
            processes = []
            for i in range(cant_procesos):
                process_name = input("Ingrese el nombre del proceso: ")
                burst_time = int(input("Ingrese el tiempo de ráfaga: "))
                processes.append((process_name, burst_time))
            print("El tiempo promedio de completación es: ", round_robin(processes, quantum))

        case 2:
            print("Entering First Come First Served...")
            cant_procesos = int(input("Cuantos procesos desea ingresar: "))
            processes = []
            for i in range(cant_procesos):
                process_name = input("Ingrese el nombre del proceso: ")
                burst_time = int(input("Ingrese el tiempo de ráfaga: "))
                processes.append((process_name, burst_time))
            print("El tiempo promedio de completación es: ", first_come_first_served(processes))

        case 3:
            print("Entering Shortest Job First...")
            cant_procesos = int(input("Cuantos procesos desea ingresar: "))
            processes = []
            for i in range(cant_procesos):
                process_name = input("Ingrese el nombre del proceso: ")
                burst_time = int(input("Ingrese el tiempo de ráfaga: "))
                processes.append((process_name, burst_time))
            print("El tiempo promedio de completación es: ", shortest_job_first(processes))

        case 4:
            print("Saliendo...")
            return False
valido = True
while valido :
  valido =  menu()