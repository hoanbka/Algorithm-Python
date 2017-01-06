# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example,
# Given board = [
#     ['A','B','C','E'],
#     ['S','F','C','S'],
#     ['A','D','E','E']
# ]
#
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    # 3:42
    def exist(self, board, word):
        visited = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.getWords(board, word, i, j, visited):
                    return True

        return False

    def getWords(self, board, word, i, j, visited, pos=0):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
            return False

        visited[(i, j)] = True
        res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
              or self.getWords(board, word, i, j - 1, visited, pos + 1) \
              or self.getWords(board, word, i + 1, j, visited, pos + 1) \
              or self.getWords(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False

        return res


# TEST:

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"

solution = Solution()
print(solution.exist(board, word))
