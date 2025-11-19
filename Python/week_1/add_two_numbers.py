from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10

            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

def to_linked(lst):
    dummy = ListNode()
    curr = dummy
    for v in lst:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result

c1l1 = [9,9,9,9,9,9,9]
c1l2 = [9,9,9,9]

l1 = to_linked(c1l1)
l2 = to_linked(c1l2)

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

print(to_list(result))


