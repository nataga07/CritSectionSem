# -*- coding: utf-8 -*-
"""
Lock

Alumna:Natalia Garcia
"""
from multiprocessing import Process, Lock
from multiprocessing import current_process
from multiprocessing import Value, Array
import time
N=8
   
def task(lock, common, tid):
    for i in range (100):
        print(f'{tid}-{i}:Non Critical Section')
        time.sleep(0.1)
        print(f'{tid}-{i}:End of non Critical Section')        
        lock.acquire()
        try:
            print(f'{tid}-{i}:Critical Section')
            v= common.value +1
            time.sleep(0.1)
            print(f'{tid}-{i}:Inside critical Section')
            common.value = v
            print(f'{tid}-{i}:End of critical Section')
        finally:
            lock.release()
            pass
   
def main():
    lock = Lock()
    lp = []
    common = Value('i', 0)
    for tid in range(N):
        lp.append(Process(target = task,
                          args = (lock, common, tid)))
       
    print(f"Valor incial del contador {common.value}")
   
    for p in lp:
        p.start()
       
    for p in lp:
        p.join()
   
    print(f"Valor final del contador {common.value}")
    print("fin")
   
if __name__ == "__main__":
    main()

