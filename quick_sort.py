"""
An implementation of Quick sort algorithm.
Pivot is assumed to be the last element in the list.
"""
i
def partition(array, low, high):
    i = low-1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)


def quicksort(array, low, high):
    if low < high:
        pivotIndex = partition(array, low, high)
        quicksort(array, low, pivotIndex-1)
        quicksort(array, pivotIndex+1, high)
    return array
