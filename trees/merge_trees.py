# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
     def to_string(self):
         return [self.val, self.left, self.right]
from typing import Optional
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        else:
            root1.val +=root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
sol =  Solution()
#[1,3,2,5]
root1 = TreeNode(val=1)
root1.left = TreeNode(val=3)
root1.right = TreeNode(val=2)
root1.left.left = TreeNode(val=5)
#[2,1,3,None,4,None,7]
root2 = TreeNode(2)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(4)
root2.right.left = None
root2.right.right = TreeNode(7)

expected = [3,4,5,5,4,None,7]
result = sol.mergeTrees(root1, root2)
print(result.to_string())
