class MaximumPriorQueue:

    class Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value
        def __gt__(self, other):
            return self._key > other._key

    def __init__(self):
        self._data = [None]
        self._number_of_items = 0

    def add(self, key, value=None):
        if self._number_of_items == len(self._data):
            self._increase_size()
        item = self._Item(key, value)
        self._data[self._number_of_items]= item #Self data is undefined, while also not affecting data, should be okay
        self._upheap(self._number_of_items)
        self._number_of_items += 1
    def remove_max(self):
        self._number_of_items -= 1
        self._swap(0, self._number_of_items)
        item = self._data[self._number_of_items]
        self._data[self._number_of_items]= None
        self._downheap(0)
        return item._key, item._value #These values somehow refrence NONE command, which show they are not refrenced

    def _increase_size(self):
        new_data = [None] * len(self._data) *2
        for index in range(len(self._data)):
            new_data[index] = self._data[index]
        self._data = new_data
    def _upheap(self, index):
        if index != 0:
            parent_index = self._add_parent(index)
            if self._data[index] > self._data[parent_index]:
                self._swap(index, parent_index)
                self._upheap(parent_index)
    def _downheap(self, index):
        largest_child_index = None
        if self._valid_index(self._right_children(index)):
            largest_child_index = self._right_children(index)
            if self._data[self._left_children(index)] > self._data[largest_child_index]:
                largest_child_index = self._left_children(index)

        elif self._valid_index(self._left_children(index)):
            largest_child_index = self._left_children(index)

        if largest_child_index is not None:
            if self._data[largest_child_index] > self._data[index]:
                self._swap(largest_child_index, index)
                self._downheap(largest_child_index)

    def _swap(self, index, new_index):
        temp = self._data[index]
        self._data[index] = self._data[new_index]
        self._data[new_index] = temp

    def _add_parent(self, index):
        return (index -1) // 2 #Index allows us to identify the exact #'s
    def _left_children(self, index):
        return index * 2 +1
    def _right_children(self, index):
        return index *2 + 2

    def _valid_index(self, index):
        return index < self._number_of_items and index >= 0
    def max(self):
        return self._data[0]._key, self._data[0]._value #Same issue, but can be fixed by running code mained when inputs are added
    def __len__(self):
        return self._number_of_items
    def is_empty(self):
        return len(self) == 0 #Overall neutral; origin

#Base code complete can be refrenced, no inputs







