"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_value(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, target):
        self.next = target

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def dequeue(self):
        if self.head is None and self.tail is None:
            return None
        else: 
            self.size -= 1
            old_head = self.head.get_value()
            if self.head.get_next() is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next()
            return old_head

class Array_Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size +=1
        self.storage.append(value)

    def dequeue(self):
        if self.size < 1:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)
