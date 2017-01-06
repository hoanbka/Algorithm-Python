# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,

# A solution set is:
# [
#     [7],
#     [2, 2, 3]
# ]

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        # candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:  #here
                break
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


# MAIN:
# candidates = [2, 3, 6, 7]
candidates = [2, 3, 4, 5, 6, 7, 8]
target = 15

solution = Solution()
print(solution.combinationSum(candidates, target))
