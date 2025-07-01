# Flight Discount - Advanced State-Space Dijkstra

*A comprehensive tutorial on solving CSES Flight Discount using state augmentation techniques*

## Problem Statement

**CSES - Flight Discount**: Given a directed graph with `n` nodes and `m` edges, find the minimum cost to travel from node 1 to node n, with the ability to use exactly one discount coupon that halves the cost of any single edge.

**Problem Link**: https://cses.fi/problemset/task/1195/

### Input Format
```
n m
a₁ b₁ c₁
a₂ b₂ c₂
...
aₘ bₘ cₘ
```

### Constraints
- 1 ≤ n ≤ 100,000
- 1 ≤ m ≤ 200,000
- 1 ≤ aᵢ, bᵢ ≤ n
- 1 ≤ cᵢ ≤ 10⁹

## Key Insights

### Core Observation
This isn't just a shortest path problem—it's a **state-space search** where each node has two possible states:
- **State 0**: Reached without using the discount coupon
- **State 1**: Reached after using the discount coupon

### Mental Model
Think of it as exploring a **2-layered graph**:
```
Layer 0 (Coupon Available):    1 → 2 → 3 → 4
                               ↓   ↓   ↓   ↓  (Use coupon)
Layer 1 (Coupon Used):         1 → 2 → 3 → 4
```

## Algorithm Visualization

Let's trace through a concrete example to see how the algorithm works.

### Example Graph
```
     10        8
  1 ----→ 2 ----→ 4
  |               ↗
  | 6         12 /
  ↓           /
  3 --------→
```

**Graph representation:**
- Edge 1→2: cost 10
- Edge 1→3: cost 6  
- Edge 2→4: cost 8
- Edge 3→4: cost 12

### State Array Evolution

We maintain `dist[node][used_coupon]` where:
- `used_coupon = 0`: coupon still available
- `used_coupon = 1`: coupon already used

#### Initial State
```
dist = [
    [∞, ∞],  # node 0 (unused)
    [0, ∞],  # node 1: start here
    [∞, ∞],  # node 2
    [∞, ∞],  # node 3
    [∞, ∞]   # node 4: destination
]

Priority Queue: [(0, 1, 0)]  # (cost, node, used_coupon)
```

#### Step 1: Process node 1 (cost=0, coupon=available)

**Exploring edges from node 1:**

**Edge 1→2 (weight=10):**
```python
# Option A: Take edge at full cost
dist[2][0] = min(∞, 0+10) = 10

# Option B: Use coupon on this edge
dist[2][1] = min(∞, 0+10//2) = 5
```

**Edge 1→3 (weight=6):**
```python
# Option A: Take edge at full cost  
dist[3][0] = min(∞, 0+6) = 6

# Option B: Use coupon on this edge
dist[3][1] = min(∞, 0+6//2) = 3
```

**Updated state:**
```
dist = [
    [∞, ∞],  # node 0
    [0, ∞],  # node 1
    [10, 5], # node 2: 10 without coupon, 5 with coupon
    [6, 3],  # node 3: 6 without coupon, 3 with coupon  
    [∞, ∞]   # node 4
]

PQ: [(3, 3, 1), (5, 2, 1), (6, 3, 0), (10, 2, 0)]
```

#### Step 2: Process node 3 (cost=3, coupon=used)

**Edge 3→4 (weight=12):**
```python
# Only option: full cost (coupon already used)
dist[4][1] = min(∞, 3+12) = 15
```

**Updated state:**
```
dist = [
    [∞, ∞],  # node 0
    [0, ∞],  # node 1
    [10, 5], # node 2
    [6, 3],  # node 3
    [∞, 15]  # node 4: 15 with coupon used
]
```

#### Step 3: Process node 2 (cost=5, coupon=used)

**Edge 2→4 (weight=8):**
```python
# Only option: full cost (coupon already used)
dist[4][1] = min(15, 5+8) = 13  # Better path found!
```

#### Step 4: Process node 3 (cost=6, coupon=available)

**Edge 3→4 (weight=12):**
```python
# Option A: Full cost
dist[4][0] = min(∞, 6+12) = 18

# Option B: Use coupon
dist[4][1] = min(13, 6+12//2) = min(13, 12) = 12  # Best path!
```

