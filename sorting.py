import random
import math
import sys
sys.setrecursionlimit(10**7)

MIN_RANGE = 10
MAX_RANGE = 999999
MAX_INPUT_SIZE = 100000


# COUNTER FOR EMPIRICAL ANALYSIS
class Counter:
    def __init__(self):
        self.time_ops = 0
        self.comparisons = 0


# ---------------- SORTING ALGORITHMS ---------------- #

def bubble_sort(arr, counter):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            counter.comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter.time_ops += 1
    return arr


def insertion_sort(arr, counter):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            counter.comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr


def selection_sort(arr, counter):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            counter.comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        counter.time_ops += 1
    return arr


def merge(left, right, counter):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        counter.comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr, counter):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], counter)
    right = merge_sort(arr[mid:], counter)

    return merge(left, right, counter)


def partition(arr, low, high, counter):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        counter.comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            counter.time_ops += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    counter.time_ops += 1
    return i + 1


def quick_sort(arr, low, high, counter):
    if low < high:
        pi = partition(arr, low, high, counter)
        quick_sort(arr, low, pi - 1, counter)
        quick_sort(arr, pi + 1, high, counter)


# ---------------- COMPLEXITY REPORT ---------------- #

def complexity_report(name, case, counter, n):
    print(f"\n--- {name} ({case}) COMPLEXITY ANALYSIS ---")
    print(f"Number of Comparisons: {counter.comparisons}")
    print(f"Number of Swaps: {counter.time_ops}")

    if name in ["Bubble Sort", "Insertion Sort"]:
        if case == "Best Case":
            print(f"Theoretical Time Complexity: O(n) = {n}")
        else:
            print(f"Theoretical Time Complexity: O(n²) = {n ** 2}")

    elif name == "Selection Sort":
        print(f"Theoretical Time Complexity: O(n²) = {n ** 2}")

    elif name == "Merge Sort":
        print(f"Theoretical Time Complexity: O(n log₂ n) = {round(n * math.log2(n), 2)}")

    elif name == "Quick Sort":
        if case == "Worst Case":
            print(f"Theoretical Time Complexity: O(n²) = {n ** 2}")
        else:
            print(f"Theoretical Time Complexity: O(n log₂ n) = {round(n * math.log2(n), 2)}")


# ---------------- MAIN PROGRAM ---------------- #

def main():
    while True:
        print("\nSORTING ALGORITHMS")
        print("0. Exit")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Selection Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting program...")
            break

        n = int(input("Enter number of elements (max 100000): "))
        if n <= 0 or n > MAX_INPUT_SIZE:
            print("Invalid input size!")
            continue

        counter = Counter()

        if choice in [1, 2]:
            print("\n1. Best Case")
            print("2. Average / Worst Case")
            case_choice = int(input("Enter case: "))

            if case_choice == 1:
                arr = list(range(n))
                case = "Best Case"
            else:
                arr = random.sample(range(MIN_RANGE, MAX_RANGE + 1), n)
                case = "Average / Worst Case"

            if choice == 1:
                result = bubble_sort(arr.copy(), counter)
                algo = "Bubble Sort"
            else:
                result = insertion_sort(arr.copy(), counter)
                algo = "Insertion Sort"

        elif choice == 3:
            arr = random.sample(range(MIN_RANGE, MAX_RANGE + 1), n)
            result = selection_sort(arr.copy(), counter)
            algo = "Selection Sort"
            case = "All Cases"

        elif choice == 4:
            arr = random.sample(range(MIN_RANGE, MAX_RANGE + 1), n)
            result = merge_sort(arr.copy(), counter)
            algo = "Merge Sort"
            case = "All Cases"

        elif choice == 5:
            print("\n1. Worst Case")
            print("2. Best / Average Case")
            case_choice = int(input("Enter case: "))

            if case_choice == 1:
                arr = list(range(n))
                case = "Worst Case"
            else:
                arr = random.sample(range(MIN_RANGE, MAX_RANGE + 1), n)
                case = "Best / Average Case"

            result = arr.copy()
            quick_sort(result, 0, n - 1, counter)
            algo = "Quick Sort"

        else:
            print("Invalid choice!")
            continue

        print("\nSorted Array:")
        print(result)

        complexity_report(algo, case, counter, n)


main()
