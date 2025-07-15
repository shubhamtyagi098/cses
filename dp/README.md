# Dynamic Programming: Coin Change Problems

This folder contains solutions to two classic dynamic programming problems related to coin change:

1. **Coin Combinations I (Permutations)** - Count ways to make a sum where order matters
2. **Coin Combinations II (Combinations)** - Count ways to make a sum where order doesn't matter

## Understanding the Difference

The key difference between these problems is whether the order of coins matters:

- In **permutations** (CSES problem), arrangements like `[1,2]` and `[2,1]` are counted as different ways.
- In **combinations** (LeetCode problem), arrangements like `[1,2]` and `[2,1]` are counted as the same way.

## Approach 1: Counting Permutations

```python
# Outer loop over amounts, inner loop over coins
for amount in range(1, target + 1):
    for coin in coins:
        if coin <= amount:
            dp[amount] += dp[amount - coin]
```

### Visual Trace with Example

Let's trace through with coins = [1, 2] and target = 3:

**Initialize:** dp = [1, 0, 0, 0]

**Process amount = 1:**
- coin = 1: dp[1] += dp[0] = 0 + 1 = 1
- dp = [1, 1, 0, 0]

**Process amount = 2:**
- coin = 1: dp[2] += dp[1] = 0 + 1 = 1
- coin = 2: dp[2] += dp[0] = 1 + 1 = 2
- dp = [1, 1, 2, 0]

**Process amount = 3:**
- coin = 1: dp[3] += dp[2] = 0 + 2 = 2
- coin = 2: dp[3] += dp[1] = 2 + 1 = 3
- dp = [1, 1, 2, 3]

**Final result:** dp[3] = 3, meaning there are 3 ways to make 3:
- 1+1+1
- 1+2
- 2+1

### Explanation

When we process each amount in the outer loop, we're considering all possible "last coins" that could be added to make that amount. This naturally counts different orderings as distinct solutions.

For example, when processing amount 3:
- Adding coin 1 to existing ways to make amount 2 (which are [1,1] and [2])
- Adding coin 2 to existing ways to make amount 1 (which is [1])

This gives us [1,1,1], [2,1], and [1,2] as three distinct ways.

## Approach 2: Counting Combinations

```python
# Outer loop over coins, inner loop over amounts
for coin in coins:
    for amount in range(coin, target + 1):
        dp[amount] += dp[amount - coin]
```

### Visual Trace with Example

Let's trace through with coins = [1, 2] and target = 3:

**Initialize:** dp = [1, 0, 0, 0]

**Process coin = 1:**
- amount = 1: dp[1] += dp[0] = 0 + 1 = 1
- amount = 2: dp[2] += dp[1] = 0 + 1 = 1
- amount = 3: dp[3] += dp[2] = 0 + 1 = 1
- dp = [1, 1, 1, 1]

**Process coin = 2:**
- amount = 2: dp[2] += dp[0] = 1 + 1 = 2
- amount = 3: dp[3] += dp[1] = 1 + 1 = 2
- dp = [1, 1, 2, 2]

**Final result:** dp[3] = 2, meaning there are 2 ways to make 3:
- 1+1+1
- 1+2

### Explanation

By processing one coin type completely before moving to the next, we ensure that combinations are counted only once. This approach effectively enforces an ordering on the coins, which eliminates duplicate counting of the same combination in different orders.

For example, when we process coin 2:
- For amount 3: We're only considering adding a 2-coin to existing combinations that used only 1-coins (which is [1])
- This gives us [1,2] but not [2,1], because we're building our solution coin-by-coin rather than position-by-position

## Visual Representation of DP Tables

### Permutations (Amount in Outer Loop)

```
dp[0] = 1 (base case)

For amount = 1:
  coin = 1: dp[1] = 1
  coin = 2: (skipped as 2 > 1)
  dp = [1, 1, 0, 0]

For amount = 2:
  coin = 1: dp[2] = 1
  coin = 2: dp[2] = 2
  dp = [1, 1, 2, 0]

For amount = 3:
  coin = 1: dp[3] = 2
  coin = 2: dp[3] = 3
  dp = [1, 1, 2, 3]
```

### Combinations (Coin in Outer Loop)

```
dp[0] = 1 (base case)

For coin = 1:
  amount = 1: dp[1] = 1
  amount = 2: dp[2] = 1
  amount = 3: dp[3] = 1
  dp = [1, 1, 1, 1]

For coin = 2:
  amount = 2: dp[2] = 2
  amount = 3: dp[3] = 2
  dp = [1, 1, 2, 2]
```

## Key Insights

1. **Loop Order Matters**: The order of the loops determines whether we count combinations or permutations.

2. **State Definition**: In both approaches, dp[i] represents the number of ways to make amount i using the available coins.

3. **Transition Function**: The basic recurrence relation dp[amount] += dp[amount - coin] is the same in both approaches, but the order of applying it makes all the difference.

4. **Modulo Operation**: Both problems typically require taking the result modulo a large number (e.g., 10^9 + 7) to handle large outputs.

## Time and Space Complexity

- **Time Complexity**: O(n × target) where n is the number of coins and target is the target sum.
- **Space Complexity**: O(target) for the dp array.
