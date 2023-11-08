"""
 Author: Francisco Franco

 A binary tree is a tree whose elements have at most 2 children.  
 For example, each node has 0 children, 1 child, or 2 children. 
 
 Tree Structure Terms

 Node: An object containing a key or value. 
       Almost all nodes have pointers to child nodes.
       Leaf nodes do not link to child nodes.
 Root: The node at the top of the tree. Only 1 root per tree.
 Edge: The link between two nodes.
 Parent: Any node (except root) with 1 edge upward to a node.
 Child: The node below a parent node connected by its edge downward.
 Degree of a node: The total number of branches of that node.
 Height of a node: Number of edges to its most distant leaf node. 
 Depth of a node:  Number of edges back up to the root.
 Subtree: The descendants of a node.
 Forest: A collection of disjoint trees

 Given the root of a binary tree, find the length of the longest 
 path from the root to a leaf.

"""

from node import Node

class BinaryTreeMaxDepth:
    def __init__(self, root:Node):
        self.root = root

    # Function to insert nodes into binary tree
    def insert(self, root:Node, val):
        if not root:
            root = Node(val)
            return root

        if root.val == val:
            return
        
        #print("About to check val less than root.val")

        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        
        return root

    # Function to return max depth of tree recursively
    # Time Complexity: O(n) where n is the number node in the tree
    # Space Complexity: O(n)
    def maxDepthRecursive(self, root:Node) -> int:
        if not root:
            return 0
        
        left = self.maxDepthRecursive(root.left)
        right = self.maxDepthRecursive(root.right)
        return max(left, right) + 1
    
    # Function to return max depth of tree iteratively
    # # Time Complexity: O(n) where n is the number node in the tree
    # # Space Complexity: O(n)
    def maxDepthIterative(self, root:Node) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        ans = 0
        
        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return ans

# Driver code
nums = [4, 2, 3, 1, 7, 6, 8, 9, 12, 25, 50]
#tree = BinaryTreeMaxDepth(Node(nums[0]))
tree = BinaryTreeMaxDepth(Node(nums[0]))
for num in nums[1:]:
    tree.insert(tree.root, num)

tree.root.printTree(tree.root)

print("Recursive max depth: " + str(tree.maxDepthRecursive(tree.root)))
print("Iterative max depth: " + str(tree.maxDepthIterative(tree.root)))









