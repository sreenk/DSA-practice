def isBST(root, min_allowed = float("-inf"), max_allowed = float("inf")):
    if root is None:
        return True
    
    if not (root.data > min_allowed and root.data < max_allowed):
        return False
    return isBST(root.left, min_allowed, root.data) and isBST(root.right, root.data, max_allowed)
