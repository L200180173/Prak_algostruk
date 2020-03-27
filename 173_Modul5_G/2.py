from kegiatan5 import *

A = [1,2,3]
B = [4,5,6]

def gabungArr(list1, list2):
    C = list1 + list2
    insertionSort(C)
    return C

print(gabungArr(A,B))
