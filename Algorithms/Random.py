from random import randrange
from random import choice


def generateRamdom():
    num = randrange(10000)
    arr = ['VHS', 'OHS']
    index = randrange(2)
    length = len(str(num))
    return str(arr[index]) + ''.join(choice(['0']) for i in range(5 - length)) + str(num)

print(generateRamdom())

