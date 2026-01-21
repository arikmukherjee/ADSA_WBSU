from collections import deque

# ---------- NODE CLASS ----------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ---------- BST CLASS ----------
class BST:
    def __init__(self):
        self.root = None

    # ---------- INSERT ----------
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    # ---------- DELETE ----------
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # ---------- BFS SEARCH ----------
    def bfs_search(self, key):
        if not self.root:
            return False
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.data == key:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    # ---------- DFS SEARCH ----------
    def dfs_search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        return self.dfs_search(root.left, key) or self.dfs_search(root.right, key)

    # ---------- TRAVERSALS ----------
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

# ---------- MAIN MENU ----------
bst = BST()

while True:
    print("\n--- BST MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Traversal")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # ---------- INSERT ----------
    if choice == 1:
        vals = input("Enter value(s) to insert (space separated): ").split()
        for val in vals:
            try:
                bst.root = bst.insert(bst.root, int(val))
            except ValueError:
                print(f"Ignored invalid value: {val}")

    # ---------- DELETE ----------
    elif choice == 2:
        vals = input("Enter value(s) to delete (space separated): ").split()
        for val in vals:
            try:
                bst.root = bst.delete(bst.root, int(val))
            except ValueError:
                print(f"Ignored invalid value: {val}")

    # ---------- SEARCH ----------
    elif choice == 3:
        if bst.root is None:
            print("BST is empty!")
            continue
        print("\nSearch Method:")
        print("1. BFS")
        print("2. DFS")
        try:
            ch = int(input("Enter choice: "))
            key = int(input("Enter value to search: "))
        except ValueError:
            print("Invalid input! Must be integers.")
            continue

        if ch == 1:
            print("Found" if bst.bfs_search(key) else "Not Found")
        elif ch == 2:
            print("Found" if bst.dfs_search(bst.root, key) else "Not Found")
        else:
            print("Invalid choice!")

    # ---------- TRAVERSALS ----------
    elif choice == 4:
        if bst.root is None:
            print("BST is empty!")
            continue
        print("\nTraversal Type:")
        print("1. Inorder")
        print("2. Preorder")
        print("3. Postorder")
        try:
            t = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if t == 1:
            bst.inorder(bst.root)
        elif t == 2:
            bst.preorder(bst.root)
        elif t == 3:
            bst.postorder(bst.root)
        else:
            print("Invalid choice!")
        print()

    # ---------- EXIT ----------
    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

