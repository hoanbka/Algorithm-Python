def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return array
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot - 1)
    quicksort(array, pivot + 1, end)


arr = [12, 4, 5, 6, 7, 12, 15, 3, 1, 15]
print(quicksort(arr))
