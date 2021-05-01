# Dummy service, which prints timestamp each second

from time import time, sleep

if __name__ == '__main__':
    while True:
        print(f"[Service] {time()}")
        sleep(1)
