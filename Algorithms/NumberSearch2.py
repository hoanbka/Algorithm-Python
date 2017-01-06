def isDigit(s):
    return s >= '0' and s <= '9'


def decodeNumber(timeArr):
    r = ''
    while len(timeArr) > 0 and isDigit(timeArr[0]):
        r = r + timeArr.pop(0)
    return r


def NumberAddition(s):
    arr = list(s)
    nums = []
    while len(arr) > 0:
        print
        arr
        num = decodeNumber(arr)
        while len(arr) > 0 and not isDigit(arr[0]):
            arr.pop(0)
        if len(num) > 0:
            nums.append(int(num))
    return sum(nums)


print(NumberAddition('94fdfs4'))


