# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
# [
#     ["aa","b"],
#     ["a","a","b"]
# ]

def partition(self, s):
    return [[s[:i]] + rest
            for i in xrange(1, len(s) + 1)
            if s[:i] == s[i - 1::-1]
            for rest in self.partition(s[i:])] or [[]]


class Solution(object):
    def partition(self, s):
        ret = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[i - 1::-1]:
                for rest in self.partition(s[i:]):
                    ret.append([s[:i]] + rest)
        if not ret:
            return [[]]
        return ret


str = "moment"

solution = Solution()
print(solution.partition(str))
