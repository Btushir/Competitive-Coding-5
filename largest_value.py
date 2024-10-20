"""
BFS: TC: O(n) SC: O(n)
"""
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bfs(self, root, ans):

        q = deque()
        q.append(root)

        while q:
            level_lst = []
            size = len(q)
            max_el = float("-inf")
            for _ in range(size):
                curr = q.popleft()
                max_el = max(max_el, curr.val)
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            ans.append(max_el)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        self.bfs(root, ans)
        return ans

