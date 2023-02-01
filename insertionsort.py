
def insertionsort(table):
    sorted  = []
    while (table):
        smaller = 2147483647
        for item in table:
            if item < smaller:
                smaller = item
        sorted.append(smaller)
        table.remove(smaller)
    return sorted