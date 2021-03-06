#Recursive DFS solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)
        return 1 + max(maxLeft, maxRight)
        

#BFS solution using Queue
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: #is not null
                    queue.append(node.left)
                if node.right: #is not null
                    queue.append(node.right)
            level += 1
        return level

# Iterative DFS using stack in pre-order manner
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        result = 0
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result