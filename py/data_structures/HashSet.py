class ChainingNode:
    def __init__(self,val):
        self.val = val
        self.next = None 

class HashSet:
    """
    This class represents the data structure called a Hash Set designed specifically to accept integer values, 
    that deals with hash collisons through chaining with linked lists. 
    """ 
    def __init__(self, init_capacity = 1000, load_factor = 0.75): 
        # A static array is the base data structure of a Hash Set 
        self._buckets = [None]*init_capacity
        self._design_load_factor = load_factor
        self._curr_items_hashed = 0  

    def add(self, val): 
        """
        Inserts the input argument, expected to be an integer, into the hash set. If by adding the element, the
        design load factor is exceeded, rehashing is done. 
        """ 
        hash_val = self._hashing_algorithm(val)
        node_wrapper_val = ChainingNode(val)
        if not self._buckets[hash_val]:
            self._buckets[hash_val] = node_wrapper_val
        else:
            node = self._buckets[hash_val] 
            prev = None 
            while node:
                # unique collection of items - if we're adding same item twice, then only one of them counts
                if node.val == val:
                    return 
                else:
                    prev = node
                    node = node.next 
            
            prev.next = node_wrapper_val

        # adding items to hash set increases current load factor, and if the load factor is >= then
        # the design load factor, we rehash to keep the time complexity of the hash set methods low 
        self._curr_items_hashed += 1
        curr_load_factor = (self._curr_items_hashed)/len(self._buckets)
        if curr_load_factor >= self._design_load_factor:
            self._rehash()

    def _rehash(self):
        saved_version_old_buckets = self._buckets
        self._buckets = (len(self._buckets)*2)*[None]
        self._curr_items_hashed = 0 
        for node in saved_version_old_buckets:
            while node:
                self.add(node.val)
                node = node.next 


    def contains(self, val):
        """
        Returns a boolean indicating whether or not hash set contains val 
        """
        hash_val = self._hashing_algorithm(val)
        node = self._buckets[hash_val]
        while node:
            if node.val == val:
                return True
            else:
                node = node.next 
        return False 

    
    def remove(self, val):
        hash_val = self._hashing_algorithm(val)
        self._curr_items_hashed -= 1 
        node = self._buckets[hash_val]
        prev = None 
        while node:
            if node.val == val:
                # edge case - deleting head of linked list from bucket
                # means the new head will be the node after the head node (which can be None)
                if not prev:
                    self._buckets[hash_val] = node.next 
                else:
                    savedNext = node.next 
                    prev.next = savedNext
                return 
            else:
                prev = node
                node = node.next 
    
    def _hashing_algorithm(self, val):
        return val % len(self._buckets)



    
