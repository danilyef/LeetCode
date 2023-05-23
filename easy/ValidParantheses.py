'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

'''




class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {'(':')','[':']','{':'}'}
        
        if len(s) % 2 == 1:
            return False
        
        stack = []
        
        for c in s:
            if c in hash_table:
                stack.append(c)
            elif len(stack) == 0 or hash_table[stack.pop()] != c:
                return False
         
        if len(stack) != 0:
            return False
        
        return True