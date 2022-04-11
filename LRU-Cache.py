class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next

    def remove(self, node):
        if node == self.head:
            if self.head.next is None:
                self.head = self.head.next
                self.tail = self.head
            else:
                self.head = self.head.next
            node = None
            return
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            node = None
            return
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            node = None
            return


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = {}
        self.linked_list = DoublyLinkedList()
        self.num_entries = 0

    def get(self, key):
        if self.hashtable.get(key):  # if key exists then return key's value and append it.
            node = self.hashtable[key]
            self.linked_list.remove(node)
            self.linked_list.append(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        new_node = Node(key, value)
        if self.hashtable.get(key):  # if key already exists then update key's value
            already_exists = self.hashtable[key]
            self.linked_list.remove(already_exists)
        elif self.num_entries < self.capacity:
            self.num_entries += 1
        else:  # if num_entries > capacity then delete the LRU(least recently used key) referenced by head.
            k = self.linked_list.head.key
            del self.hashtable[k]
            self.linked_list.remove(self.linked_list.head)

        self.hashtable[key] = new_node
        self.linked_list.append(new_node)


# Hashtable and doubly linked list used to implement LRU-Cache
# O(1) Time Complexity for both put and get functions
# O(n) Space Complexity
# head of linked list acts as a LRU(least recently used)
# tail of linked list acts as a MRU(most recently used)
# hashtable key holds node as its value
# Doubly Linked list is used to have a O(1) removal of a node

a = ["put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "put",
     "get", "put", "get"]
b = [[7, 28], [7, 1], [8, 15], [6], [10, 27], [8, 10], [8], [6, 29], [1, 9], [6], [10, 7], [1], [2], [13], [8, 30],
     [1, 5], [1], [13, 2], [12]]

our_cache = LRUCache(10)
for i in range(len(a)):
    if a[i] == "put":
        print(our_cache.put(b[i][0], b[i][1]))
    else:
        print(our_cache.get(b[i][0]))
