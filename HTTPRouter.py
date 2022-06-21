class RouteTrie:
    def __init__(self, handler, no_handler):
        self.root = RouteTrieNode(handler)
        self.handler_none = no_handler

    def insert(self, path_list, handler):
        curr_node = self.root
        if len(path_list) < 2 and (path_list[0] == "/" or path_list[1] == ""):
            curr_node.insert(path_list[0])
            return

        for elem in path_list:
            if elem not in curr_node.children:
                curr_node.insert(elem)
            curr_node = curr_node.children[elem]
        curr_node.handler = handler

    def find(self, path_list):
        curr_node = self.root
        if len(path_list) > 1:
            for elem in path_list:
                curr_node = curr_node.children.get(elem)

            if curr_node is None:
                return self.handler_none

            if curr_node.handler is None:
                return self.handler_none

        return curr_node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, elem):
        self.children[elem] = RouteTrieNode()


class Router:
    def __init__(self, handler, no_handler):
        self.route_trie = RouteTrie(handler, no_handler)

    def add_handler(self, path, handler):
        path_list = self.split_path(path)
        self.route_trie.insert(path_list, handler)

    def lookup(self, path):
        path_list = self.split_path(path)
        return self.route_trie.find(path_list)

    def split_path(self, path):
        if path != "":
            temp = [path[0]]
            path_list = [x for x in path.split("/") if x]
            if temp[0][0] == "/":
                path_list = temp + path_list
            else:
                temp = [""]
                path_list = temp + path_list
        else:
            path_list = [""]

        return path_list


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/blog", "blog handler")
router.add_handler("/home", "home handler")

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup(""))
print(router.lookup("/home/about/blog"))

print("\n")

router.add_handler("someone/about/me", "me handler")
router.add_handler("/about/company", "company handler")
router.add_handler("/blog/sign_in", "sign in handler")
router.add_handler("/blog/sign_out", "sign out handler")

print(router.lookup("someone/about/me"))
print(router.lookup("/about/me"))
print(router.lookup("/about/company"))
print(router.lookup("/blog/sign_in"))
print(router.lookup("/blog/sign_out"))

