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

# Need to support tuples lol
# class MaxHeap:
#     def __init__(self):
#         self.data = []

#     def __len__(self):
#         return len(self.data)

#     def top(self):
#         if not len(self):
#             raise IndexError('top of empty maxheap')
#         _val = [x for x in self.data[0]]
#         _val[0] *= -1
#         return _val

#     def push(self, val):
#         _val = [x for x in val]
#         _val[0] *= -1
#         heapq.heappush(self.data, tuple(_val))

#     def pop(self):
#         if not len(self):
#             raise IndexError('pop from empty maxheap')
#         _val = [x for x in heapq.heappop(self.data)]
#         _val[0] *= -1
#         return _val