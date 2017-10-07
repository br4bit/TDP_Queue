class Queue():
    """Classe astratta che implemente ADT Queue."""

    def __init__(self):
        raise NotImplementedError('TBI')

    def __len__(self):
        """Restituite il numero di elementi nella cosa"""
        raise NotImplementedError('TBI')

    def first(self):
        """Restituisce (ma non rimuove) l'elemento al front della coda"""
        raise NotImplementedError('TBI')

    def dequeue(self):
        """Rimuove e restituisce l'elemento al front della coda"""
        raise NotImplementedError('TBI')

    def enqueue(self):
        """Aggiunge l'elemento al back della coda"""
        raise NotImplementedError('TBI')

    def is_empty(self):
        """Restituisce true se la coda è vuota"""
        raise NotImplementedError('TBI')
