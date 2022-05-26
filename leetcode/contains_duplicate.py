# Problem: https://leetcode.com/problems/contains-duplicate

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any(num1 == num2 for num1, num2 in zip(nums, nums[1:]))
