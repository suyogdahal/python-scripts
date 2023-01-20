import re
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_sell = prices[0], prices[0]
        idx_min = False
        for price in prices:
            if price < min_buy:
                min_buy = price
                idx_min = True
            if price > max_sell and idx_min:
                max_sell = price
        return max_sell - min_buy


if __name__ == "__main__":
    Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4])
