import os

res = []


def readFolderUsingRecursive(file):
    if os.path.isfile(file):
        res.append(os.path.getsize(file))
    else:
        arr = os.listdir(file)
        for element in arr:
            child = file + "\\" + element

            if os.path.isfile(child):
                res.append(os.path.getsize(child))
            else:
                readFolderUsingRecursive(child)
    return sum(res)


def readFolderUsingStack(file):
    size = []
    if os.path.isfile(file):
        return os.path.getsize(file)
    else:
        arr = os.listdir(file)

        while True:

            if arr:
                temp = arr.pop()
                print('temp = ' + temp)
                child = file + "\\" + temp
                print('child = ' + child)

                if os.path.isfile(child):
                    print('size = '+ str(os.path.getsize(child)))
                    size.append(os.path.getsize(child))
                else:
                    for i in os.listdir(child):
                        print('i = ' + i)
                        arr.append(temp+"\\"+i)
            else:
                break

    return sum(size)


path = 'D:\English'
# path = 'D:\STC'
# path ='D:\English\English_Collocations_in_Use_Advanced.pdf'
arr = readFolderUsingRecursive(path)
print(arr)
print(readFolderUsingStack(path))
