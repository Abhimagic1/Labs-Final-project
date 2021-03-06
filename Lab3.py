class CircularQueue:

    DEFAULT_CAPACITY = 11 #Adjust to explore whether change is made

    def __init__(self, initial_size = DEFAULT_CAPACITY):
        self._data = [None] * initial_size
        self._front = 0
        self._back = 0
        self._number_of_items = 0

    def enqueue(self, item): #Backwards queue, _raw_contents is where you would input values
        self._check_capacity()
        self._data[self._back] = item
        self._back += 1
        if self._back == len(self._data):
            self._back = 0
        self._number_of_items += 1

    def dequeue(self):
        if self._number_of_items == 0:
            raise IndexError
        item = self._data[self._front]
        self._data[self._front] = None
        self._front += 1 #Write this down for final, recursive until stopped; resizes
        if self._front == len(self._data):
            self._front = 0
        self._number_of_items -= 1
        return item

    def front(self):
        if self._number_of_items == 0:
            raise IndexError
        return self._data[self._front]

    def __len__(self):
        return self._number_of_items

    def _check_capacity(self): # Traps values in one
        if self._number_of_items >= len(self._data):
            new_data = [None] * len(self._data) * 2
            new_data_index = 0
            for index in range(self._front, len(self._data)):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1 # Hold down write HRD
            for index in range(0, self._back):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
            self._data = new_data
            self._front = 0
            self._back = self._number_of_items

    def get_raw_contents(self):
        return str(self._data)