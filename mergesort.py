def mergeTables(table1, table2):
    table1len = len(table1)
    table2len = len(table2)
    index1 = 0
    index2 = 0
    ret = []
    while len(ret) < table2len + table1len:
        if index1 >= table1len:
            ret.append(table2[index2])
            index2 += 1
        elif index2 >= table2len:
            ret.append(table1[index1])
            index1 += 1
        elif table1[index1] < table2[index2]:
            ret.append(table1[index1])
            index1 += 1
        else:
            ret.append(table2[index2])
            index2 += 1
    return ret

def mergesort(tab):
    if len(tab) < 2:
        return tab
    if len(tab) == 2:
        if tab[0] > tab[1]:
            tmp = tab[0]
            tab[0] = tab[1]
            tab[1] = tmp
        return tab
    midleIndex = int(len(tab) / 2)
    leftTab = tab[:midleIndex]
    rightTab = tab[midleIndex:]
    leftTab = mergesort(leftTab)
    rightTab = mergesort(rightTab)
    return mergeTables(leftTab, rightTab)