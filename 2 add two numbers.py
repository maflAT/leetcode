"""You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def decodeLL(ll: ListNode):
    exp = n = 0
    while ll:
        n += ll.val * 10**exp
        exp += 1
        ll = ll.next
    return n

def toLL(n:int):
    n = str(n)
    ll = node = ListNode(n[-1])
    for d in reversed(n[:-1]):
        node.next = ListNode(d)
        node = node.next
    return ll

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return toLL(decodeLL(l1) + decodeLL(l2))
