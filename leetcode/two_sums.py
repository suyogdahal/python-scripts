# Problem: https://leetcode.com/problems/two-sum/

from typing import List


class TwoSums:
    def two_sums(self, nums: List[int], target: int):
        ref: dict = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in ref:
                return [ref[diff], idx]
            ref[num] = idx


if __name__ == "__main__":
    print(TwoSums().two_sums([1, 2, 3], 5))
