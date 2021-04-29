class DoubleLinkedList:
    class position:

        def __init__(self, containter, node):
            self._container = containter
            self._node = node

            def data(self):
                return self._node.data

            def _equal_(self, other):
                return type(other) is type(self) and other._node is self._node

            def _ne_(self, other):
                return not (self == other)

    def __init__(self):
        self._head = self.node(None)
        self._head.next = self._head
        self._head.previous = self._head
