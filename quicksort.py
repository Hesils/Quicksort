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

