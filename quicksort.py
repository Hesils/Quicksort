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
    for i in range(len(tab)):
        if tab[i] != pivot:
            if tab[i] < pivot:
                leftSide.append(tab[i])
            else:
                rightSide.append(tab[i])
        else: 
            equal.append(tab[i])
    sortedTab = quicksort(leftSide) + equal + [pivot] + quicksort(rightSide)
    return sortedTab

def main():
    len = 100000
    table = []
    for i in range(len):
        table.append(random.randint(0, 1000000))
    exectim = timeit.timeit(lambda: quicksort(table), number=1)
    sortedTable  = quicksort(table)
    print("Not sorted : " + str(table))
    print("Sorted : " + str(sortedTable))
    print("execution time = " + str(exectim))

if __name__ == "__main__":
    main()
