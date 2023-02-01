import random
import timeit

def quicksort(tab):
    # First: scan table and put every item on the left of pivot if smaller else put it on the right
    # make subTable for left part of table and rerun quicksort on this
    # do the same for right part
    if len(tab) < 2:
        return tab
    leftSide = []
    rightSide = []
    equal = []
    pivot = tab[int(len(tab)/2)]
    for item in tab:
        if item != pivot:
            if item < pivot:
                leftSide.append(item)
            else:
                rightSide.append(item)
        else: 
            equal.append(item)
    return quicksort(leftSide) + equal + quicksort(rightSide)

def main():
    len = 10
    table = []
    for i in range(len):
        table.append(random.randint(0, 1000000))
    print("Not sorted : ", str(table))
    exectim = timeit.timeit(lambda: print("sorted : " + str(quicksort(table))), number=1)
    print("execution time = " + str(exectim))

if __name__ == "__main__":
    main()
