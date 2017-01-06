import time

def binarySearch(arr, item):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == item:
            found = True
        else:
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

start_time = time.time()
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(binarySearch(arr, 77))
print("--- %s seconds ---" % (time.time() - start_time))