def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if amount >= coin:
            num = amount // coin
            count += num
            amount -= num * coin

    return count if amount == 0 else -1


# -------- USER INPUT --------
n = int(input("Enter number of coin types: "))
coins = list(map(int, input("Enter coin values separated by space: ").split()))
amount = int(input("Enter the amount: "))

dp_result = coin_change_dp(coins, amount)
greedy_result = coin_change_greedy(coins, amount)

print("\n--- Results ---")
print("DP (Minimum coins):", dp_result)
print("Greedy (Minimum coins):", greedy_result)

