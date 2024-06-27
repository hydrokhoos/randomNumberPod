import random
import time
import os


path_semaphore = '/shared/semaphore'
path_data = '/shared/data'

def service_function():
    while True:
        if os.path.exists(path_semaphore):
            print(f'{time.time()}: function start')
            with open(path_data, 'w') as f:
                f.write(str(random.randint(0, 10)))
            time.sleep(2)
            os.remove(path_semaphore)
            print(f'{time.time()}: function complete')
        time.sleep(1)

if __name__ == '__main__':
    print(f'{time.time()}: service ready')
    if os.path.exists(path_semaphore):
        os.remove(path_semaphore)
    service_function()
