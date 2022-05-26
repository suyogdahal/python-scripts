# Problem: https://leetcode.com/problems/missing-number
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = sum(range(n + 1))
        given_sum = sum(nums)
        return expected_sum - given_sum
