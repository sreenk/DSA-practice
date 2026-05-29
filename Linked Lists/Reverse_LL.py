def reverse_ll(head):
        if not head:
            return None
        
        curr = head
        prev = None

        while curr:
            res = curr.next
            curr.next = prev
            prev = curr
            curr = res
                
        head = prev
        return head