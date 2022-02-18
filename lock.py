"""
Lock

Alumna:Natalia Garcia
"""
from multiprocessing import Process, Lock
from multiprocessing import current_process
from multiprocessing import Value, Array

N=8
    
def task(l, common, tid):
    for i in range (100):
        l.acquire()
        try:
            print(f'{tid}-{i}:Critical Section')
            v= common.value +1
            print(f'{tid}-{i}:Inside critical Section')
            common.value = v
            print(f'{tid}-{i}:End of critical Section')
        finally:
            l.release()
    
def main():
    lock = Lock()
    lp = []
    common = Value('i', 0)
    for tid in range(N):
        lp.append(Process(target = task, args = (lock,common, tid)))
    print(f"Valor incial del contador {common.value}")
    for p in lp:
        p.start()
        
    for p in lp:
        p.join()
    
    print(f"Valor final del contador {common.value}")
    print("fin")
    
if __name__ == "__main__":
    main()