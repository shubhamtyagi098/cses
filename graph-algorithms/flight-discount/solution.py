"""
CSES - Flight Discount
Problem: https://cses.fi/problemset/task/1195/

Solution using state-space Dijkstra algorithm.
Time Complexity: O((V + E) log V)
Space Complexity: O(V)
"""

import heapq

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list using dictionary
    graph = {i: [] for i in range(n + 1)}
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
    # dist[node][used_coupon] where used_coupon: 0 = available, 1 = used
    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    
    # Priority queue: (cost, node, used_coupon)
    pq = [(0, 1, 0)]
    dist[1][0] = 0
    
    while pq:
        cost, node, used = heapq.heappop(pq)
        
        # Skip if we've found a better path to this state
        if cost > dist[node][used]:
            continue
        
        # Early termination optimization
        if node == n:
            return cost
            
        # Explore all outgoing edges
        for neighbor, weight in graph[node]:
            
            # Option 1: Take edge at full cost
            new_cost = cost + weight
            if new_cost < dist[neighbor][used]:
                dist[neighbor][used] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, used))
            
            # Option 2: Use coupon on this edge (if available)
            if used == 0:
                discounted_cost = cost + weight // 2
                if discounted_cost < dist[neighbor][1]:
                    dist[neighbor][1] = discounted_cost
                    heapq.heappush(pq, (discounted_cost, neighbor, 1))
    
    # Return minimum cost to reach destination
    return min(dist[n][0], dist[n][1])

print(solve())
