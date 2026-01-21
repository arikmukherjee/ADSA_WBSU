items = [
    (40, 100),  # (value, weight)
    (35, 50),
    (18, 45),
    (4, 20),
    (10, 10),
    (2, 5)
]

W = 100  # capacity

# --- Same helper functions as before ---

def greedy_by_value(items, W):
    idx = list(range(len(items)))
    idx.sort(key=lambda i: items[i][0], reverse=True)
    total_value = 0
    total_weight = 0
    chosen = [0] * len(items)
    for i in idx:
        v, w = items[i]
        if total_weight + w <= W:
            chosen[i] = 1
            total_value += v
            total_weight += w
    return chosen, total_value, total_weight

def greedy_by_weight(items, W):
    idx = list(range(len(items)))
    idx.sort(key=lambda i: items[i][1])  # smallest weight first
    total_value = 0
    total_weight = 0
    chosen = [0] * len(items)
    for i in idx:
        v, w = items[i]
        if total_weight + w <= W:
            chosen[i] = 1
            total_value += v
            total_weight += w
    return chosen, total_value, total_weight

def greedy_by_ratio(items, W):
    idx = list(range(len(items)))
    idx.sort(key=lambda i: items[i][0] / items[i][1], reverse=True)
    total_value = 0
    total_weight = 0
    chosen = [0] * len(items)
    for i in idx:
        v, w = items[i]
        if total_weight + w <= W:
            chosen[i] = 1
            total_value += v
            total_weight += w
    return chosen, total_value, total_weight

def knapsack_dp(items, W):
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        v, w = items[i - 1]
        for cap in range(1, W + 1):
            if w <= cap:
                dp[i][cap] = max(dp[i - 1][cap], dp[i - 1][cap - w] + v)
            else:
                dp[i][cap] = dp[i - 1][cap]

    chosen = [0] * n
    cap = W
    for i in range(n, 0, -1):
        if dp[i][cap] != dp[i - 1][cap]:
            chosen[i - 1] = 1
            cap -= items[i - 1][1]

    total_value = dp[n][W]
    total_weight = sum(items[i][1] for i in range(n) if chosen[i] == 1)
    return chosen, total_value, total_weight

# --- Run all strategies ---
g_value = greedy_by_value(items, W)
g_weight = greedy_by_weight(items, W)
g_ratio = greedy_by_ratio(items, W)
optimal = knapsack_dp(items, W)

# --- Print table manually ---
headers = ["i", "v_i", "w_i", "v_i/w_i",
           "Greedy by value", "Greedy by weight", "Greedy by v_i/w_i", "Optimal solution"]

# Print header row
print("-" * 87)
print(f"| {' | '.join(h.center(15) for h in headers)} |")
print("-" * 87)

# Print each item row
for i in range(len(items)):
    v, w = items[i]
    ratio = round(v / w, 2)
    row = [
        str(i+1).center(15),
        str(v).center(15),
        str(w).center(15),
        str(ratio).center(15),
        str(g_value[0][i]).center(15),
        str(g_weight[0][i]).center(15),
        str(g_ratio[0][i]).center(15),
        str(optimal[0][i]).center(15)
    ]
    print("| " + " | ".join(row) + " |")
print("-" * 87)

# Total value row
total_value_row = [
    "Total value".ljust(15),
    str(sum(items[i][0] for i in range(len(items)))).center(15),
    "".center(15),
    "".center(15),
    str(g_value[1]).center(15),
    str(g_weight[1]).center(15),
    str(g_ratio[1]).center(15),
    str(optimal[1]).center(15)
]
print("| " + " | ".join(total_value_row) + " |")

# Total weight row
total_weight_row = [
    "Total weight".ljust(15),
    "".center(15),
    "".center(15),
    "".center(15),
    str(g_value[2]).center(15),
    str(g_weight[2]).center(15),
    str(g_ratio[2]).center(15),
    str(optimal[2]).center(15)
]
print("| " + " | ".join(total_weight_row) + " |")

print("-" * 87)

