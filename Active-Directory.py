from collections import deque


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


# parent = Group("parent")
# child = Group("child")
# sub_child = Group("subchild")
#
# sub_child_user = "sub_child_user"
# sub_child.add_user(sub_child_user)
#
# child.add_group(sub_child)
# parent.add_group(child)
# print(sub_child.is_user_in_group(sub_child_user))

parent = Group("P")
p_child1 = Group("x")
p_child2 = Group("y")
some_user = "Z"
parent.add_group(p_child1)
parent.add_group(p_child2)
parent.add_user(some_user)
x_child1 = Group("a")
x_child2 = Group("b")
p_child1.add_group(x_child1)
p_child1.add_group(x_child2)
y_child = Group("c")
some_user1 = "d"
p_child2.add_group(y_child)
p_child2.add_user(some_user1)


def is_user_in_group(user, group):
    q = deque()
    q.appendleft(group)
    while len(q) != 0:
        temp = q.pop()
        if len(temp.get_users()) != 0:
            for element in temp.get_users():
                if element == user:
                    return True

        if len(temp.get_groups()) != 0:
            for group in temp.get_groups():
                q.appendleft(group)

    return False


print(is_user_in_group(some_user1, parent))
print(is_user_in_group(some_user, parent))
print(is_user_in_group(some_user1, x_child1))

# # BFS used to traverse the graph/tree
# # O(m*n) where m refers to a node/group and n refers to its groups and users
