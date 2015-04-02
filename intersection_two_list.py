# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pa, pb = headA, headB
        len_a, len_b = 0, 0
        while pa is not None:
            len_a += 1
            pa = pa.next
        while pb is not None:
            len_b += 1
            pb = pb.next
        pa, pb = headA, headB
        if len_a > len_b:
            for i in range(len_a - len_b):
                pa = pa.next
        if len_b > len_a:
            for i in range(len_b - len_a):
                pb = pb.next
        while pa != pb:
            pa = pa.next
            pb = pb.next
        return pa
