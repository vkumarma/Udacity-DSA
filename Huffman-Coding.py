import sys


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.next = None


class LinkedList:  # Linked list acts as a priority queue in this algorithm
    def __init__(self):
        self.head = None  # head of linked list refers to the highest priority node.

    def append(self, node):  # appending to a sorted list worst case:O(n), bestcase:O(1).
        if self.head is None:
            self.head = node
            return
        if node.freq < self.head.freq:
            node.next = self.head
            self.head = node
            return
        current = self.head
        while current.next is not None and current.next.freq <= node.freq:
            current = current.next
        node.next = current.next
        current.next = node

    def pop(self):  # returns highest priority or node/character with lowest frequency.
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp


frequency_table = {}  # How frequent is some character in the string/message


def huffman_encoding(data):
    if data == "":
        return None, None
    encoded_string = ""
    for char in data:
        frequency_table[char] = 1 + frequency_table.get(char, 0)

    linked_list = LinkedList()  # priority queue == linked_list
    for key in frequency_table:  # O(52) constant time
        new_node = Node(key, frequency_table[key])
        linked_list.append(new_node)  # O(n) in worst case and O(1) in best case

    while linked_list.head.next is not None:  # iterate till only one node left in priority queue.
        left_child = linked_list.pop()
        right_child = linked_list.pop()
        root_node = Node(None, None)  # internal node of the tree
        root_node.freq = left_child.freq + right_child.freq
        root_node.left = left_child
        root_node.right = right_child
        linked_list.append(root_node)

    huffman_tree = linked_list.pop()  # root node of the tree
    s = ""

    def dfs(root, d, s):  # traversing through the root to the leaf node. left node = 0, right node = 1
        old_s = s
        if root.left is None and root.right is None:  # if lead node
            d[root.char] = s
        else:
            if root.left is not None:
                s += "0"
                dfs(root.left, d, s)
                s = old_s

            if root.right is not None:
                s += "1"
                dfs(root.right, d, s)
                s = old_s

        return

    dfs(huffman_tree, frequency_table, s)
    if (huffman_tree.left == None and huffman_tree.right == None):
        frequency_table[huffman_tree.char] = str(1)

    for char in data:
        encoded_string += frequency_table[char]

    # print(frequency_table)
    return encoded_string, huffman_tree


def huffman_decoding(data, tree):
    if tree == None:
        return
    decoded_string = ""
    current = tree  # represents root node of the tree
    for bit in data:
        if bit == "0":  # move left
            if current.left is not None:
                current = current.left
        else:  # bit == "1" move right
            if current.right is not None:
                current = current.right

        if current.left is None and current.right is None:  # if reached the leaf node
            decoded_string += current.char
            current = tree  # start from the root again


    return decoded_string


if __name__ == "__main__":
    inputs = ["The Bird is the Word", "someone@gmail.com" , "aaaaaaaa", ""]
    for elem in inputs:
        a_great_sentence = elem

        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)
        if encoded_data != None:
            print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)
        if decoded_data != None:
            print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print("The content of the encoded data is: {}\n".format(decoded_data))

        #############################################################################################
        if tree != None:
            print("message_size_in_bytes | encoded_message_size_in_bytes | decoded_message_size_in_bytes")
            print("         ", sys.getsizeof(a_great_sentence), "                      ", sys.getsizeof(int(encoded_data, base=2)),
              "                             ", sys.getsizeof(decoded_data))

        frequency_table = {}

# Encoding Time complexity:
# Worst case time complexity for encoding will be O(n^2) because using linked list to determine highest
# priority, and in worst case appending would take O(n), and in best case O(1). Also since, have to
# iterate over n items.Therefore, worst case O(n^2) and best case O(n) to build the tree. Also since
# traversing through all the nodes in the tree it is also gonna take O(n). Thus
# Worst case: O(n^2), Best case:O(n), and Average case: O(n) (I believe)

# Decoding Time complexity:
# Average case: O(number of bits) because traversing through the root to the leaf node for all bits.

# Most frequent character is represented by fewer bits.

