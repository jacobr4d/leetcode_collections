class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Two Pointers: O(n), O(1)
    a, b = None, head
    while b: 
        b.next, a, b = a, b, b.next
    return a