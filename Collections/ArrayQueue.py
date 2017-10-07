from Collections.Queue import Queue


class ArrayQueue(Queue):
    """Implementazione di ADT Queue basata sul tipo list di Python usato come array circolare"""
    DEFAULT_CAPACITY = 10
    _front = 0

    def __init__(self):
        """Crea coda vuota"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        """Restituisce il numero di elementi presenti nella coda"""
        return self._size

    def is_empty(self):
        """Restituisce true se la coda è vuota"""
        return self._size == 0

    def first(self):
        """Restituisce ma non rimuove l'elemento al front della coda. Se è vuota raise exception."""
        if not self.is_empty():
            return self._data[self._front]
        raise ValueError('Queue is empty')

    def dequeue(self):
        """Restituisce e rimuove l'elemento al front della coda"""
        if not self.is_empty():
            if len(self._data) - self._size > len(self._data) // 4:
                self._resize(int(len(self._data)) - len(self._data) // 4)
            ris = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)
            self._size -= 1
            return ris
        raise ValueError('Queue is empty')

    def enqueue(self, e):
        """Aggiunge un elemento al back della coda"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)  # front+size mi da la posizione dove inserire l'elemento
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Ridimensiona l'array portandolo a dimensione cap"""
        old = self._data
        self._data = [None] * cap
        j = self._front
        for k in range(len(self._data)):
            self._data[k] = old[j]
            j = (j + 1) % len(old)
        self._front = 0

    def __str__(self):
        return str(self._data)
