import random
import math

MIN_RANGE = 10
MAX_RANGE = 999999
MAX_INPUT_SIZE = 100000


# COUNTER FOR EMPIRICAL ANALYSIS
class Counter:
    def __init__(self):
        self.time_ops = 0   # counts comparisons


# LINEAR SEARCH
def linear_search(arr, target, counter):
    for i in range(len(arr)):
        counter.time_ops += 1
        if arr[i] == target:
            return i
    return -1


# BINARY SEARCH
def binary_search(arr, target, counter):
    low, high = 0, len(arr) - 1

    while low <= high:
        counter.time_ops += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# COMPLEXITY REPORT (SPACE COMPLETELY REMOVED)
def complexity_report(name, counter, n):
    print(f"\n--- {name} COMPLEXITY ANALYSIS ---")
    print(f"Number of Comparisons: {counter.time_ops}")

    if name == "Linear Search":
        print(f"Theoretical Time Complexity: O(n) = {n}")
    else:
        print(f"Theoretical Time Complexity: O(log₂ n) = {round(math.log2(n), 2)}")


# ARRAY GENERATION
def generate_array(n, choice):
    if choice == 1:
        return list(range(n))
    else:
        return random.sample(range(MIN_RANGE, MAX_RANGE + 1), n)


# MAIN PROGRAM
def main():
    while True:
        print("\nSEARCHING TECHNIQUES")
        print("0. Exit")
        print("1. Linear Search")
        print("2. Binary Search")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting program...")
            break

        if choice not in [1, 2]:
            print("Invalid choice!")
            continue

        n = int(input("Enter number of elements (max 100000): "))
        if n <= 0 or n > MAX_INPUT_SIZE:
            print("Invalid input size!")
            continue

        print("\nARRAY INPUT METHOD")
        print("1. Values from 0 to n-1")
        print("2. Random values")

        input_choice = int(input("Enter your choice: "))

        arr = generate_array(n, input_choice)

        if choice == 2:
            arr.sort()

        print("\nArray:")
        print(arr)

        target = int(input("\nEnter element to search: "))

        counter = Counter()

        if choice == 1:
            index = linear_search(arr, target, counter)
            algo_name = "Linear Search"
        else:
            index = binary_search(arr, target, counter)
            algo_name = "Binary Search"

        print("\nSearch Result:")
        if index != -1:
            print(f"Element found at index {index}")
        else:
            print("Element not found")

        complexity_report(algo_name, counter, n)


main()
