"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def set_prev(self, value=None):
        self.prev = value
    
    def set_next(self, value=None):
        self.next = value

    def get_value(self):
        return self.value
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
        
    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head           
            old_head.set_prev(new_node)
            new_node.set_next(old_head)
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        if self.length == 1:
            self.length = 0
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.get_value()
        self.length -= 1
        old_head = self.head
        self.head = self.head.next
        self.head.prev = None
        return old_head.get_value()
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            self.tail.set_next(new_node)
            self.tail = new_node
            self.tail.set_prev(old_tail)
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.length = 0
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        self.length -= 1
        old_tail = self.tail.get_value()
        new_tail = self.tail.prev
        new_tail.set_next(None)
        self.tail = new_tail
        return old_tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.tail == node:
            old_tail = self.tail
            self.tail = old_tail.prev
            self.tail.set_next(None)
            old_tail.set_prev(None)
            old_tail.set_next(self.head)
            self.head.set_prev(old_tail)
            self.head = old_tail
        else:
            current = self.head
            while current:
                if current == node:
                    current.prev.set_next(current.next)
                    current.next.set_prev(current.prev)
                    current.set_next(self.head)
                    self.head.set_prev(current.prev)
                    self.head = current
                    self.head.set_prev(None)
                current = current.next
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head == node:
            old_head = self.head
            self.head = old_head.next
            self.head.set_prev(None)
            old_head.set_next(None)
            old_head.set_prev(self.tail)
            self.tail.set_next(old_head)
            self.tail = old_head
        else:
            current = self.head
            while current:
                if current == node:
                    current.prev.set_next(current.next)
                    current.next.set_prev(current.prev)
                    current.set_prev(self.tail)
                    self.tail.set_next(current)
                    self.tail = current
                    self.tail.set_next(None)
                current = current.next
    
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            pass
        elif self.length == 1:
            self.length = 0
            self.head = None
            self.tail = None
        elif self.head == node:
            self.length -= 1
            self.head = self.head.next
            self.head.set_prev(None)
        else:
            self.length -= 1
            current = self.head
            while current:
                if current.get_value() == node:
                    current.prev.set_next(current.next)
                    current.next.set_prev(current.prev)
                current = current.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        current = self.head
        max_val = self.head.value
        while current:
            if current.get_value() > max_val:
                max_val = current.get_value()
            current = current.next
        return max_val