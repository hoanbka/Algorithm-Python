def sort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
        return sort(less) + equal + sort(greater)
    else:
        return arr


arr = [12, 4, 5, 6, 7, 12, 15, 3, 1, 15]
print(sort(arr))
