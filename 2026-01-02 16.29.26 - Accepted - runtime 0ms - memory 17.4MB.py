# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        # Find the node with value x and count its subtrees
        left_count = 0
        right_count = 0
        
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        
        def find_x(node):
            nonlocal left_count, right_count
            if not node:
                return False
            if node.val == x:
                left_count = count_nodes(node.left)
                right_count = count_nodes(node.right)
                return True
            return find_x(node.left) or find_x(node.right)
        
        find_x(root)
        
        # Player 2 can choose:
        # 1. Parent of x (gets n - left_count - right_count - 1 nodes)
        # 2. Left child of x (gets left_count nodes)
        # 3. Right child of x (gets right_count nodes)
        
        parent_side = n - left_count - right_count - 1
        
        # Player 2 wins if they can get more than n/2 nodes
        max_player2 = max(left_count, right_count, parent_side)
        
        return max_player2 > n // 2