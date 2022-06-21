from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()  # referencing to a new node

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffixes = []

        def dfs(children, suffix, suffixes):
            ori_suffix = suffix
            for child in children:
                suffix += child
                new_node = children[child]
                if len(new_node.children) == 0:
                    suffixes.append(suffix)
                    return
                elif new_node.is_word:
                    suffixes.append(suffix)
                dfs(new_node.children, suffix, suffixes)
                suffix = ori_suffix

        dfs(self.children, suffix, suffixes)
        return suffixes


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.insert(char)
            curr_node = curr_node.children[char]  # updating the current node

        curr_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return None
            curr_node = curr_node.children[char]

        return curr_node


#################### Testing ######################
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod", "talking", "talk"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='');

#################################### Console testing ############################
end = False
while not end:
    prefix = input("type prefix and hit enter: ")
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
            end = True
    else:
        print('')