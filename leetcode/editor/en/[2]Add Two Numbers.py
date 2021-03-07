# You are given two non-empty linked lists representing two non-negative integer
# s. The digits are stored in reverse order, and each of their nodes contains a si
# ngle digit. Add the two numbers and return the sum as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the nu
# mber 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#  
# 
#  Example 2: 
# 
#  
# Input: l1 = [0], l2 = [0]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each linked list is in the range [1, 100]. 
#  0 <= Node.val <= 9 
#  It is guaranteed that the list represents a number that does not have leading
#  zeros. 
#  
#  Related Topics Linked List Math Recursion 
#  👍 11029 👎 2654


# leetcode submit region begin(Prohibit modification and deletion)
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


# leetcode submit region end(Prohibit modification and deletion)
