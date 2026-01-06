# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        left_count = right_count = 0
        
        def count(node):
            nonlocal left_count, right_count
            if not node:
                return 0
            
            l = count(node.left)
            r = count(node.right)
            
            if node.val == x:
                left_count = l
                right_count = r
            
            return l + r + 1
        
        count(root)
        
        # Three options: choose x's left subtree, x's right subtree, or x's parent subtree
        parent_count = n - left_count - right_count - 1
        
        # We win if any of the three regions > half of all nodes
        half = n // 2
        return left_count > half or right_count > half or parent_count > half