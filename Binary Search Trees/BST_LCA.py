class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def LCA_BST(root, p,q):
    if root is None:
        return None
        
    if p.data <= root.data and q.data >= root.data:
        return root
    elif p.data > root.data and q.data > root.data:
        return LCA_BST(root.right, p, q)
    else:
        return LCA_BST(root.left, p, q)
                