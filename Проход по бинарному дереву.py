# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []

        le = self.inorderTraversal(root.left)
        ri = self.inorderTraversal(root.right)

        return le + [root.val] + ri