import random
import time
import sys
import heapq
import math

sys.setrecursionlimit(30000)

# ---------------- SORTING ALGORITHMS ----------------

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    a = arr.copy()
    quick(a, 0, len(a) - 1)
    return a


def quick(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quick(a, low, p - 1)
        quick(a, p + 1, high)

def partition(a, low, high):
    pivot_index = random.randint(low, high)
    a[pivot_index], a[high] = a[high], a[pivot_index]
    pivot = a[high]

    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i+1], a[high] = a[high], a[i+1]
    return i + 1



def heap_sort(arr):
    a = arr.copy()
    heapq.heapify(a)
    return [heapq.heappop(a) for _ in range(len(a))]


# ---------------- TIME MEASURE ----------------

def measure_sort_time(func, arr):
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return end - start


# ---------------- MAIN PROGRAM ----------------

while True:
    print("\n====== SORTING ALGORITHM MENU ======")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    print("7. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "":
        continue

    if choice == "7":
        print("Exiting...")
        break

    if choice not in {"1", "2", "3", "4", "5", "6"}:
        print("Invalid choice!")
        continue

    N = int(input("Enter number of elements: "))
    arr = [random.randint(1, 1000000) for _ in range(N)]

    # ---------- ALGORITHM & CASE ----------
    if choice == "1":  # Bubble Sort
        print("\nChoose Case:")
        print("a. Best Case")
        print("b. Average/Worst Case")
        case = input("Enter choice (a/b): ").strip().lower()
        if case == "a":
            arr.sort()
            theory = f"O(n) = O({N}) ≈ {N} operations"
            case_name = "Best Case"
        else:
            random.shuffle(arr)
            theory = f"O(n²) = O({N*N}) operations"
            case_name = "Average/Worst Case"
        func = bubble_sort
        algo = "Bubble Sort"

    elif choice == "2":  # Selection Sort
        random.shuffle(arr)
        theory = f"O(n²) = O({N*N}) operations"
        case_name = "All Cases"
        func = selection_sort
        algo = "Selection Sort"

    elif choice == "3":  # Insertion Sort
        print("\nChoose Case:")
        print("a. Best Case")
        print("b. Average/Worst Case")
        case = input("Enter choice (a/b): ").strip().lower()
        if case == "a":
            arr.sort()
            theory = f"O(n) = O({N}) ≈ {N} operations"
            case_name = "Best Case"
        else:
            random.shuffle(arr)
            theory = f"O(n²) = O({N*N}) operations"
            case_name = "Average/Worst Case"
        func = insertion_sort
        algo = "Insertion Sort"

    elif choice == "4":  # Merge Sort
        random.shuffle(arr)
        log_val = math.log2(N)
        ops = int(N * log_val)
        theory = (
            f"O(n log₂ n) = O({N} × {log_val:.2f}) "
            f"≈ {ops} operations"
        )
        case_name = "All Cases"
        func = merge_sort
        algo = "Merge Sort"

    elif choice == "5":  # Quick Sort
        print("\nChoose Case:")
        print("a. Average Case")
        print("b. Worst Case")
        case = input("Enter choice (a/b): ").strip().lower()
        if case == "a":
            random.shuffle(arr)
            log_val = math.log2(N)
            ops = int(N * log_val)
            theory = (
                f"O(n log₂ n) = O({N} × {log_val:.2f}) "
                f"≈ {ops} operations"
            )
            case_name = "Average Case"
        else:
            arr.sort()
            theory = f"O(n²) = O({N*N}) operations"
            case_name = "Worst Case"
        func = quick_sort
        algo = "Quick Sort"

    else:  # Heap Sort
        random.shuffle(arr)
        log_val = math.log2(N)
        ops = int(N * log_val)
        theory = (
            f"O(n log₂ n) = O({N} × {log_val:.2f}) "
            f"≈ {ops} operations"
        )
        case_name = "All Cases"
        func = heap_sort
        algo = "Heap Sort"

    # ---------- SORT ----------
    sort_time = measure_sort_time(func, arr)

    # ---------- FINAL OUTPUT ----------
    print("\n================ FINAL RESULT ================\n")
    print(f"Sorting Algorithm           : {algo}")
    print(f"Case                        : {case_name}")
    print(f"Array Size (n)              : {N}")
    print(f"Execution Time              : {sort_time:.6f} seconds")
    print(f"Theoretical Time Complexity : {theory}")
    print("=============================================\n")

    input("Press Enter to return to menu...")
