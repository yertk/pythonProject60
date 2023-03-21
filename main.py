import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")


    await say_after(1,'hello')

    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())