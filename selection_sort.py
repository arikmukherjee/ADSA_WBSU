def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example Usage:
my_list = [64, 25, 12, 22, 11]
print(f"Original list: {my_list}")
sorted_list = selection_sort(my_list)
print(f"Sorted list: {sorted_list}")
