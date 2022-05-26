# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
from operator import sub
from typing import List, Tuple


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        greatest_length = 1 if len(s) else 0
        for char in s:
            if char in substring:
                char_idx_in_substring = substring.index(char)
                idx = min(char_idx_in_substring + 1, len(substring))
                substring = substring[idx:]
            substring += char
            if len(substring) > greatest_length:
                greatest_length = len(substring)

        return greatest_length


greatest_length = Solution().lengthOfLongestSubstring("abcabcbb")
print(greatest_length)
