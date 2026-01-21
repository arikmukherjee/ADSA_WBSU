import sys

# ---------------- 0/1 Knapsack (DP) ----------------
def knapsack_dp(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    print("Maximum value:", dp[n][capacity])


# ---------------- Strassen's Matrix Multiplication ----------------
def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, sub_matrix(B12, B22))
    M4 = strassen(A22, sub_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


# ---------------- Matrix Chain Multiplication (DP) ----------------
def matrix_chain_order(p):
    n = len(p) - 1  # number of matrices
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    print("Number of matrices:", n)
    print("Minimum number of multiplications:", dp[0][n - 1])


# ---------------- Maximum Subarray (Kadane’s Algorithm) ----------------
def max_subarray(arr):
    max_current = max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    print("Maximum subarray sum:", max_global)


# ---------------- Menu Driven Program ----------------
def main():
    while True:
        print("\n--- Dynamic Programming Menu ---")
        print("1. 0/1 Knapsack")
        print("2. Strassen's Matrix Multiplication")
        print("3. Matrix Chain Multiplication")
        print("4. Maximum Subarray")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of items: "))
            weights = list(map(int, input("Enter weights: ").split()))
            values = list(map(int, input("Enter values: ").split()))
            capacity = int(input("Enter knapsack capacity: "))
            knapsack_dp(weights, values, capacity)

        elif choice == 2:
            n = int(input("Enter matrix size (power of 2): "))
            print("Enter Matrix A:")
            A = [list(map(int, input().split())) for _ in range(n)]
            print("Enter Matrix B:")
            B = [list(map(int, input().split())) for _ in range(n)]
            C = strassen(A, B)
            print("Resultant Matrix:")
            for row in C:
                print(row)

        elif choice == 3:
            num_matrices = int(input("Enter number of matrices: "))
            print(f"Enter dimensions array (length {num_matrices + 1}):")
            p = list(map(int, input().split()))
            if len(p) != num_matrices + 1:
                print(f"Error: Dimensions array must have {num_matrices + 1} elements.")
                continue
            matrix_chain_order(p)

        elif choice == 4:
            arr = list(map(int, input("Enter array elements: ").split()))
            max_subarray(arr)

        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

