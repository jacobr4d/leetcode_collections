import unittest
from more_collections.trie import Trie

class Testing(unittest.TestCase):

    # init()
    def test_init(self):
        trie = Trie()
        self.assertTrue(True)

    # size()
    def test_size_empty(self):
        trie = Trie()
        self.assertEqual(trie.getsize(), 0)

    def test_size_one(self):
        trie = Trie()
        trie.insert("abc")
        self.assertEqual(trie.getsize(), 1)

    def test_size_two(self):
        trie = Trie()
        trie.insert("abc")
        trie.insert("xyz")
        self.assertEqual(trie.getsize(), 2)

    def test_size_duplicate(self):
        trie = Trie()
        trie.insert("abc")
        trie.insert("abc")
        self.assertEqual(trie.getsize(), 1)

    # insert()
    def test_insert_one(self):
        trie = Trie()
        trie.insert("aaaaa")
        self.assertTrue(trie.search("aaaaa"))

    # search()
    def test_search_false(self):
        trie = Trie()
        trie.insert("abc")
        self.assertFalse(trie.search("a"))

    def test_search_true(self):
        trie = Trie()
        trie.insert("abc")
        self.assertTrue(trie.search("abc"))

    # startswith()
    def test_startswith_false(self):
        trie = Trie()
        trie.insert("abc")
        self.assertFalse(trie.startswith("z"))

    def test_startswith_true(self):
        trie = Trie()
        trie.insert("abc")
        self.assertTrue(trie.startswith("ab"))

    # delete()
    def test_delete_nonexistant_one(self):
        trie = Trie()
        self.assertRaises(ValueError, lambda: trie.delete("abc"))

    def test_delete_nonexistant_two(self):
        trie = Trie()
        trie.insert("abcd")
        self.assertRaises(ValueError, lambda: trie.delete("abc"))

    def test_delete_changes_size(self):
        trie = Trie()
        trie.insert("abc")
        trie.delete("abc")
        self.assertEqual(trie.getsize(), 0)

    def delete_one(self):
        trie = Trie()
        trie.insert("abc")
        trie.delete("abc")
        self.assertFalse(trie.search("abc"))

if __name__ == '__main__':
    unittest.main()
