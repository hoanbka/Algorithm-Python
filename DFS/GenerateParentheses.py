def generateParenthesis(n):
    list = []
    backtrack(list, "", 0, 0, n)
    return list


def backtrack(list, str, open, close, max):
    if (len(str) == max * 2):
        list.append(str)
        return

    if (open < max):
        backtrack(list, str + "(", open + 1, close, max)
    if (close < open):
        backtrack(list, str + ")", open, close + 1, max)


print(generateParenthesis(3))
