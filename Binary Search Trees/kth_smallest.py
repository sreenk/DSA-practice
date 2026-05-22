
def kth_small(root,k):
    if root is None:
        return None
    count = [0]     
    def inorder(root, count):
        if root is None:
            return None
        
        left = inorder(root.left, count)
        if left is not None:
            return left
        
        count[0] += 1
        
        if count[0] == k:
            return root.data
        
        right=inorder(root.right, count)
        if right is not None:
            return right
    
    return inorder(root, count)