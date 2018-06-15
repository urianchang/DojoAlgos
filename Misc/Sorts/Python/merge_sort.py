# Python 2.7
from utils import timer


def mergeSort(arr):
    #type: (list) -> None
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr)/2]
    left = [val for val in arr if val < mid]
    middle = [val for val in arr if val == mid]
    right = [val for val in arr if val > mid]
    return mergeSort(left) + middle + mergeSort(right)


ex1 = [2, 1, 4, 5, 7, 1, 3, 9, 9, 2]
ex2 = [9, 5, 6, 3, 2, 8, 1, 7, 10, 4]
ex3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for ts in (ex1, ex2, ex3, ex4):
    print "Before: %s" % ts

    with timer():
        mergeSort(ts)

    print "After: %s\n" % ts
