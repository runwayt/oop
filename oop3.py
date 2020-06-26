class Container(object):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return "<Container name:%s, size:%s>" % (self.__class__.__name__, self.size())

    def __str__(self):
        return "Container name:%s, size:%s" % (self.__class__.__name__, self.size())


class Tree(Container):
    def __init__(self, data, parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data, self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data, self)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def root(self):
        self.parent

    def size(self):
        size = 1
        if self.left:
            size += self.left.size()
        if self.right:
            size += self.right.size()
        return size


class Queue(Container):
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def head(self):
        return self.items[0]

    def tail(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


root = Tree(1)
root.insert(22)
root.insert(333)
root.insert(4444)
root.insert(5555)
root.insert(66666)
print(root)

q = Queue()
q.insert(4)
q.insert('hello world')
q.insert(True)
print(q)