# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_ptr, sell_ptr = 0, 1

        while sell_ptr < len(prices):
            if prices[sell_ptr] > prices[buy_ptr]:  # We have a profit here
                profit = prices[sell_ptr] - prices[buy_ptr]
                max_profit = max(profit, max_profit)
            else:
                buy_ptr = sell_ptr
            sell_ptr += 1
        return max_profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
