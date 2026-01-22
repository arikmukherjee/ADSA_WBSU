import sys

# ---------------- 1. 0/1 Knapsack ----------------
def knapsack():
    n = int(input("Enter number of items: "))
    wt = []
    val = []

    for i in range(n):
        wt.append(int(input(f"Enter weight of item {i+1}: ")))
        val.append(int(input(f"Enter value of item {i+1}: ")))

    W = int(input("Enter knapsack capacity: "))

    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    print("Maximum value in Knapsack =", dp[n][W])

# ---------------- 2. LCS ----------------
def lcs():
    X = input("Enter first string: ")
    Y = input("Enter second string: ")

    m = len(X)
    n = len(Y)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print("Length of LCS =", dp[m][n])

# ---------------- 3. Matrix Chain Multiplication ----------------
def matrix_chain():
    n = int(input("Enter number of matrices: "))
    p = []

    print("Enter dimensions:")
    for i in range(n+1):
        p.append(int(input(f"p[{i}] = ")))

    m = [[0]*n for _ in range(n)]

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i+L-1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                m[i][j] = min(m[i][j], cost)

    print("Minimum number of multiplications =", m[0][n-1])

# ---------------- 4. Kadane’s Algorithm ----------------
def kadane():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)

    print("Maximum subarray sum =", max_so_far)

# ---------------- 5. Strassen’s Matrix Multiplication ----------------
def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

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

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C

def strassen_menu():
    n = int(input("Enter matrix size (power of 2): "))

    print("Enter Matrix A:")
    A = [list(map(int, input().split())) for _ in range(n)]

    print("Enter Matrix B:")
    B = [list(map(int, input().split())) for _ in range(n)]

    C = strassen(A, B)

    print("Result Matrix:")
    for row in C:
        print(row)

# ---------------- MAIN MENU ----------------
while True:
    print("\n===== MENU =====")
    print("1. 0/1 Knapsack")
    print("2. LCS")
    print("3. Matrix Chain Multiplication")
    print("4. Maximum Subarray (Kadane)")
    print("5. Strassen's Matrix Multiplication")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        knapsack()
    elif choice == 2:
        lcs()
    elif choice == 3:
        matrix_chain()
    elif choice == 4:
        kadane()
    elif choice == 5:
        strassen_menu()
    elif choice == 6:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Try again.")
