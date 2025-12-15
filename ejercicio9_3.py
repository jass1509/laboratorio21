from multiprocessing import Process
import time
import random

def consulta(id_proceso):
    t = random.randint(1, 5)
    time.sleep(t)
    print(f"Proceso {id_proceso} terminó en {t}s")

if __name__ == "__main__":
    procesos = []

    for i in range(3):
        p = Process(target=consulta, args=(i,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()
