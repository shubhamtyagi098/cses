"""
LeetCode Problem: Coin Change (https://leetcode.com/problems/coin-change/)
This is an INCORRECT implementation to demonstrate why certain choices don't work.
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
        
        # Incorrect base case: setting dp[0] = 1
        dp[0] = 1
        
        # Incorrect transition: missing the +1
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin])  # Missing +1 here
        
        # Return the result, or -1 if it's not possible
        return dp[amount] if dp[amount] != float("inf") else -1

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))  # Will give incorrect result
