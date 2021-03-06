class HashMap:
#Make sure you completely understand before running command
    class Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        self._data = [None] * 10
        self._number_of_items = 0
        self._load_factor = .75

    def resize_check(self): #Was added to ensure size
        if self._number_of_items / len(self._data) > self._load_factor:
            old_data = self._data
            self._data = [None] * len(self._data) * 2

            for node in old_data:
                current_node = node
                while current_node is not None:
                    self.add_item(current_node.key, current_node.value) #add_item command not present in node
                    current_node = current_node.next

    def __setitem__(self, key, value=None):
        self._number_of_items += 1

        self.resize_check()

        item_hash = hash(key)
        item_index = item_hash % len(self._data)
        if self._data[item_index] is None:
            self._data[item_index] = self.Node(key, value)
        else:
            current_node = self._data[item_index] #Along in the text; bucket
            if current_node.key == key:
                current_node.value = value
            else:
                while current_node.next is not None:
                    if current_node.next.key == key:
                        current_node.next.value = value
                        return
                    else:
                        current_node = current_node.next
                current_node.next = self.Node(key, value)

    def __getitem__(self, key):
        item_hash = hash(key)
        item_index = item_hash % len(self._data)
        if self._data[item_index] is None:
            raise KeyError
        current_node = self._data[item_index]
        while current_node is not None: #Place where 'bucket' used
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        raise KeyError

    def __delitem__(self, key):
        item_hash = hash(key)
        item_index = item_hash % len(self._data)
        if self._data[item_index] is None:
            raise KeyError
        current_node = self._data[item_index]

        if current_node.key == key:
            value = current_node.value
            self._data[item_index] = current_node.next
            return value

        while current_node.next is not None: #Use this node to store current values
            if current_node.next.key == key:
                value = current_node.next.value
                current_node.next = current_node.next.next
                return value

            current_node = current_node.next
        raise KeyError
    #full node created, after reading into proj
