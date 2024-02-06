from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def equal(self, other):
        while self and other and self.val == other.val:
            self = self.next
            other = other.next
        if not self and not other:
            return True
        return False


# 2,4,3
# 5,6,4
# 7,0,8
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_list_node: ListNode = ListNode(0)
        result_list_node_current: ListNode = result_list_node
        carry = 0
        while l1 or l2 or carry > 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            result_sum = l1_val + l2_val + carry
            carry = result_sum // 10
            result_list_node_current.next = ListNode(result_sum % 10)
            result_list_node_current = result_list_node_current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result_list_node.next
