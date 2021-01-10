# Merge two sorted linked lists and return it as a sorted list. 
# The list should be made by splicing together the nodes of the first two lists.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        curr = dummy = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        curr.next = l1 or l2
        
        return dummy.next
        
# Iteration. 两两比较，元素小的链表上的指针往后移.     

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            
# Recursion.        
