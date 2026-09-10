import time 
from collections import deque 
processes = [["P1", 5],["P2", 3],["P3", 7],["P4", 10],["P5", 2]]
quantum = 2
queue = deque (processes)

print("Simulacao Roun Robin\n")
while queue:
process = queue.popleft()
name, remaining = process

print(f"Executando{name} por {quantum} segundos")
time.sleep(1)
remaining -= quantum

if remaining > 0:
 print(f"{name} nao terminou.restante: {remaining}")
queue.append([name, remaining])
else:
 print(f"{name} terminou")

print(f"Fila:", list(queue))
print("-" * 30)

print("Todos os processos terminaram")

