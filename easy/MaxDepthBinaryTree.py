from collections import deque


# Definition for a binary tree node.
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root == None:
            return 0


        max_depth = 0
        stack = deque([[root,1]])

        while stack:

            node, depth = stack.pop()
            max_depth = max(max_depth,depth)

            if node.left:
                stack.append([node.left,depth + 1])
            if node.right:
                stack.append([node.right,depth + 1])
        

        return max_depth

            





