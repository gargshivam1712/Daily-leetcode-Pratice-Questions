# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        current_node = head
        val = head.val
        while current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
                continue
            
            current_node = current_node.next
            val = current_node.val
        
            
        return head
            
        