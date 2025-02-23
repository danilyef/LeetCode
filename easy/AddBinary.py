'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''



from collections import deque

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        c = deque()
        ptr_a = len(a) - 1
        ptr_b = len(b) - 1
        rest = 0

        while ptr_a >= 0 or ptr_b >= 0 or rest > 0: 
            elem_a = 0 if ptr_a < 0 else ord(a[ptr_a]) - ord('0')
            elem_b = 0 if ptr_b < 0 else ord(b[ptr_b]) - ord('0')          
            
            tmp = elem_a + elem_b + rest
            c.appendleft(str(tmp % 2))
            rest = 1 if tmp > 1 else 0
            
            ptr_a -=1
            ptr_b -=1


        return ''.join(c)





        

