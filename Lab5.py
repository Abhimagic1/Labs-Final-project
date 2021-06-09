class NTree:
    class Position:

        def __init__(self, container, tree):
            self._container = container
            self._tree = tree
        def data(self):
            return self._tree.value
        def __eq__(self, other):
            return type(other) is type(self) and other._tree is self._tree
        def __ne__(self, other):
            return not (self == other)
#It is written within code that in order to start the code main variables must be identified; do so

    def __init__(self, value, parent=None):
        self.value = value
        self._children = []
        self.parent = parent


    def _validate(self, position): # Start here when coding NTREE oPS
        if not isinstance(position, self.Position):
            raise TypeError()
        if position._container is not self.root()._tree:
            raise ValueError()
        return position._tree
    def root(self):
        if self.is_empty():
            return None
        current = self
        while current.parent is not None:
            current = current.parent
        return self.Position(current, current)


    def is_root(self, position):
        return position == self.root()
    def add_parent(self, position):
        current_tree = self._validate(position)
        return self.Position(self.root()._tree, current_tree.parent)
    def is_leaf(self, position):
        current_tree = self._validate(position)
        return current_tree.is_leaf()
    def is_empty(self):
        return self.value is None and len(self._children) == 0


    def add_child(self, value):
        child = NTree(value, self)
        self._children.append(child)
        return child
    def number_of_children(self, position): # In other words the branches or leaves of the original tree
        current_tree = self._validate(position)
        return len(current_tree._children)


    def children(self, position):
        current_tree = self._validate(position)
        for child in current_tree._children:
            yield self.Position(self.root()._tree, child)
    def positions(self): # Make sure to test whether this shows origin or place within NTree
        for subtree in self._subtree_org_order(self.root()):
            yield subtree
    def _subtree_org_order(self,position):
        yield position
        for child in self.children(position):
            for sub_tree in self._subtree_org_order(child):
                yield sub_tree


    def __str__(self):
        return self.value
    def depth(self):
        current_depth = 0
        current_parent = self.parent
        while current_parent is not None: #None command will ensure; rest of items are passed without extra
            current_depth +=1
            current_parent = current_parent.parent
        return current_depth
    def is_leaf(self): #Leaf off branch is considered undefined while it makes the program run
        return len(self._children) == 0
    def height(self):
        if self.is_leaf():
            return self.depth()
        return max(child.height() for child in self._children)

org_root = NTree("Org_Tree") # root will be base code
print("root.depth: " + str(org_root.depth()))
lab_one = org_root.add_child("Child")
print("lab1.depth: " + str(lab_one.depth()))

lab_one_py = lab_one.add_child("Full depth") # written in textbook; depth is Tree value
print("lab1py.depth: " + str(lab_one_py.depth()))
project_one = org_root.add_child("Additional child")
project_one.add_child("Add Child")

print(org_root.height()) # next value inputted
root_position = org_root.root()
print(org_root.number_of_children(root_position))

for child in org_root.children(root_position):
    print(child.data())
for position in org_root.positions():
    print(position.data())
