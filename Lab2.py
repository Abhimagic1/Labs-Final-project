#Am not able to import matplotlib, due to error while doing so, unable to plot
import time


def compute_time_to_add(list_to_add_to, item):
    start = time.perf_counter()
    list_to_add_to.append(item)
    end = time.perf_counter()
    return end-start


def compute_time_to_remove_from_index(list_to_remove_from, index_to_remove_from):
    start = time.perf_counter()
    list_to_remove_from.pop(index_to_remove_from)
    end = time.perf_counter()
    return end - start # values = list(range(100_000))


def compute_time_to_insert_at_index(list_to_insert_into, index_to_insert_into):
    start = time.perf_counter()
    list_to_insert_into.insert(index_to_insert_into, index_to_insert_into)
    end = time.perf_counter()
    return end - start

timings = [] #Variables worth changing to explore, make sure to do so
some_list = []
length_of_list = []

for n in range(500_000): #Will be able to adjust, typically reaches furthest negative value till stop
    length_of_list.append(len(some_list))
    timings.append(compute_time_to_insert_at_index(some_list, n))

print(some_list, timings) #Still able to show the values, cannot plot
