import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because we can easily pop off the head or tail
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add the item toe the beginning of the list
        self.storage.add_to_head(value)
        # Increase list size by one since we're adding an item
        self.size += 1

    def dequeue(self):
        # if there are no items in the queue we can't dequeue anything
        if self.size == 0:
            return None
        # In a queue we remove the opposite
        removed_value = self.storage.remove_from_tail()
        # Decrease list size by one since we're removing an item
        self.size -= 1
        return removed_value

    def len(self):
        return self.size
