class NTree:
    class Position: #Similiar NTree
        def __init__(self, container, tree):
            self._container = container
            self._tree = tree
        def data(self):
            return self._tree.value
        def __eq__(self, other):
            return type(other) is type(self) and other._tree is self._tree
        def __ne__(self, other):
            return not (self == other)
        #Values will de differnt when adding to a list

    def __init__(self, value, parent=None):
        self.value = value
        self._children = []
        self.parent = parent
    def _validate(self, position):
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
    def number_of_children(self, position):
        current_tree = self._validate(position)
        return len(current_tree._children)
    def children(self, position):
        current_tree = self._validate(position)
        for child in current_tree._children:
            yield self.Position(self.root()._tree, child)
    def positions(self):
        for subtree in self._subtree_org_order(self.root()):
            yield subtree
    def _subtree_org_order(self, position):
        yield position
        for child in self.children(position):
            for sub_tree in self._subtree_org_order(child):
                yield sub_tree
    def __str__(self):
        return self.value

    def breadth_first_alg(self): #new value that will
        queue = [self.root()]
        while len(queue) != 0:
            current_position = queue.pop(0)
            yield current_position
            for child in self.children(current_position):
                queue.append(child)

    def is_leaf(self): #Again leaf declares no usage but code fails without; passes its own test
        return len(self._children) == 0
    def depth(self):
        current_depth = 0
        current_parent = self.parent
        while current_parent is not None:
            current_depth += 1
            current_parent = current_parent.parent
        return current_depth
    def height(self):
        if self.is_leaf():
            return self.depth()
        return max(child.height() for child in self._children)

org_root = NTree('CIS2001-Winter2021- Computer Science II for Data scientists') # Base root code, different values but similiar stature
print("root.depth(): " + str(org_root.depth()))
lab_one = org_root.add_child('Lab1')
print("lab1.depth(): " + str(lab_one.depth()))

lab_one_py = lab_one.add_child(('lab1.py'))
print("lab1py.depth(): " + str(lab_one_py.depth()))
project1 = org_root.add_child(('Project 1')) # will result in order and tree registered within the final product
project1.add_child('Mazesolver.py')
project1.add_child('__main__.py')
project1.add_child('unit_test.py')
org_root.add_child('basic_arrays.py')
print(org_root.height())
root_position = org_root.root()
print(org_root.number_of_children(root_position))


for child in org_root.children(root_position):
    print(child.data())
    for position in org_root.positions():
        print('breadth-first traversal - node-by-node')
    for position in org_root.breadth_first_alg(): #used for traversal on graphs or tree data structures- educative
        print(position.data())
