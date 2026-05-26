class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def pair_sum(root, target):
    if root is None:
        return None
        
    sum_list = []
    def inorder(root):
        if root is None:
            return None
            
        inorder(root.left)
        sum_list.append(root.data)
        inorder(root.right)
    
    inorder(root)
    first = 0
    last = len(sum_list) - 1
    
    while first < last:
        if sum_list[first] + sum_list[last] == target:
            return sum_list[first] , sum_list[last]
        elif sum_list[first] + sum_list[last] < target:
            first += 1
        else:
            last -=1
    return None, None