from Collections.ArrayQueue import ArrayQueue

f = ArrayQueue()

f.enqueue(1)
f.enqueue(2)
f.enqueue(3)
f.enqueue(4)
f.enqueue(5)
f.enqueue(6)
f.dequeue()
f.dequeue()
f.dequeue()
f.dequeue()
f.dequeue()
f.dequeue()
f.enqueue(6)
f.enqueue(5)
f.enqueue(4)
print(len(f))
print(f)
print(f._front)
