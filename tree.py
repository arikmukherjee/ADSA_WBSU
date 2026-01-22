import math
from collections import deque

# ===============================
# NODE DEFINITION
# ===============================
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ===============================
# BST CLASS
# ===============================
class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    # Insert
    def insert(self, data):
        self.root = self._insert(self.root, data)
        self.count += 1

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root

    # Delete
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self._delete(root.left, key)
        elif key > root.data:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            temp = self._min_value(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)
        return root

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node

    # Traversals
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# ===============================
# BFS SEARCH
# ===============================
def bfs_search(root, key):
    if not root:
        return False, 0

    queue = deque([root])
    steps = 0

    while queue:
        node = queue.popleft()
        steps += 1

        if node.data == key:
            return True, steps

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False, steps


# ===============================
# DFS SEARCH
# ===============================
def dfs_search(root, key):
    stack = [root]
    steps = 0

    while stack:
        node = stack.pop()
        steps += 1

        if node is None:
            continue

        if node.data == key:
            return True, steps

        stack.append(node.right)
        stack.append(node.left)

    return False, steps


# ===============================
# COMPLEXITY DISPLAY
# ===============================
def show_search_complexity(n):
    print("\nTime Complexity:")
    print("Best Case    : O(1)")
    print("Average Case : O(log n)")
    print("Worst Case   : O(n)")
    if n > 0:
        print(f"log2(n) = {math.log2(n):.2f}")
    print(f"n = {n}")


def show_traversal_complexity(n):
    print("\nTraversal Time Complexity:")
    print("O(n)")
    print(f"Operations = {n}")


# ===============================
# MAIN MENU
# ===============================
bst = BST()

while True:
    print("\nBST")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Traversal")
    print("0. Exit")

    choice = input("Enter choice: ")

    # INSERT
    if choice == '1':
        n = int(input("Enter number of elements: "))
        for i in range(n):
            val = int(input(f"Enter element {i+1}: "))
            bst.insert(val)
        print("Insertion completed.")

    # DELETE
    elif choice == '2':
        key = int(input("Enter value to delete: "))
        bst.delete(key)
        print("Delete operation completed.")

    # SEARCH
    elif choice == '3':
        print("\nSearch Options")
        print("1. BFS")
        print("2. DFS")
        sch = input("Enter choice: ")

        key = int(input("Enter value to search: "))

        if sch == '1':
            found, steps = bfs_search(bst.root, key)
            method = "BFS"
        elif sch == '2':
            found, steps = dfs_search(bst.root, key)
            method = "DFS"
        else:
            print("Invalid search option.")
            continue

        print(f"\nSearch Method: {method}")
        print("Result:", "Found" if found else "Not Found")
        print(f"Computational steps taken: {steps}")
        show_search_complexity(bst.count)

    # TRAVERSAL
    elif choice == '4':
        print("\nTraversal Options")
        print("1. Preorder")
        print("2. Postorder")
        print("3. Inorder")
        tr = input("Enter choice: ")

        if tr == '1':
            print("Preorder Traversal:")
            bst.preorder(bst.root)
        elif tr == '2':
            print("Postorder Traversal:")
            bst.postorder(bst.root)
        elif tr == '3':
            print("Inorder Traversal:")
            bst.inorder(bst.root)
        else:
            print("Invalid traversal option.")
            continue

        show_traversal_complexity(bst.count)

    # EXIT
    elif choice == '0':
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
