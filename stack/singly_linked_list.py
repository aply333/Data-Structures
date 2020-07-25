class Node:
    def __init__(self, value = None, target = None):
        self.value = value
        self.next = target
    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def remove_head(self):
        if not self.head:
            return None
        if self.head.next is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next
        return head_value

    def contains(self, value):
        if not self.head:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() == value:
                return True
            current_node = current_node.next
        return False
        
    def get_max(self):
        if not self.head:
            return None
        current = self.head
        max_val = self.head.value
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val