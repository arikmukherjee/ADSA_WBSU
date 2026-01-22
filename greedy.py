def coin_change():
    print("\n--- COIN CHANGE (Greedy) ---")
    coins = list(map(int, input("Enter coin denominations (space separated): ").split()))
    coins.sort(reverse=True)

    amount = int(input("Enter amount to change: "))

    result = {}
    remaining = amount

    for coin in coins:
        if remaining >= coin:
            count = remaining // coin
            remaining -= coin * count
            result[coin] = count

    print("\nCoins used:")
    for coin, count in result.items():
        print(f"{coin} -> {count} times")

    if remaining != 0:
        print("Remaining amount cannot be changed using given coins.")
    else:
        print("Change completed successfully.")


# 🔹 CHANGED: Knapsack based on your image algorithm
def fractional_knapsack():
    print("\n--- GREEDY KNAPSACK (Based on Ratio Algorithm) ---")
    n = int(input("Enter number of items: "))

    profit = []
    weight = []
    ratio = []

    for i in range(n):
        p = float(input(f"Enter profit of item {i+1}: "))
        w = float(input(f"Enter weight of item {i+1}: "))
        profit.append(p)
        weight.append(w)
        ratio.append(p / w)

    W = float(input("Enter knapsack capacity: "))

    # Step 2: sort by ratio descending
    items = list(zip(profit, weight, ratio))
    items.sort(key=lambda x: x[2], reverse=True)

    totalProfit = 0
    currentWeight = 0

    print("\nSelected Items:")

    # Step 4: select or skip
    for p, w, r in items:
        if currentWeight + w <= W:
            currentWeight += w
            totalProfit += p
            print(f"Selected item (profit={p}, weight={w}, ratio={r:.2f})")
        else:
            print(f"Skipped item (profit={p}, weight={w}, ratio={r:.2f})")

    print("\nTotal Profit:", totalProfit)
    print("Total Weight:", currentWeight)


# -------- MAIN MENU LOOP --------
while True:
    print("\n====== GREEDY ALGORITHMS MENU ======")
    print("1. Coin Change Problem")
    print("2. 0/1 Knapsack ")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        coin_change()
    elif choice == "2":
        fractional_knapsack()
    elif choice == "3":
        print("Exiting program... Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")
