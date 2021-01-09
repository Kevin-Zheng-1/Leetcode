# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Solution(object):
    def removeNthFromEnd(self, head, n):
	
        slow = head # finally point to the previous node of the target node
        fast = head # finally point to the last node
        for i in range(n): # let the fast pointer move n steps ahead of the slow pointer
            fast = fast.next
        
        # This situation would happen when we are required to del the first node (n = len(List))
        # Also, it can handle the [] case
        if not fast:
            return slow.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return head
        
# 双指针，两个指针中间隔着n个数，前面的指针遍历到头之后，后面的指针跳一个即得到答案        
