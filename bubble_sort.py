def bubble_sort(arr):
    n = len(arr)
    # Outer loop to traverse through all array elements
    for i in range(n):
        swapped = False
        # Inner loop to compare adjacent elements
        # The last 'i' elements are already in place
        for j in range(0, n - i - 1):
            # Compare the element at j with the element at j+1
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, 
        # then the list is already sorted and we can stop
        if not swapped:
            break
    return arr

# Example Usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print(f"Sorted array: {sorted_list}")
