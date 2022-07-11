# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        
        current_node = head.next
        temp = None 
        new_node = temp
        
        while current_node:
            
            if current_node.val == 0:
                if new_node == None:
                    new_node = ListNode(count)
                    temp = new_node
                else:
                    new_node.next = ListNode(count)
                    new_node = new_node.next
                # new_node = self.add_node(new_node , count)
                count = 0
            else:
                count = count + current_node.val
            current_node = current_node.next
            
        return temp
            
    def add_node(self , head , data):
        
        new_node = ListNode(data)
        if head == None:
            return new_node
        current_node = head
        # while current_node.next:
        #     current_node = current_node.next

        current_node.next = new_node
        
        return head
        
            
        