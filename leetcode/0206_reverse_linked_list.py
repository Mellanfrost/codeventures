from typing import Optional


# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list


"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution_one(head:Optional[ListNode]) -> Optional[ListNode]:
    if not head or head.next:
        return head
    def f(node, previous_node):
        if not node:
            return previous_node
        next_node = node.next
        node.next = previous_node
        return f(next_node, node)
    return f(head, None)
