class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def pair_sum(root, target):
    if root is None:
        return None
    
    stack1 = []
    stack2 = []

    def inorder(root):
        if root is None:
            return None
        while root:
            stack1.append(root)
            root = root.left
    
    def rev_inorder(root):
        if root is None:
            return None
        
        while root:
            stack2.append(root)
            root = root.right

    def get_next(stack):
        top = stack.pop()
        right = top.right
        while right:
            stack.append(right)
            right = right.left

        return top.data

    def get_prev(stack):
        top = stack.pop()
        left = top.left
        while left:
            stack.append(left)
            left = left.right
        return top.data
    
    inorder(root)
    rev_inorder(root)
    start = get_next(stack1)
    finish = get_prev(stack2)

    while start < finish:
        if start + finish == target:
            return start,finish
        elif start +finish < target:
            start = get_next(stack1)
        else:
            finish = get_prev(stack2)
    return None, None
        