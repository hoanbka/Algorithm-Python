def bubbleSort(arr):
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i + 1]:
                # temp = arr[i]
                # arr[i] = arr[i + 1]
                # arr[i + 1] = temp
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(arr)
print(arr)


def bubleSort2(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(bubleSort2(arr))
