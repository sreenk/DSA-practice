def kth_node_from_end(self, k):
        if not self.head:
            return None
            
        slow = fast = self.head 
        for i in range(k):
            if not fast:
                return None
                
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow