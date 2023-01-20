from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, num in enumerate(nums):
            if num in hash_map.keys():
                return hash_map.get(num), idx
            hash_map[target - num] = idx


if __name__ == "__main__":
    print(Solution().twoSum(nums=[3, 3], target=6))
