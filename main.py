class Vertex:
    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def info(self):
        if self.parent is None:
            return f"[{self.key} {self.value}]"
        else:
            return f"[{self.key} {self.value} {self.parent.key}]"

    def is_leaf(self):
        return self.left is None and self.right is None


class DBT:
    def __init__(self):
        self.root = None
        self.height = 0

    def add(self, key, value):
        if self.root is None:
            self.root = Vertex(key, value, None)
            self.height += 1
        else:
            current_vertex = self.root
            height = 1
            while True:
                if key < current_vertex.key:
                    if current_vertex.left is None:
                        current_vertex.left = Vertex(key, value, current_vertex)
                        height += 1
                        if height > self.height:
                            self.height = height
                        break
                    else:
                        current_vertex = current_vertex.left
                        height += 1
                elif key > current_vertex.key:
                    if current_vertex.right is None:
                        current_vertex.right = Vertex(key, value, current_vertex)
                        height += 1
                        if height > self.height:
                            self.height = height
                        break
                    else:
                        current_vertex = current_vertex.right
                        height += 1


    def print(self):
        level = 0
        print_counter = 0
        current_vertex = self.root
        while level < self.height:
            if current_vertex is None:
                print('_')
                break
            else:
                print(current_vertex.info())
                print_counter += 1
            if print_counter == 2 ** level:
                level += 1
                print_counter = 0


test_tree = DBT()
test_tree.add(8, 10)
test_tree.add(4, 14)
test_tree.add(7, 15)
test_tree.add(9, 11)
test_tree.add(3, 13)
test_tree.add(5, 16)
test_tree.add(88, 1)
test_tree.add(11, 2)
test_tree.add(100, 18)
print()
