import random
import timeit
from quicksort import quicksort
from insertionsort import insertionsort
from heapsort import heapsort
from mergesort import mergesort

def main():
    len = 100
    table = []
    for i in range(len):
        table.append(random.randint(0, 100))
    print("Not sorted : ", str(table))
    # exectim = timeit.timeit(lambda: print("quick sorted : " + str(quicksort(table))), number=1)
    # print("execution time for quicksort = " + str(exectim))
    # exectim = timeit.timeit(lambda: print("heap sorted : " + str(heapsort(table))), number=1)
    # print("execution time for heap = " + str(exectim))
    # exectim = timeit.timeit(lambda: print("insertion sorted : " + str(insertionsort(table))), number=1)
    # print("execution time for insertion = " + str(exectim))
    exectim = timeit.timeit(lambda: print("merge sorted : " + str(mergesort(table))), number=1)
    print("execution time for merge = " + str(exectim))


if __name__ == "__main__":
    main()
