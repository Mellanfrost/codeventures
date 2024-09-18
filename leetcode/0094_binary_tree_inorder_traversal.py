from typing import Optional
from tester import test


# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal


"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution_one(root:Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    res = []
    def f(node):
        if node.left:
            f(node.left)
        res.append(node.val)
        if node.right:
            f(node.right)
    f(root)
    return res
        

def solution_two(root:Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    res = []
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            res.append(temp.val)
            root = temp.right
    return res


# TESTING
# --------------------

test_cases = [
    [[TreeNode(1, None, TreeNode(2, TreeNode(3)))], [1, 3, 2]],
    [[TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, None, TreeNode(8, TreeNode(9))))], [4, 2, 6, 5, 7, 1, 3, 9, 8]],
    [[None], []],
    [[TreeNode(1)], [1]],
]

test(solution_one, test_cases)
test(solution_two, test_cases)
