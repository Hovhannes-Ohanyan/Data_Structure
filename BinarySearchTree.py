class Node:
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if current.leftChild is None:
                    current.leftChild = Node(data)
                    return

                else:
                    current = current.leftChild

            elif data > current.data:
                if current.rightChild is None:
                    current.rightChild = Node(data)
                    return
                else:
                    current = current.rightChild
            else:
                return

    def delete(self, value):
        def find_min(node):
            while node.leftChild:
                node = node.leftChild
            return node

        def delete_node(root, value):
            if root is None:
                return root

            if value < root.data:
                root.leftChild = delete_node(root.leftChild, value)
            elif value > root.data:
                root.rightChild = delete_node(root.rightChild, value)
            else:
                if root.leftChild is None:
                    return root.rightChild
                elif root.rightChild is None:
                    return root.leftChild

                temp = find_min(root.rightChild)
                root.data = temp.data
                root.rightChild = delete_node(root.rightChild, temp.data)

            return root

        self.root = delete_node(self.root, value)

    def minimum(self):
        current = self.root
        while current.leftChild:
            current = current.leftChild
        return current.data

    def maximum(self):
        current = self.root
        while current.rightChild:
            current = current.rightChild
        return current.data

    def successor(self, value):
        current = self.root
        successor = None
        while current:
            if current.data > value:
                successor = current
                current = current.leftChild
            else:
                current = current.rightChild
        return successor.data if successor else None

    def height(self):
        def calculate_height(node):
            if node is None:
                return -1
            else:
                left_height = calculate_height(node.leftChild)
                right_height = calculate_height(node.rightChild)
                return max(left_height, right_height) + 1

        return calculate_height(self.root)

    def count_nodes(self):
        def count(node):
            if node is None:
                return 0
            return 1 + count(node.leftChild) + count(node.rightChild)

        return count(self.root)

    def search(self, value):
        current = self.root
        while current:
            if value == current.data:
                return True
            elif value < current.data:
                current = current.leftChild
            else:
                current = current.rightChild
        return False

    def pre_order_traversal(self):
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.data)
                stack.append(node.rightChild)
                stack.append(node.leftChild)
        return result

    def in_order_traversal(self):
        result = []
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.leftChild
            current = stack.pop()
            result.append(current.data)
            current = current.rightChild
        return result

    def post_order_traversal(self):
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.data)
                stack.append(node.leftChild)
                stack.append(node.rightChild)
        return result[::-1]


bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)
print(bst.successor(5))
print(bst.minimum())
print(bst.maximum())
print(bst.search(10))
print(bst.in_order_traversal())
print(bst.pre_order_traversal())
print(bst.post_order_traversal())
