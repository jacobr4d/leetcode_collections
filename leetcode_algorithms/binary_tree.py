class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order(root):
    if root == None:
        return []
    else:
        return [root.val] + pre_order(root.left) + pre_order(root.right)