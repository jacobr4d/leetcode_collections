import unittest
from leetcode_collections.minheap import MinHeap

class Testing(unittest.TestCase):

    # init()
    def test_init(self):
        heap = MinHeap()
        self.assertTrue(True)

    # len()
    def test_truthy_empty(self):
        self.assertFalse(MinHeap())

    def test_truthy_nonempty(self):
        heap = MinHeap()
        heap.push(1)
        self.assertTrue(heap)

    def test_len_empty(self):
        self.assertEqual(len(MinHeap()), 0)
    
    def test_len_nonempty(self):
        heap = MinHeap()
        heap.push(1)
        heap.push(2)
        heap.push(3)
        self.assertEqual(len(heap), 3)

    # top()
    def test_top_empty(self):
        heap = MinHeap()
        self.assertRaises(IndexError, lambda: heap.top())

    def test_top_one(self):
        heap = MinHeap()
        heap.push(1)
        self.assertEqual(heap.top(), 1)

    def test_top_two(self):
        heap = MinHeap()
        heap.push(1)
        heap.push(2)
        self.assertEqual(heap.top(), 1)

    # push()
    def test_push_one(self):
        heap = MinHeap()
        heap.push(1)
        self.assertTrue(heap)

    def test_push_many(self):
        heap = MinHeap()
        for i in range(100):
            heap.push(i)
        self.assertTrue(heap)

    # pop()
    def test_pop_empty(self):
        heap = MinHeap()
        self.assertRaises(IndexError, lambda: heap.pop())

    def test_pop_right_order(self):
        heap = MinHeap()
        heap.push(3)
        heap.push(1)
        heap.push(2)
        self.assertEqual(heap.pop(), 1)


if __name__ == '__main__':
    unittest.main()
