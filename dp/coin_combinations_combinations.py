"""
LeetCode Problem: Coin Change II (https://leetcode.com/problems/coin-change-ii/)
This problem asks for the number of ways to form a sum using coins, where order doesn't matter (combinations).
"""

def count_ways_combinations():
    # Read input
    n, target = map(int, input().split())
    coins = list(map(int, input().split()))
    
    # Initialize DP array
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: one way to make sum 0 (by using no coins)
    
    # Fill the DP array - combination approach (coin in outer loop)
    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] = (dp[amount] + dp[amount - coin]) % (10**9 + 7)
    
    # Return the result
    return dp[target]

if __name__ == "__main__":
    print(count_ways_combinations())