**Final state:**
```
dist = [
    [∞, ∞],  # node 0
    [0, ∞],  # node 1
    [10, 5], # node 2
    [6, 3],  # node 3
    [18, 12] # node 4: 18 without coupon, 12 with coupon
]

Answer: min(dist[4][0], dist[4][1]) = min(18, 12) = 12
```

### Visual Path Analysis

```
OPTIMAL SOLUTION FOUND:

Path: 1 → 3 → 4
├─ 1 → 3: cost 6 (full price, save coupon)
└─ 3 → 4: cost 12 → 6 (use coupon here!)

Total cost: 6 + 6 = 12

Alternative paths considered:
❌ 1 → 2 → 4 (full): 10 + 8 = 18
❌ 1 → 2 → 4 (coupon on 1→2): 5 + 8 = 13  
❌ 1 → 3 → 4 (coupon on 1→3): 3 + 12 = 15
✅ 1 → 3 → 4 (coupon on 3→4): 6 + 6 = 12
```

## Algorithm Deep Dive

### State Transition Diagram

```
State (node, coupon_used):

(u, 0) ──full_cost──→ (v, 0)
  │
  └──discounted_cost──→ (v, 1)

(u, 1) ──full_cost──→ (v, 1)
```

**Key Rules:**
1. From state `(u, 0)`, we can go to `(v, 0)` or `(v, 1)`
2. From state `(u, 1)`, we can only go to `(v, 1)`
3. Once coupon is used, it cannot be "unused"

### Why This Works

**Optimal Substructure:** If the optimal path uses the coupon on edge `(u,v)`, then:
- The subpath from start to `u` must be optimal without using the coupon
- The subpath from `v` to end must be optimal with the coupon already used

**Greedy Choice:** At each step, Dijkstra's algorithm makes the locally optimal choice, which leads to the globally optimal solution due to the problem's structure.

## Complexity Analysis

### Time Complexity: O((V + E) log V)
- **Standard Dijkstra:** O((V + E) log V)
- **State multiplication:** 2× states per vertex
- **Total:** O(2(V + E) log(2V)) = O((V + E) log V)

### Space Complexity: O(V)
- **Distance array:** O(2V) = O(V)
- **Priority queue:** O(V) in worst case
- **Graph storage:** O(E)

## Advanced Optimizations

### 1. Early Termination
```python
if node == n:
    return cost  # Found optimal path to destination
```

### 2. Bidirectional Search
For very large graphs, run Dijkstra from both ends:
```python
# Forward: dist_forward[node][used]
# Backward: dist_backward[node][used]  
# Meet in the middle and combine results
```

### 3. Memory Optimization
```python
# Use single array with bit manipulation
dist = [INF] * (2 * (n + 1))
# dist[2*node + used] represents dist[node][used]
```

## Common Pitfalls & Debug Tips

### ❌ Wrong: Single Distance Array
```python
# This loses information about coupon state!
dist = [INF] * (n + 1)
```

### ❌ Wrong: Coupon Reuse
```python
# Don't allow transitioning from used back to unused
if used == 1:
    # Can still use coupon - WRONG!
```

### ❌ Wrong: Integer Division
```python
# In some languages, be careful with division
discounted_cost = cost + weight / 2  # Might give float!
discounted_cost = cost + weight // 2  # Correct floor division
```

### ✅ Debug Checklist
1. **State separation:** Two distances per node?
2. **Transition rules:** Can only use coupon once?
3. **Input parsing:** Reading M edges, not N?
4. **Output format:** Minimum of both final states?

## Practice Problems

### Similar State-Space Problems
1. **CSES - Flight Routes:** Find K shortest paths
2. **AtCoder ABC191 E:** Shortest path with teleportation
3. **Codeforces 1473E:** Shortest path with edge modifications
4. **SPOJ EZDIJKST:** Multiple shortest paths with constraints

### Extension Ideas
1. **Multiple Coupons:** What if you have K discount coupons?
2. **Different Discounts:** What if coupons give different discount rates?
3. **Conditional Coupons:** What if coupons only work on certain edge types?

## Conclusion

The Flight Discount problem beautifully demonstrates how classic algorithms can be extended through **state augmentation**. The key insights are:

1. **Expand the state space** to track additional information
2. **Maintain optimal substructure** across state transitions  
3. **Let the algorithm explore** all possibilities naturally

This technique appears frequently in competitive programming and forms the foundation for solving many advanced shortest path variants.

### Key Takeaway
> When a problem adds constraints to a classic algorithm, consider expanding your state space rather than trying to predetermine optimal choices.
