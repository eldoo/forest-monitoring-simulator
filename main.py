from multiprocessing import Process
import generate as gen
import process as proc
import time


def main():
    print("Start sensor metrics processing")
    p1 = Process(target=proc.main)
    p1.start()
    time.sleep(5)
    print("Start sensor metrics generation")
    p2 = Process(target=gen.main)
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
