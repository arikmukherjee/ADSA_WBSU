def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    result = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    if amount != 0:
        print("Exact change not possible using greedy approach.")
    else:
        print("Coins used:", result)
        print("Total coins:", len(result))


def knapsack_greedy(weights, values, capacity):
    n = len(values)
    items = []

    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i], i))

    # Sort items by value/weight ratio (descending)
    items.sort(reverse=True)

    total_value = 0
    selected_items = []

    for item in items:
        if item[1] <= capacity:
            capacity -= item[1]
            total_value += item[2]
            selected_items.append(item[3])

    print("Selected item indices:", selected_items)
    print("Maximum value (Greedy):", total_value)


def main():
    while True:
        print("\n--- Greedy Algorithm Menu ---")
        print("1. Coin Change")
        print("2. 0/1 Knapsack")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of coin denominations: "))
            coins = list(map(int, input("Enter coin denominations: ").split()))
            amount = int(input("Enter amount: "))
            coin_change_greedy(coins, amount)

        elif choice == 2:
            n = int(input("Enter number of items: "))
            weights = list(map(int, input("Enter weights: ").split()))
            values = list(map(int, input("Enter values: ").split()))
            capacity = int(input("Enter knapsack capacity: "))
            knapsack_greedy(weights, values, capacity)

        elif choice == 3:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

