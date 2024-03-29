class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            if not current_node:
                raise IndexError("Position out of bounds")
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            print("List is empty.")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.is_empty():
            print("List is empty.")
            return

        if not self.head.next:
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def delete_at_position(self, position):
        if self.is_empty():
            print("List is empty.")
            return

        if position == 0:
            self.head = self.head.next
            return

        current_node = self.head
        for _ in range(position - 1):
            if not current_node or not current_node.next:
                raise IndexError("Position out of bounds")
            current_node = current_node.next
        current_node.next = current_node.next.next

    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.data == target:
                return True
            current_node = current_node.next
        return False

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("Null")


linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()

linked_list.prepend(0)
linked_list.display()

linked_list.insert_at_position(1.5, 2)
linked_list.display()

linked_list.delete_at_beginning()
linked_list.display()

linked_list.delete_at_end()
linked_list.display()

linked_list.delete_at_position(1)
linked_list.display()

print(linked_list.search(2))
print(linked_list.search(5))
