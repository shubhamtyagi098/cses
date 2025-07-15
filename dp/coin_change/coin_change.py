"""
LeetCode Problem: Coin Change (https://leetcode.com/problems/coin-change/)
This problem asks for the minimum number of coins needed to make up a given amount.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Initialize DP array with infinity
        dp = [float("inf")] * (amount + 1)
        
        # Base case: it takes 0 coins to make amount 0
        dp[0] = 0
        
        # Fill the DP array
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return the result, or -1 if it's not possible
        return dp[amount] if dp[amount] != float("inf") else -1

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)
