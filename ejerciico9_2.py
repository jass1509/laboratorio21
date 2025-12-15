import asyncio
import random

async def consulta():
    t = random.randint(1, 5)
    await asyncio.sleep(t)
    print(f"Async terminó en {t}s")

async def main():
    await asyncio.gather(*(consulta() for _ in range(3)))

asyncio.run(main())
