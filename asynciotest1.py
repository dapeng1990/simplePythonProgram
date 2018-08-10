import threading
import asyncio

@asyncio.coroutine
def hello1():
    print("Hello world! (%s)"%threading.currentThread())
    yield from asyncio.sleep(1)
    print("Hello again! (%s)"%threading.currentThread())

loop1 = asyncio.get_event_loop()
tasks=[hello1(),hello1()]
loop1.run_until_complete(asyncio.wait(tasks))
loop1.close()