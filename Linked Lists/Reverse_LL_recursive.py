def reverse_ll_recursive(head):
    if not head or not head.next:
        return head
    
    new_head = reverse_ll_recursive(head)
    head.next.next = head
    head.next = None
    
    return new_head