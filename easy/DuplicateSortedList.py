'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''



class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):

        if head == None or head.next == None:
            return head
            
        current_elem = head
        next_elem = head.next

        if next_elem.next == None and current_elem.val != next_elem.val:
            return head
        
        elif next_elem.next == None and current_elem.val == next_elem.val:
            head.next = None 
            return head

        elif current_elem.val != next_elem.val:
            current_elem = next_elem
            next_elem = next_elem.next
            self.deleteDuplicates(current_elem)

        elif current_elem.val == next_elem.val:
            head.val = next_elem.val
            head.next = next_elem.next
            self.deleteDuplicates(head)

        return head
