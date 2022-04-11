import os


def find_files(suffix, path):
    l = []
    s = "./" + path.split("/")[-1]

    def Backtrack(suffix, path, l, s):
        old_path = path
        old_s = s
        files = os.listdir(path)  # returns all files in particular directory
        for file in files:
            new_path = path + "/" + file
            if os.path.isdir(new_path):  # if new path is a path to some directory
                s = s + "/" + file
                Backtrack(suffix, new_path, l, s)
            elif os.path.isfile(new_path):  # if new path is a path to some file
                if new_path.endswith(suffix):
                    s = s + "/" + file
                    l.append(s)
            path = old_path
            s = old_s
        return l
    return Backtrack(suffix, path, l, s)

res = find_files(".c", "/Users/vivekkumar/Desktop/testdir")
print(res)
print(find_files('.h',"/Users/vivekkumar/Desktop/testdir"))
print(find_files('.k',"/Users/vivekkumar/Desktop/testdir"))
print(find_files('.py',"/Users/vivekkumar/Desktop"))


# Backtracking Algorithm or DFS used to solve the problem
# O(V) time complexity as all vertices/nodes checked
