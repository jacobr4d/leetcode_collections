import unittest
from more_collections.unionfind import UnionFind

class Testing(unittest.TestCase):

    # init()
    def test_init_zero(self):
        uf = UnionFind(0)
        self.assertTrue(uf)

    def test_init_nonzero(self):
        uf = UnionFind(1)
        self.assertTrue(uf)

    # union()
    def test_union_nonexistant(self):
        uf = UnionFind(10)
        self.assertRaises(IndexError, lambda: uf.union(-1, 1))

    def test_union_one(self):
        uf = UnionFind(10)
        uf.union(0, 1)
        self.assertEqual(uf.find(0), uf.find(1))

    def test_union_two(self):
        uf = UnionFind(10)
        uf.union(0, 1)
        uf.union(1, 2)
        self.assertTrue(uf.find(0) == uf.find(1) == uf.find(2))

    # find()
    def test_find_nonexistant_left(self):
        uf = UnionFind(10)
        self.assertRaises(IndexError, lambda: uf.find(-1))

    def test_find_nonexistant_right(self):
        uf = UnionFind(10)
        self.assertRaises(IndexError, lambda: uf.find(10))

    def test_find_unmodified(self):
        uf = UnionFind(5)
        self.assertEqual(uf.find(3), 3)

    def test_find_modified(self):
        uf = UnionFind(5)
        uf.union(2, 3)
        self.assertTrue(uf.find(2) in [2, 3])

if __name__ == '__main__':
    unittest.main()
