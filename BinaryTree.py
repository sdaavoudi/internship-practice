class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def printBT(node):

    if (node == None):
        return

    printBT(node.left)
    print(node.data, end=" ")
    printBT(node.right)

def mirrorBT(node):
    if (node == None):
        return
    else:
        mirrorBT(node.left)
        mirrorBT(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)

    print("Current Binary Tree: ")
    printBT(root)
    mirrorBT(root)

    print("\n")
    print("Binary serach tree after mirror: ")
    printBT(root)