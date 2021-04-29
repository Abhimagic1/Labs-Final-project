from Lab3 import CircularQueue
queue = CircularQueue()

for number in range(5):
    queue.enqueue(number)

print(queue.get_raw_contents())

queue.dequeue()
queue.dequeue()

print(queue.get_raw_contents())

for number in range(7):
    queue.enqueue(number)

print(queue.get_raw_contents())

queue.dequeue()
queue.dequeue()

print(queue.get_raw_contents())


for number in range(5, 9):
    queue.enqueue(number)

print(queue.get_raw_contents())

queue.dequeue()
queue.dequeue()

print(queue.get_raw_contents())

for number in range(2, 8): #cls
    queue.enqueue(number)

print(queue.get_raw_contents())

queue.dequeue()
queue.dequeue()

print(queue.get_raw_contents())

for number in range(6, 12):
    queue.enqueue(number)

print(queue.get_raw_contents())

for number in range(11, 18):
    queue.enqueue(number)

print(queue.get_raw_contents())


for number in range(0, 15): # Furthest range
    queue.enqueue(number)

print(queue.get_raw_contents())
