import threading, time, random

def consulta():
    t = random.randint(1,5)
    time.sleep(t)
    print(f"Hilo terminó en {t}s")

threads = [threading.Thread(target=consulta) for _ in range(3)]
for t in threads: t.start()
for t in threads: t.join()
