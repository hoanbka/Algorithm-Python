def linearSearch(arr, item):
    pos = 0
    found = False
    while pos < len(arr):
        if arr[pos] == item:
            found = True
            break
        else:
            pos += 1
    return found


def linearSearch2(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return True
    return False


arr = [3, 6, 8, 2, 65, 7, 89]

print(linearSearch(arr, 89))
print(linearSearch2(arr, 89))
