class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
        
        return self.head
        
    def insert_at_end(self,data):
        new_node = Node(data)
        
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
            self.head = new_node
        
        return self.head
        
    def insert_at_position(self, data, pos):
        if not self.head or pos == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            
            return self.head
            
        else:
            count = 1 
            curr = self.head
            
            while curr.next:
                
                if count == pos-1:
                    res = curr.next
                    curr.next = Node(data)
                    curr.next.next = res
                    return self.head
                else:
                    curr = curr.next
                count += 1
                
            if count < pos:
                curr.next = Node(data)
        return self.head
        
    def delete_first_node(self):
        if self.head:
            self.head = self.head.next
            return self.head
        else:
            return None
            
    def delete_last_node(self):
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            return None
            
        curr = self.head
        while curr.next.next:
            curr = curr.next
        
        curr.next = None
        return self.head
        
    def delete_at_pos(self, pos):
        if not self.head:
            return
        if pos == 1:
            self.head = self.head.next
            return self.head
            
        count = 1
        curr = self.head
        prev = None
        
        while curr:
            if count == pos:
                res = curr.next
                prev.next = res
                return self.head
            
            count += 1
            prev = curr
            curr = curr.next
    
        return self.head
        
    def search_elem(self,target):
        if not self.head:
            return
        
        curr = self.head
        
        while curr:
            if curr.data == target:
                return curr
            curr = curr.next
        return None
    
    def ll_length(self):
        if not self.head:
            return 0
        count = 0
        curr = self.head
        
        while curr:
            curr = curr.next
            count += 1
        return count 

    def print_ll(self):
        if not self.head:
            return None
        
        curr = self.head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("\n")
    
node_list = LinkedList()
node_list.insert_at_end(10)
node_list.insert_at_end(40)
node_list.insert_at_end(70)
node_list.insert_at_end(100)
node_list.insert_at_end(120)
node_list.print_ll()
node_list.insert_at_position(20,2)
node_list.print_ll()
node_list.insert_at_beginning(0)
node_list.print_ll()

#node_list.delete_first_node()
#node_list.print_ll()
#node_list.delete_first_node()
#node_list.print_ll()
#node_list.delete_last_node()
#node_list.print_ll()
node_list.delete_at_pos(2)
node_list.print_ll()
res = node_list.search_elem(1)
if res:
    print(res.data) 
l =  node_list.ll_length()
print(l)