# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle, end = head, head #at the beginning of linked list
        while end and end.next:
            middle, end = middle.next, end.next.next
        return middle