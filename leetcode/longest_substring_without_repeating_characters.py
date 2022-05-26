# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import List, Tuple


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> Tuple[set, int]:
        substrings = set()
        greatest_length = 1 if len(s) else 0
        for idx1, char1 in enumerate(s):
            idx2 = min(idx1 + 1, len(s))
            for char2 in s[idx2:]:
                if char2 in char1:
                    break
                char1 += char2
                if len(char1) > greatest_length:
                    substrings.add(char1)
                    greatest_length = len(char1)
        return substrings, greatest_length


substrings, greatest_length = Solution().lengthOfLongestSubstring("anijajaj")
print(substrings)
print(greatest_length)
