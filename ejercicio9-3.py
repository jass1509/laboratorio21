from multiprocessing import Process
import time, random

def consulta():
    t = random.randint(1,5)
    time.sleep(t)
    print(f"Proceso terminó en {t}s")

procesos = [Process(target=consulta) for _ in range(3)]
for p in procesos: p.start()
for p in procesos: p.join()
