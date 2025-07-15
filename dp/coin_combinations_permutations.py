"""
CSES Problem: Coin Combinations I (https://cses.fi/problemset/task/1635)
This problem asks for the number of ways to form a sum using coins, where order matters (permutations).
"""

def count_ways_permutations():
    # Read input
    n, target = map(int, input().split())
    coins = list(map(int, input().split()))
    
    # Initialize DP array
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: one way to make sum 0 (by using no coins)
    
    # Fill the DP array - permutation approach (amount in outer loop)
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = (dp[amount] + dp[amount - coin]) % (10**9 + 7)
    
    # Return the result
    return dp[target]

if __name__ == "__main__":
    print(count_ways_permutations())
