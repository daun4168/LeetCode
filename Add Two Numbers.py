# Definition for singly-linked list.
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        num1 = 0
        digit_1 = 0
        while l1 is not None:
            num1 += l1.val * (10 ** digit_1)
            l1 = l1.next
            digit_1 += 1

        num2 = 0
        digit_2 = 0
        while l2 is not None:
            num2 += l2.val * (10 ** digit_2)
            l2 = l2.next
            digit_2 += 1

        result_num = num1 + num2

        if result_num == 0:
            return ListNode(0)

        result_digit = int(math.log10(result_num))

        before_node = None
        while result_digit >= 0:
            new_val = result_num // (10 ** result_digit) % 10
            before_node = ListNode(new_val, before_node)
            result_digit -= 1

        return before_node

