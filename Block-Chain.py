import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(
            " | ") + str(self.hash)


class Blockchain:
    def __init__(self):
        self.head = None
        self.d = {}
        self.l = []

    def add_block(self, block):
        if block.data is None or block.data == "":
            return
        if self.head is None:
            self.d[block.hash] = block
            self.head = block
        else:
            self.d[block.hash] = block
            block.previous_hash = self.head.hash
            self.head = block

        self.l.append(block)

    def print_block_chain(self):
        original_head = self.head
        cur_head = self.head
        out_string = ""
        while cur_head:
            if cur_head != original_head:
                out_string += "->"
            out_string += str(cur_head.data)
            if self.d.get(cur_head.previous_hash):
                cur_head = self.d[cur_head.previous_hash]
            else:
                cur_head = None
        return out_string


def test(input):
    block_chain = Blockchain()
    for data in input:
        time_stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M %Y/%m/%d")
        block = Block(time_stamp, data, None)
        block_chain.add_block(block)

    print(block_chain.print_block_chain())
    for entry in block_chain.l:
        print(entry)


test(["Chain", "Block", "a", "is", "This"])
test([""])
test(["Block", "a", "is"])
test([])

# O(1) time complexity for adding to the linked list
# hashtable used where block's hash acts as a key and block as its value
# Every block refers to previous block's hash


