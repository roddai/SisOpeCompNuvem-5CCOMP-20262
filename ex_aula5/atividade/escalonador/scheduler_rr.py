import time
from collections import deque

processes = [
    ["P1", 5],
    ["P2", 3],
    ["P3", 7],
    ["P4", 10],
    ["P5", 2]
]

quantum = 2
queue = deque(processes)

print("--- Simulação Round Robin ---\n")

while queue:
    process = queue.popleft()
    name, remaining = process

    print(f"Executando {name} por {quantum} segundos")
    time.sleep(0.5)

    remaining -= quantum

    if remaining > 0:
        print(f"{name} não terminou. Restante: {remaining}")
        queue.append([name, remaining])
    else:
        print(f"{name} terminou")

    print("Fila:", [p[0] for p in queue])
    print("-" * 30)

print("Todos os processos terminaram")