import random
import time
import math

# ---------- search functions ----------

def linear_search(arr, key):
    comparisons = 0
    for index, value in enumerate(arr):
        comparisons += 1
        if value == key:
            return comparisons, index


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == key:
            return comparisons, mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1


# ---------- helper for timing ----------
def measure_time(func, arr, key):
    start = time.perf_counter()
    comparisons, index = func(arr, key)
    end = time.perf_counter()
    return comparisons, index, end - start


# ---------- main program ----------
while True:
    print("\n=== SEARCHING ALGORITHM MENU ===")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "3":
        print("Exiting...")
        break

    if choice not in ("1", "2"):
        print("Invalid choice!")
        continue

    N = int(input("Enter array size (minimum 10000): "))
    if N < 10000:
        print("Array size must be at least 10000!")
        continue

    key = int(input("Enter element to search: "))

    arr = [random.randint(1, 1000000) for _ in range(N)]

    # ---------- Linear Search ----------
    if choice == "1":
        # force key into array
        arr[N // 2] = key

        algo_name = "Linear Search"
        case_name = "All Case"
        theory = f"O(n) = O({N})"
        func = linear_search

    # ---------- Binary Search ----------
    else:
        arr.sort()
        arr[N // 2] = key
        arr.sort()

        algo_name = "Binary Search"
        case_name = "All Cases"
        func = binary_search

        log_exact = math.log2(N)
        log_rounded = math.ceil(log_exact)

        theory = (
            f"O(log₂ n) = O(log₂ {N}) ≈ "
            f"{log_exact:.2f} ≈ {log_rounded} operations"
        )

    # ---------- execution ----------
    actual_comparisons, index, time_taken = measure_time(func, arr, key)

    # ---------- result ----------
    print("\n--------- RESULT ---------")
    print(f"Array Size                 : {N}")
    print(f"Algorithm                  : {algo_name}")
    print(f"Case                        : {case_name}")
    print(f"Element Searched            : {key}")
    print(f"No. of Comparisons          : {actual_comparisons}")
    print(f"Element Found At Index      : {index}")
    print(f"Execution Time              : {time_taken:.10f} seconds")
    print(f"Theoretical Time Complexity : {theory}")
    print("---------------------------\n")

