import random
import timeit
from quicksort import quicksort
from insertionsort import insertionsort
from heapsort import heapsort

def main():
    len = 10
    table = []
    for i in range(len):
        table.append(random.randint(0, 1000000))
    print("Not sorted : ", str(table))
    heapsort(table)
    # exectim = timeit.timeit(lambda: print("sorted : " + str(quicksort(table))), number=1)
    # print("execution time for quicksort = " + str(exectim))
    # exectim = timeit.timeit(lambda: print("sorted : " + str(insertionsort(table))), number=1)
    # print("execution time for insertion = " + str(exectim))


if __name__ == "__main__":
    main()
