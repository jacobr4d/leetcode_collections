import unittest
from more_collections.minheap import MinHeap

class Testing(unittest.TestCase):
    def test_create(self):
        heap = MinHeap()
        self.assertFalse(heap)
        self.assertEqual(len(heap), 0)

    def test_push_pop(self):
        heap = MinHeap()
        heap.push(1)
        heap.push(3)
        heap.push(2)
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 3)
        self.assertRaises(IndexError, lambda: heap.pop())

    def test_len_updates(self):
        heap = MinHeap()
        for i in range(10):
            heap.push(i)
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
