import unittest
from more_collections.trie import Trie

class Testing(unittest.TestCase):
    def test_create(self):
        trie = Trie()
        self.assertEqual(trie.size, 0)
        self.assertEqual(trie.depth, 0)

    def test_insert(self):
        trie = Trie()
        trie.insert("foo")
        trie.insert("bar")
        trie.insert("baz")
        self.assertEqual(trie.size, 3)

if __name__ == '__main__':
    unittest.main()
