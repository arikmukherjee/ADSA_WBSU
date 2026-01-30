import sys
# ---------------- 1. 0/1 Knapsack ----------------
def knapsack():
    n = int(input("Enter number of items: "))
    wt = []
    val = []

    for i in range(n):
        val.append(int(input(f"Enter value of item {i+1}: ")))
        wt.append(int(input(f"Enter weight of item {i+1}: ")))
        

    W = int(input("Enter knapsack capacity: "))

    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(
                    val[i-1] + dp[i-1][w-wt[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    # -------- RESULT OUTPUT --------
    print("\nSelected Items:")

    selected = [0] * n
    w = W

    # Backtracking to find selected items
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected[i-1] = 1
            w -= wt[i-1]

    total_profit = 0
    total_weight = 0

    for i in range(n):
        if selected[i]:
            total_profit += val[i]
            total_weight += wt[i]
            print(f"Selected item (profit={val[i]}, weight={wt[i]})")
        else:
            print(f"Skipped item (profit={val[i]}, weight={wt[i]})")

    print(f"\nTotal Profit: {total_profit}")
    print(f"Total Weight: {total_weight}")


# ---------------- LCS (Longest Common Subsequence) ----------------
def lcs():
    X = input("Enter first string: ")
    Y = input("Enter second string: ")

    m = len(X)
    n = len(Y)

    # DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Build dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtracking to find LCS string
    i, j = m, n
    lcs_str = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()
    lcs_string = ''.join(lcs_str)

    print("\nLCS:", lcs_string)
    print("Length of LCS:", dp[m][n])


# ---------------- MATRIX CHAIN MULTIPLICATION ----------------
def matrix_chain():
    n = int(input("Enter number of matrices: "))

    p = []
    print("Enter dimensions:")
    for i in range(n + 1):
        p.append(int(input(f"p[{i}] = ")))

    # m[i][j] = minimum cost of multiplying matrices Ai..Aj
    m = [[0 for _ in range(n)] for _ in range(n)]

    # s[i][j] = index at which optimal split occurs
    s = [[0 for _ in range(n)] for _ in range(n)]

    # L = chain length
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    print("\nMinimum number of multiplications =", m[0][n - 1])

    print("Optimal Parenthesization:", end=" ")
    print_parenthesis(s, 0, n - 1)
    print()


# -------- PRINT OPTIMAL PARENTHESIZATION --------
def print_parenthesis(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_parenthesis(s, i, s[i][j])
        print_parenthesis(s, s[i][j] + 1, j)
        print(")", end="")





# ---------------- MAXIMUM SUBARRAY (KADANE'S ALGORITHM) ----------------
def kadane():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

    max_so_far = arr[0]
    curr_max = arr[0]

    start = 0
    end = 0
    temp_start = 0

    for i in range(1, n):
        if arr[i] > curr_max + arr[i]:
            curr_max = arr[i]
            temp_start = i
        else:
            curr_max = curr_max + arr[i]

        if curr_max > max_so_far:
            max_so_far = curr_max
            start = temp_start
            end = i

    print("\nMaximum Subarray Sum =", max_so_far)
    print("Maximum Subarray =", arr[start:end+1])




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
    print("\n===== DP MENU =====")
    print("0. Exit")
    print("1. 0/1 Knapsack")
    print("2. LCS")
    print("3. Matrix Chain Multiplication")
    print("4. Maximum Subarray (Kadane Algorithm)")
    print("5. Strassen's Matrix Multiplication")
    

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
    elif choice == 0:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice")
