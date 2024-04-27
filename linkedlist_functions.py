class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_linked_list(head):
    curr_node = head
    while curr_node is not None:
        print(curr_node.value)
        curr_node = curr_node.next


def create_linked_list(input_list):
    head = None
    if len(input_list) != 0:
        head = Node(input_list[0])
        current = head
        for i in range(1, len(input_list)):
            current.next = Node(input_list[i])
            current = current.next

    return head


def create_linked_list_with_tail(input_list):
    head = None
    tail = None
    if len(input_list) != 0:
        for e in input_list:
            if head is None:  # at this point both head tail referring to same node
                head = Node(e)  # creating new node
                tail = head
            else:  # creation of second node or rest of the nodes
                tail.next = Node(e)
                tail = tail.next

    # In the end tail is holding reference of the last node in the linked list
    return head


# linked_list_head = create_linked_list([1, 2, 3, 4, 5])
linked_list_head = create_linked_list_with_tail([1, 2, 3, 4, 5, 6])

print_linked_list(linked_list_head)
print(linked_list_head.next.value)
print("\n")


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):  # adding node to the end of the list
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def to_list(self):
        l = []
        current = self.head
        while current is not None:
            l.append(current.value)
            current = current.next
        return l

    def pop_right(self):
        if self.head is None:
            return

        current = self.head
        if current.next is None:
            temp = current
            self.head = None
            return temp.value

        while current.next.next is not None:
            current = current.next

        temp = current.next
        current.next = None
        # current.next = temp.next will also work as temp.next will be None at this point
        return temp.value

    def pop_left(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            return temp.value

        return  # otherwise returns None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1

        return count

    def search(self, value):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next

        raise ValueError("Value not found in the list")

    def insert(self, value, pos):  # inserting value at a position
        # We can use Prev=None and Current=self.head to implement this part.
        if self.head is None:
            self.head = Node(value)
            return

        if pos == 0:
            self.prepend(value)
            return

        current = self.head
        index = 0
        while current.next is not None and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return

            index += 1
            current = current.next

        self.append(value)  # if all else fails add the node to the end of the list

    def remove(self, value):
        # Two pointers: Prev = None and Current = self.head can be used to implement this part
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:  # iterates till reached the last node in the linked list
            if current.next.value == value:  # checking first step in the future
                current.next = current.next.next
                return

            current = current.next

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev

    def reverse_to_list(self):

        prev = None
        for value in self.to_list():
            new_node = Node(value)
            new_node.next = prev
            prev = new_node

        self.head = prev

    def is_cycle(self):
        if self.head is not None:
            slow = self.head
            fast = self.head
            while fast.next is not None:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
                elif fast is None:
                    return False

        return False

    def add_sorted(self, value):  # priority Queue behavior O(n) worst case and O(1) best case
        if self.head is None:
            self.head = Node(value)
            return
        if value <= self.head.value:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            if value <= current.next.value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        current.next = Node(value)


l = LinkedList()
for i in range(6):
    l.add_sorted(i * 2)

print(l.to_list())
l.add_sorted(-1)
l.add_sorted(-1)
l.add_sorted(-1)
l.add_sorted(0)
l.add_sorted(5)

print(l.to_list())
print(l.is_cycle())