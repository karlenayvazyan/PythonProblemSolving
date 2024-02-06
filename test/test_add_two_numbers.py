import unittest
from src.add_two_numbers import Solution
from src.add_two_numbers import ListNode


class TestAddTwoNumbers(unittest.TestCase):

    def test_0(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual("708", self.get_string(result))

    def test_1(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual("0", self.get_string(result))

    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]
    def test_2(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual("89990001", self.get_string(result))

    def test_3(self):
        l1 = ListNode(2, ListNode(4, ListNode(9)))
        l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual("70401", self.get_string(result))

    # [2,4,3] [5,6,4]
    # [7,0,8]
    def test_4(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual("708", self.get_string(result))

    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]
    def test_5(self):
        result = 0
        result = 18 // 10
        print(result)


    @staticmethod
    def get_string(list_node: ListNode):
        l1 = list_node
        result = ""
        while l1:
            result += str(l1.val)
            l1 = l1.next
        return result
