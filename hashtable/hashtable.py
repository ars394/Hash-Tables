class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity

    def fnv1(self, key):
        fnv_hash = 14695981039346656037

        enc_key = key.encode()
        for e in enc_key:
            fnv_hash = fnv_hash * 1099511628211
            fnv_hash = fnv_hash ^ e
        return fnv_hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)
        node = self.table[index] 
        if node == None:
            self.table[index] = HashTableEntry(key, value)
        elif node.key == key:
            node.value = value
        else:
            while node != None:
                
                if node.key == key:
                    node.value = value
                    return
                elif node.next == None:
                    node.next = HashTableEntry(key, value)
                    return
                node = node.next


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        node = self.table[index]
        prev = None 
        if node == None:
            return None
        elif node.key == key:
            if node.next == None:
                self.table[index] = None
        else:
            while node.next != None:
                prev = node
                node = node.next
                if node.key == key:
                    prev.next = node.next
                    return node
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        node = self.table[index] 
        if node == None:
            return None
        elif node.key == key:
            print('elif', node.value, node.next)
            return node.value
            
        else:
            while node != None:
                node = node.next
                if node == None:
                    return None
                if node.key == key:
                    print(node.value)
                    return node.value
                

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")