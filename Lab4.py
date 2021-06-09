class DoublyLinkedList:
# First write Double, then included one/singular ; initial as told by teacher
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
        def data(self):
            return self._node.data
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self, other):
            return not ( self == other )


    def __init__(self,):
        self._head = self.Node(None)
        self._head.next = self._head
        self._head.previous = self._head
        self._number_of_items = 0
    def __len__(self):
        return self._number_of_items
    def first(self):
        return self._make_position(self._head.next)
    def last(self):
        return self._make_position(self._head.previous)


    def after(self, position):
        node = self._validate(position)
        return self._make_position(node.next)
    def before(self, position):
        node = self._validate(position)
        return self._make_position(node.previous)
    def add_after_list(self, position, data):
        node = self._validate(position)
        return self._make_position(self._insert_between(data, previous=node, next=node.next))
    def add_before_list(self, position, data):
        node = self._validate(position)
        return self._make_position(self._insert_between(data, previous=node.previous, next=node))
    def delete(self, position):
        node = self._validate(position)
        return self._remove_node(node)
    def replace(self, position, data):
        node = self._validate(position)
        original = node.data
        node.data = data
        return original
    def is_empty(self):
        return self._number_of_items == 0


    def add_to_front_list(self, item):
        self._insert_between(item, next=self._head.next, previous=self._head)
    def add_to_back_list(self, item):
        self._insert_between(item, next=self._head, previous=self._head.previous)
    def remove_back(self):
        if self.is_empty():
            raise ValueError("List is empty")
        return self._remove_node(self._head.previous)
    def remove_front(self):
        if self.is_empty():
            raise ValueError("List is empty")
        return self._remove_node(self._head.next)
    def pop(self, index):
        if not (0 <= index < self._number_of_items):
            raise IndexError("invalid index")
        current_item = self._head.next
        for number in range(index):
            current_item = current_item.next
        return self._remove_node(current_item)
    def insert(self, index, item):
        if not (0 <= index < self._number_of_items):
            raise IndexError("invalid index")
        current_item = self._head.next
        for number in range(index):
            current_item = current_item.next
        self._insert_between(item, previous=current_item.previous, next=current_item)

    def __next__(self):
        if self._current is self._head:
            raise StopIteration()
        else:
            answer = self._current.data
            self._current = self._current.next
            return answer
    def __iter__(self):
        self._current = self._head.next
        return self
        current = self.first()
        while current is not None: # current = self.first(), designed to ensure list will show the current values, seems unreachable until anticipated values put in
            yield current.data()
            current = self.after(current)
    def _insert_between(self, item, previous, next):
        new_node = self.Node(item, next = next, previous = previous)
        new_node.previous.next = new_node
        new_node.next.previous = new_node
        self._number_of_items += 1
        return new_node
    def _remove_node(self, current_item):
        data = current_item.data
        current_item.data = None
        current_item.previous.next = current_item.next
        current_item.next.previous = current_item.previous
        self._number_of_items -= 1
        return data
    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError()
        if position._container is not self:
            raise ValueError()
        if position._node.next is None:
            raise ValueError()
        return position._node
    def _make_position(self, node):
        if node is self._head:
            return None
        return self.Position(self, node)

    class Node:
        def __init__(self, data, next=None, previous = None):
            self.data = data
            self.next = next
            self.previous = previous


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._number_of_items = 0
    def __len__(self):
        return self._number_of_items
    def add_to_front_list(self, data):
        new_node = self.Node(data, self._head) #Node is unresolved; still works when arranging list
        if self._head.next is None:
            return None

doublyLinkedList_range = DoublyLinkedList()
for n in range(20): # any value according to value within code, so no initial value inputted; one less
    doublyLinkedList_range.add_to_back_list(n)

for item in doublyLinkedList_range:
    print(item)
current_position = doublyLinkedList_range.first()

while current_position is not None:
    print(current_position.data())
    current_position = doublyLinkedList_range.after(current_position)



