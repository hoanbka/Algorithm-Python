# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
# [
#     ["aa","b"],
#     ["a","a","b"]
# ]


def find_palindrome_substring(str):
    substrings = []
    for i in range(len(str)):
        for j in range(len(str)):
            if ((str[i:j + 1] != '') & (isPalindrome(str[i:j + 1]))):
                substrings.append(str[i:j + 1])
    return substrings


def find(str):
    substrings = []
    for i in range(len(str)):
        for j in range((i + 1), len(str)+1):
            if  (isPalindrome(str[i:j])):
                substrings.append(str[i:j])
    return substrings


def isPalindrome(str):
    i = 0
    j = len(str) - 1
    while i < j:
        if str[i] != str[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


str = "moment"
substrings = find_palindrome_substring(str)
print(substrings)

print(len(str))

print(find(str))
print(str[len(str)-1:len(str)])