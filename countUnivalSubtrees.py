# https://leetcode.com/problems/count-univalue-subtrees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Bottom-up solution 
# If node is leaf node then it has 1 uni-value subtree 
# If node has left and right subtree as leaf node and their value are equal then node has 2 uni-value subtree 
class Solution(object):
    
    def __init__(self):
        self.count = 0
        
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root is None):
            return 0
        
        self.isUni(root)
        return self.count
    
    def isUni(self, root):
        """
        Check if root has uni-value subtree 
        :type root: TreeNode
        :rtype bool 
        
        """
        is_uni = True 
        # if node is leaf node then it has 1 uni-value subtree
        if (root.left is None and root.right is None):
            self.count +=1 
            return True 
        
        # otherwise, move to the leaf node and check if its left node vs its parent 
        if (root.left is not None):
            is_uni = self.isUni(root.left) and is_uni and root.left.val == root.val 
        
        if (root.right is not None):
            is_uni = self.isUni(root.right) and is_uni and root.right.val == root.val
        
        # if both left subTree and right subTree is uni then we can count the subtree is uni
        if (is_uni):
            self.count +=1 
            
        return is_uni
        
        
        
        
