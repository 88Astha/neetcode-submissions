class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr = prices[0]
        maxprofit = 0

        for price in prices:
            profit = price - pr
            pr = min(pr,price)
            maxprofit = max(maxprofit,profit)

        return maxprofit