import unittest
from leetcode_algorithms.binary_tree import *

class Testing(unittest.TestCase):

    # init()
    def test_init(self):
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(pre_order(tree), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
