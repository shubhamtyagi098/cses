# Dynamic Programming: Coin Change Problem

## Problem Statement (LeetCode 322)

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

## Understanding the Problem

This is a classic dynamic programming problem where we need to find the minimum number of coins required to make a given amount.

## State Definition

- `dp[i]` = the minimum number of coins needed to make amount `i`

## Base Case

- `dp[0] = 0` because it takes 0 coins to make amount 0

## Transition Function

- `dp[i] = min(dp[i], dp[i - coin] + 1)` for each coin in coins if `coin <= i`

## Why Base Case Matters: dp[0] = 0 vs dp[0] = 1

### Correct Approach: dp[0] = 0

Setting `dp[0] = 0` correctly represents that it takes 0 coins to make amount 0. This is logically sound - if we need to make 0 amount, we don't need any coins.

### Incorrect Approach: dp[0] = 1

Setting `dp[0] = 1` would incorrectly suggest that it takes 1 coin to make amount 0, which is logically flawed. This leads to incorrect calculations for all subsequent amounts.

## Why the +1 in Transition Matters

The `+1` in the transition function `dp[i] = min(dp[i], dp[i - coin] + 1)` represents the additional coin we're using. Without this `+1`, we're not accounting for the coin we just decided to use, which would lead to incorrect results.

## Visual Trace with Example

Let's trace through with coins = [1, 2, 5] and amount = 11:

### Correct Implementation (dp[0] = 0, with +1 in transition)

