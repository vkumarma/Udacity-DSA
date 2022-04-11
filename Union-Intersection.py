class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


commons = []


def union(llist_1, llist_2):
    if llist_1.size() == 0 and llist_2.size() == 0:
        return
    if llist_1.size() == 0:
        return llist_2
    if llist_2.size() == 0:
        return llist_1

    llist_1_hashtable = {}
    llist_2_hashtable = {}
    previous = None
    current = llist_1.head
    while current:
        if llist_1_hashtable.get(current.value):
            previous.next = current.next
        else:
            llist_1_hashtable[current.value] = True
            previous = current
        current = current.next

    previous = None
    current = llist_2.head
    while current:
        if llist_2_hashtable.get(current.value):
            previous.next = current.next
        else:
            llist_2_hashtable[current.value] = True
            previous = current
        current = current.next

    if llist_1.size() >= llist_2.size():
        previous = None
        current = llist_1.head
        while current:
            if llist_2_hashtable.get(current.value):
                commons.append(current.value)
                if previous == None:
                    llist_1.head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next

        previous.next = llist_2.head
        return llist_1

    elif llist_1.size() < llist_2.size():
        previous = None
        current = llist_2.head
        while current:
            if llist_1_hashtable.get(current.value):
                commons.append(current.value)
                if previous == None:
                    llist_2.head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next

        previous.next = llist_1.head
        return llist_2


def intersection(llist_1, llist_2):
    if len(commons) == 0:
        return None
    new_linked_list = LinkedList()
    new_linked_list.head = Node(commons[0])
    current = new_linked_list.head
    for i in range(1, len(commons)):
        current.next = Node(commons[i])
        current = current.next

    while len(commons) != 0:
        commons.pop()
    return new_linked_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [2, 3, 4]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
print(intersection(linked_list_7, linked_list_8))

# Test case 5

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [1, 2, 4, 5, 6, 7]
element_2 = [3, 4, 5, 6]

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))
print(intersection(linked_list_9, linked_list_10))

# The time complexity for Union is O(n)
# The time complexity for Intersection is O(n)
