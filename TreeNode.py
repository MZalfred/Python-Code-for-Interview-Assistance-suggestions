# norder traversal of a binary tree

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Example usage
# Creating a binary tree
#       1
#      / \
#     2   3
root = TreeNode(1, TreeNode(2), TreeNode(3))
print("Inorder traversal:")
inorder_traversal(root)