**Initialize:** dp = [0, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 1:**
- coin = 1: dp[1] = min(∞, dp[0] + 1) = min(∞, 0 + 1) = 1
- coin = 2: (skipped as 2 > 1)
- coin = 5: (skipped as 5 > 1)
- dp = [0, 1, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 2:**
- coin = 1: dp[2] = min(∞, dp[1] + 1) = min(∞, 1 + 1) = 2
- coin = 2: dp[2] = min(2, dp[0] + 1) = min(2, 0 + 1) = 1
- coin = 5: (skipped as 5 > 2)
- dp = [0, 1, 1, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 3:**
- coin = 1: dp[3] = min(∞, dp[2] + 1) = min(∞, 1 + 1) = 2
- coin = 2: dp[3] = min(2, dp[1] + 1) = min(2, 1 + 1) = 2
- coin = 5: (skipped as 5 > 3)
- dp = [0, 1, 1, 2, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 4:**
- coin = 1: dp[4] = min(∞, dp[3] + 1) = min(∞, 2 + 1) = 3
- coin = 2: dp[4] = min(3, dp[2] + 1) = min(3, 1 + 1) = 2
- coin = 5: (skipped as 5 > 4)
- dp = [0, 1, 1, 2, 2, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 5:**
- coin = 1: dp[5] = min(∞, dp[4] + 1) = min(∞, 2 + 1) = 3
- coin = 2: dp[5] = min(3, dp[3] + 1) = min(3, 2 + 1) = 3
- coin = 5: dp[5] = min(3, dp[0] + 1) = min(3, 0 + 1) = 1
- dp = [0, 1, 1, 2, 2, 1, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 6:**
- coin = 1: dp[6] = min(∞, dp[5] + 1) = min(∞, 1 + 1) = 2
- coin = 2: dp[6] = min(2, dp[4] + 1) = min(2, 2 + 1) = 2
- coin = 5: dp[6] = min(2, dp[1] + 1) = min(2, 1 + 1) = 2
- dp = [0, 1, 1, 2, 2, 1, 2, ∞, ∞, ∞, ∞, ∞]

**Process amount = 7:**
- coin = 1: dp[7] = min(∞, dp[6] + 1) = min(∞, 2 + 1) = 3
- coin = 2: dp[7] = min(3, dp[5] + 1) = min(3, 1 + 1) = 2
- coin = 5: dp[7] = min(2, dp[2] + 1) = min(2, 1 + 1) = 2
- dp = [0, 1, 1, 2, 2, 1, 2, 2, ∞, ∞, ∞, ∞]

**Process amount = 8:**
- coin = 1: dp[8] = min(∞, dp[7] + 1) = min(∞, 2 + 1) = 3
- coin = 2: dp[8] = min(3, dp[6] + 1) = min(3, 2 + 1) = 3
- coin = 5: dp[8] = min(3, dp[3] + 1) = min(3, 2 + 1) = 3
- dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, ∞, ∞, ∞]

**Process amount = 9:**
- coin = 1: dp[9] = min(∞, dp[8] + 1) = min(∞, 3 + 1) = 4
- coin = 2: dp[9] = min(4, dp[7] + 1) = min(4, 2 + 1) = 3
- coin = 5: dp[9] = min(3, dp[4] + 1) = min(3, 2 + 1) = 3
- dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, ∞, ∞]

**Process amount = 10:**
- coin = 1: dp[10] = min(∞, dp[9] + 1) = min(∞, 3 + 1) = 4
- coin = 2: dp[10] = min(4, dp[8] + 1) = min(4, 3 + 1) = 4
- coin = 5: dp[10] = min(4, dp[5] + 1) = min(4, 1 + 1) = 2
- dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, ∞]

**Process amount = 11:**
- coin = 1: dp[11] = min(∞, dp[10] + 1) = min(∞, 2 + 1) = 3
- coin = 2: dp[11] = min(3, dp[9] + 1) = min(3, 3 + 1) = 3
- coin = 5: dp[11] = min(3, dp[6] + 1) = min(3, 2 + 1) = 3
- dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]

**Final result:** dp[11] = 3, meaning we need 3 coins to make amount 11.
The optimal solution is to use coins [5, 5, 1].

### Incorrect Implementation (dp[0] = 1, without +1 in transition)

**Initialize:** dp = [1, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 1:**
- coin = 1: dp[1] = min(∞, dp[0]) = min(∞, 1) = 1
- coin = 2: (skipped as 2 > 1)
- coin = 5: (skipped as 5 > 1)
- dp = [1, 1, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 2:**
- coin = 1: dp[2] = min(∞, dp[1]) = min(∞, 1) = 1
- coin = 2: dp[2] = min(1, dp[0]) = min(1, 1) = 1
- coin = 5: (skipped as 5 > 2)
- dp = [1, 1, 1, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 3:**
- coin = 1: dp[3] = min(∞, dp[2]) = min(∞, 1) = 1
- coin = 2: dp[3] = min(1, dp[1]) = min(1, 1) = 1
- coin = 5: (skipped as 5 > 3)
- dp = [1, 1, 1, 1, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 4:**
- coin = 1: dp[4] = min(∞, dp[3]) = min(∞, 1) = 1
- coin = 2: dp[4] = min(1, dp[2]) = min(1, 1) = 1
- coin = 5: (skipped as 5 > 4)
- dp = [1, 1, 1, 1, 1, ∞, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 5:**
- coin = 1: dp[5] = min(∞, dp[4]) = min(∞, 1) = 1
- coin = 2: dp[5] = min(1, dp[3]) = min(1, 1) = 1
- coin = 5: dp[5] = min(1, dp[0]) = min(1, 1) = 1
- dp = [1, 1, 1, 1, 1, 1, ∞, ∞, ∞, ∞, ∞, ∞]

**Process amount = 6:**
- coin = 1: dp[6] = min(∞, dp[5]) = min(∞, 1) = 1
- coin = 2: dp[6] = min(1, dp[4]) = min(1, 1) = 1
- coin = 5: dp[6] = min(1, dp[1]) = min(1, 1) = 1
- dp = [1, 1, 1, 1, 1, 1, 1, ∞, ∞, ∞, ∞, ∞]

**Process amount = 7:**
- coin = 1: dp[7] = min(∞, dp[6]) = min(∞, 1) = 1
- coin = 2: dp[7] = min(1, dp[5]) = min(1, 1) = 1
- coin = 5: dp[7] = min(1, dp[2]) = min(1, 1) = 1
- dp = [1, 1, 1, 1, 1, 1, 1, 1, ∞, ∞, ∞, ∞]

**Process amount = 8:**
- coin = 1: dp[8] = min(∞, dp[7]) = min(∞, 1) = 1
- coin = 2: dp[8] = min(1, dp[6]) = min(1, 1) = 1
- coin = 5: dp[8] = min(1, dp[3]) = min(1, 1) = 1
- dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, ∞, ∞, ∞]

**Process amount = 9:**
- coin = 1: dp[9] = min(∞, dp[8]) = min(∞, 1) = 1
- coin = 2: dp[9] = min(1, dp[7]) = min(1, 1) = 1
- coin = 5: dp[9] = min(1, dp[4]) = min(1, 1) = 1
- dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ∞, ∞]

**Process amount = 10:**
- coin = 1: dp[10] = min(∞, dp[9]) = min(∞, 1) = 1
- coin = 2: dp[10] = min(1, dp[8]) = min(1, 1) = 1
- coin = 5: dp[10] = min(1, dp[5]) = min(1, 1) = 1
- dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ∞]

**Process amount = 11:**
- coin = 1: dp[11] = min(∞, dp[10]) = min(∞, 1) = 1
- coin = 2: dp[11] = min(1, dp[9]) = min(1, 1) = 1
- coin = 5: dp[11] = min(1, dp[6]) = min(1, 1) = 1
- dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

**Final result:** dp[11] = 1, which is clearly wrong! We can't make amount 11 with just 1 coin from [1, 2, 5].

## Why the Incorrect Implementation Fails

1. **Incorrect Base Case**: Setting `dp[0] = 1` means it takes 1 coin to make amount 0, which is logically incorrect.

2. **Missing the +1 in Transition**: Without adding 1 when we use a coin, we're not counting the coins we use. This leads to all amounts having the same coin count as their subproblems, which is clearly wrong.

3. **Result Propagation**: The incorrect values propagate through the DP table, leading to a final result that suggests we can make any amount with just 1 coin, which is absurd.

## Conclusion

The Coin Change problem demonstrates the importance of:

1. **Correct Base Case**: `dp[0] = 0` correctly represents that it takes 0 coins to make amount 0.

2. **Proper Transition Function**: The `+1` in `dp[i] = min(dp[i], dp[i - coin] + 1)` is crucial as it accounts for the additional coin we're using.

3. **Logical State Definition**: `dp[i]` must represent the minimum number of coins needed to make amount `i`.

These principles ensure that our dynamic programming solution correctly calculates the minimum number of coins needed for any given amount.

## Time and Space Complexity

- **Time Complexity**: O(amount × n) where n is the number of coins and amount is the target amount.
- **Space Complexity**: O(amount) for the dp array.
