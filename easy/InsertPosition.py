"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
"""

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (right + left)//2

            if nums[index] == target :
                return index
            elif target < nums[index]:
                right = index - 1
            elif target > nums[index]:
                left = index + 1


        return left