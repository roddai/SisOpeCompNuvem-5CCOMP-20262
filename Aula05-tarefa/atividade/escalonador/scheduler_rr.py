import time
from collections import deque

# processos (nome, tempo de execução)
processes = [
    ["P1", 5],
    ["P2", 3],
    ["P3", 7]
]

quantum = 2

queue = deque(processes)

print("Simulação Round Robin\n")

while queue:
    process = queue.popleft()
    name, remaining = process

    print(f"Executando {name} por {quantum} segundos")

    time.sleep(1)

    remaining -= quantum

    if remaining > 0:
        print(f"{name} não terminou. Restante: {remaining}")
        queue.append([name, remaining])
    else:
        print(f"{name} terminou")

    print("Fila:", list(queue))
    print("-" * 30)

print("Todos os processos terminaram")
