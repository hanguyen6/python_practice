# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
###
# Use a queue to store a list of nodes 
# Initially only root in the queue 
# As long as the queue is not empty, remove next node from the queue
# Swap its children and add them to the queue 
# Eventually the queue is empty, all children swapped 
#
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root is None):
            return root 
        
        queue = []
        queue = queue + [root]
        while (len(queue) != 0):
            elem = queue[0]
            queue = queue[1:]
            
            tmp = elem.left
            elem.left = elem.right
            elem.right = tmp 
            
            if (elem.left is not None):
                queue = queue + [elem.left]
            if (elem.right is not None):
                queue = queue + [elem.right ]
                
        return root
            
        
