'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1
'''


import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        start_sequence = 1
        end_sequence = x//2 


        while start_sequence < end_sequence:
            m = math.floor((start_sequence + end_sequence) / 2)
            
            if m * m == x:
                return int(m)
                
            elif (m + 1) * (m + 1) > x:
                end_sequence = int(m)
            else:
                start_sequence = int(m) + 1

        return int(start_sequence)