# coding: utf-8
import unittest
import random

from data_structures.trees.binary_search_tree import BinarySearchTree
from data_structures.trees.binary_search_tree import BinaryTreeNode


class BinaryTreeNodeTest(unittest.TestCase):
    def setUp(self):
        self.node = BinaryTreeNode(2)

    def test__eq__(self):
        other_node = BinaryTreeNode(2)
        self.assertEqual(self.node, other_node)

        node_a = BinaryTreeNode(2, left=BinaryTreeNode(1), right=BinaryTreeNode(3))
        node_b = BinaryTreeNode(2, left=BinaryTreeNode(1), right=BinaryTreeNode(3))
        self.assertEqual(node_a, node_b)

        other_node = BinaryTreeNode(22)
        self.assertNotEqual(self.node, other_node)

    def test_left(self):
        self.assertEqual(self.node.left, None)

        self.node.left = BinaryTreeNode(1)
        self.assertEqual(self.node.left.value, 1)

    def test_right(self):
        self.assertEqual(self.node.right, None)

        self.node.right = BinaryTreeNode(3)
        self.assertEqual(self.node.right.value, 3)


class BinarySearchTreeTest(unittest.TestCase):
    def setUp(self):
        self.empty_bst = BinarySearchTree()

        #     ______8
        #    /       \
        #   3__       10___
        #  /   \           \
        # 1     6          _14
        #      / \        /
        #     4   7      13
        self.insert_items = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        self.bst = BinarySearchTree()
        for i in self.insert_items:
            self.bst.insert(i)

    def test__eq__(self):
        tree_1 = BinarySearchTree()
        for i in self.insert_items:
            tree_1.insert(i)
        self.assertEqual(self.bst, tree_1)

        tree_2 = BinarySearchTree()
        for i in [1, 2, 3]:
            tree_2.insert(i)
        self.assertNotEqual(self.bst, tree_2)

        self.assertNotEqual(self.bst, self.empty_bst)

    def test__len__(self):
        self.assertEqual(len(self.empty_bst), 0)
        self.assertEqual(len(self.bst), len(self.insert_items))

    def test__iter__(self):
        items = [node.value for node in self.bst]
        expected = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        self.assertEqual(items, expected)

    def test__contains__(self):
        self.assertIn(random.choice(self.insert_items), self.bst)
        self.assertNotIn(100, self.bst)

    def test_search(self):
        self.assertEqual(self.bst.search(8), self.bst.root)
        self.assertEqual(self.bst.search(1), self.bst.root.left.left)
        self.assertEqual(self.bst.search(13), self.bst.root.right.right.left)

        self.assertEqual(self.bst.search(100), None)

    def test_inorder_traverse(self):
        items = [node.value for node in self.bst.inorder_traverse(self.bst.root)]
        expected = [1, 3, 4, 6, 7, 8, 10, 13, 14]
        self.assertEqual(items, expected)

        items = [node.value for node in self.bst.inorder_traverse(self.bst.root.right.left)]
        expected = []
        self.assertEqual(items, expected)

    def test_preorder_traverse(self):
        items = [node.value for node in self.bst.preorder_traverse(self.bst.root)]
        expected = [8, 3, 1, 6, 4, 7, 10, 14, 13]
        self.assertEqual(items, expected)

    def test_postorder_traverse(self):
        items = [node.value for node in self.bst.postorder_traverse(self.bst.root)]
        expected = [1, 4, 7, 6, 3, 13, 14, 10, 8]
        self.assertEqual(items, expected)

    def test_breadth_first_traverse(self):
        items = [node.value for node in self.bst.breadth_first_traverse(self.bst.root)]
        expected = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        self.assertEqual(items, expected)

    def test_level_order_traverse(self):
        items = [node.value for node in self.bst.level_order_traverse(self.bst.root)]
        expected = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        self.assertEqual(items, expected)

    def test_traverse(self):
        with self.assertRaises(ValueError):
            self.bst.traverse('NOT EXIST')

    def test_is_root(self):
        self.assertTrue(self.bst.is_root(self.bst.root))
        self.assertFalse(self.bst.is_root(self.bst.root.left))
        self.assertFalse(self.bst.is_root(self.bst.root.right))

    def test_childre(self):
        self.assertEqual(list(self.bst.children(self.bst.root)), [self.bst.root.left, self.bst.root.right])
        self.assertEqual(list(self.bst.children(self.bst.root.left)), [self.bst.root.left.left, self.bst.root.left.right])
        self.assertEqual(list(self.bst.children(self.bst.root.right)), [self.bst.root.right.right])
        self.assertEqual(list(self.bst.children(self.bst.root.left.left)), [])

    def test_is_leaf(self):
        self.assertTrue(self.bst.is_leaf(self.bst.root.left.left))
        self.assertTrue(self.bst.is_leaf(self.bst.root.left.right.left))
        self.assertTrue(self.bst.is_leaf(self.bst.root.left.right.right))
        self.assertTrue(self.bst.is_leaf(self.bst.root.right.right.left))

        self.assertFalse(self.bst.is_leaf(self.bst.root))
        self.assertFalse(self.bst.is_leaf(self.bst.root.left))
        self.assertFalse(self.bst.is_leaf(self.bst.root.right))


if __name__ == '__main__':
    unittest.main()