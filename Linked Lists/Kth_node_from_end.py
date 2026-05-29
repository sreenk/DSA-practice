def kth_node_from_end(head, k):
        if not head:
            return None
            
        slow = fast = head 
        for i in range(k):
            if not fast:
                return None
                
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow