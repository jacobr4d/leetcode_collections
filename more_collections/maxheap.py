import heapq

class MaxHeap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def top(self):
        if not len(self):
            raise IndexError('top of empty maxheap')
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        if not len(self):
            raise IndexError('pop from empty maxheap')
        return -heapq.heappop(self.data)