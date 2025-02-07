#class ListNode(object):
    #def __init__(self, val=0, next=None):
        # self.val = val
        # self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        new = ListNode(head.val)
        new_cur = new
        current = head
        while current:
            
            if current.val != new_cur.val:
                new_cur.next = ListNode(current.val)
                new_cur = new_cur.next
            current = current.next
    

        return new