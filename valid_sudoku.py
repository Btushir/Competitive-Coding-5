"""
TC: 3 * O(m*n), SC: 3*O(m)
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row
        m = len(board)  # rows
        n = len(board[0])  # cols
        ans = True

        for i in range(m):
            temp = set()
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.add(board[i][j])
        # cols
        for i in range(m):
            temp = set()
            for j in range(n):
                if board[j][i] != ".":
                    if board[j][i] in temp:
                        return False
                    else:
                        temp.add(board[j][i])

        # cells
        r_start = 0
        r_end = 0
        c_start = 0
        c_end = 0
        for l in range(3):
            r_start = r_end  # 3
            r_end = r_start + 3  # 6
            c_start = 0
            c_end = 0
            for k in range(3):
                c_start = c_end  # 0
                c_end = c_start + 3  # 6
                temp = set()
                for i in range(r_start, r_end):  # (0,3)
                    for j in range(c_start, c_end):  # (6,9)
                        if board[i][j] != ".":
                            if board[i][j] in temp:
                                return False
                            else:
                                temp.add(board[i][j])

        return True
