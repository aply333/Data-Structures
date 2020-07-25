"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

    Arrays: Bennefit with arrays, is if you know what you want you can 
            skip straight to it, allowing for a constant time operation.
            When adding to it, you have to copy the previous array which
            makes them a tad less efficient compared to Linked - List

    Linked-List: Group of objects that point not only contain their data but
                also point to the next piece of data in the list.
                Adding data to them can be quicker but even if you know which 
                item you are looking for, you will have to go through every object
                leading up to your target. You can't manipulate that as easily,
                if you remove one element without it breaking the rest of the 
                list. You would need to put some work to fix the list.

"""
class Old_Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) < 1:
            return None
        else:
            return self.storage.pop()


# import sys
# sys.path.append("../singly_linked_list")
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()





# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     def get_value(self):
#         return self.data
#     def get_next(self):
#         return self.next
#     def set_next(self, new_next):
#         self.next = new_next

# class Failed_Stack:
#     def __init__(self):
#         self.size = 0
#         self.head = None
#         self.tail = None

#     def __len__(self):
#         return self.size

#     def push(self, data):
#         self.size += 1
#         new_node = Node(data)
#         if not self.head and not self.tail:  
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node
    
#     def remove_head(self):
#         if self.head is None and self.tail is None:
#             return None
#         self.size -= 1
#         val = self.head.get_value()
#         self.head = self.head.get_next()
#         return val

#     def pop(self):
#         if self.size == 0:
#             return None  
#         self.size -= 1
#         val = self.tail.get_value()
#         print(f"VAL: {val}")
#         current = self.head
#         while current.get_next() is not None:
#             current = current.get_next()
#             print(f"Cycle: {current.data}")
#         current.set_next(None)
#         self.tail = current
#         return val
