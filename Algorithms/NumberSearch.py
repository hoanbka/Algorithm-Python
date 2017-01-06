'''
Have the function NumberSearch(str) take the str parameter,
search for all the numbers in the string, add them together,
then return that final number.

For example: if str is "88Hello 3World!" the output should be 91.
You will have to differentiate between single digit numbers and multiple digit numbers like in the example above.
So "55Hello" and "5Hello 5" should return two different answers.
Each string will contain at least one letter or symbol.
'''


def isDegit(s):
    return s >= '0' and s <= '9'


def decodeNumber(arr):
    element = ''
    while len(arr) > 0 and isDegit(arr[0]):
        element = element + arr.pop(0)
    return element


def addNumbers(str):
    arr = list(str)
    result = []
    while len(arr) > 0:
        num = decodeNumber(arr)

        while len(arr) > 0 and not isDegit(arr[0]):
            arr.pop(0)
        if len(num) > 0:
            result.append(int(num))
    return sum(result)


str = 'abc123vbn5'
print(addNumbers(str))
