class DequeNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def peek_first(self):
        if self.head:
            return self.head.val
        else:
            raise IndexError("peek first in empty deque")
    
    def peek_last(self):
        if self.tail:
            return self.tail.val
        else:
            raise IndexError("peek last in empty deque")

    def add_first(self):
        pass
    
    def add_last(self):
        pass

    def pop_first(self):
        pass

    def pop_last(self):
        pass

    def __len__(self):
        pass 