import time
import random

def waiting_time():


    target = random.randint(2,4)
    print(f"\nYour target time is {target} seconds")

    input("----Press Enter to begin----")
    start = time.perf_counter()

    input(f"\nPress Enter again after {target} seconds")
    elapsed= time.perf_counter() - start

    print (f"\n Elapsed time is {elapsed :.3f} seconds")

    if elapsed == target:
        print('(Unbeleivable! Perfect timing)')
    elif elapsed < target:
        print(f"{target - elapsed :.3f} seconds too fast")
    elif elapsed > target:
        print(f"{elapsed - target :.3f} seconds too slow")

waiting_time()


