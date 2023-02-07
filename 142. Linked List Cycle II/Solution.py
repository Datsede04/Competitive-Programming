class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast == slow:
                while head != fast:
                    head=head.next
                    fast=fast.next 
                return head
        return None