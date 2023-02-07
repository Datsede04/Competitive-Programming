class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        else:
            slow = head
            fast = head.next
            while fast != slow:
                if not fast or not fast.next:
                    return False
                slow=slow.next
                fast=fast.next.next
        return True
