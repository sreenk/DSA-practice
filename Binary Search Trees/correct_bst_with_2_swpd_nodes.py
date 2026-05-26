class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def correct_bst(root):
    if root is None:
        return None

    first = [None]
    last = [None]
    middle = [None]
    prev = [None]

    def inorder(root):
        if root is None:
            return None

        inorder(root.left)

        if prev[0]:
            if (root.data < prev[0].data):
                if not first[0]:
                    first[0] = prev[0]
                    middle[0] = root
                else:
                    last[0] = root

        prev[0] = root

        inorder(root.right)

    inorder(root)
    if first[0] and last[0]:
        first[0].data, last[0].data = last[0].data, first[0].data
    elif first[0] and middle[0]:
        first[0].data,middle[0].data = middle[0].data, first[0].data
    else:
        return None