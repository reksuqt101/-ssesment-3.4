
# Create Node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create Binary Tree
def create_tree():
    S = Node("S")
    E1 = Node("E")
    L1 = Node("L")
    L2 = Node("L")
    O = Node("O")
    T = Node("T")
    E2 = Node("E")

    S.left = E1
    S.right = L1
    E1.left = L2
    E1.right = O
    L1.left = T
    L1.right = E2

    return S


# BFS
def bfs(root):
    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


# DFS
def dfs(root):
    if root is None:
        return []

    return [root.value] + dfs(root.left) + dfs(root.right)


# Main Program
root = create_tree()

print("BINARY TREE USING SELLOTE")
print("BFS:", " -> ".join(bfs(root)))
print("DFS:", " -> ".join(dfs(root)))
