'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
               
        if not p and not q:
            return True

        if not p or not q:
            return False

        stack = [(p,q)]

        while len(stack) != 0:
            
            node_p, node_q = stack.pop()
            
            # compate values
            if node_p.val != node_q.val:
                return False
            
            # add to stack
            if node_q.right and node_p.right:
                stack.append((node_p.right,node_q.right))
            elif node_q.right == None and node_p.right == None:
                pass
            else:
                return False


            if node_q.left and node_p.left:
                stack.append((node_p.left,node_q.left))
            elif node_q.left == None and node_p.left == None:
                pass
            else:
                return False

        return True
        

