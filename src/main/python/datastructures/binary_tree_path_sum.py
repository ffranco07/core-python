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

 Given the root of a binary tree and an integer targetSum, 
 return true if there exists a path from the root to a leaf 
 such that the sum of the nodes on the path is equal to targetSum, 
 and return false otherwise. 

"""

from node import Node

class BinaryTreePathSum:
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
    
    # Recursive function returns boolean if tree has path sum 
    # for target sum value
    # # Time Complexity: O(n) where n is the number of node in the tree
    # # Space Complexity: O(n) 
    def hasPathSumRecursive(self, root: Node, targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False
            
            # if both children are null, then the node is a leaf
            if node.left == None and node.right == None:
                return (curr + node.val) == targetSum
            
            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left or right
        
        return dfs(root, 0)
    

    # Iterative function returns boolean if tree has path sum 
    # for target sum value
    # # Time Complexity: O(n) where n is the number of node in the tree
    # # Space Complexity: O(n) 
    def hasPathSumIterative(self, root: Node, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, 0)]
        while stack:
            node, curr = stack.pop()
            # if both children are null, then the node is a leaf
            if node.left == None and node.right == None:
                if (curr + node.val) == targetSum:
                    return True

            curr += node.val
            if node.left:
                stack.append((node.left, curr))
            if node.right:
                stack.append((node.right, curr))

        return False

# Driver code
nums = [4, 2, 3, 1, 7, 6, 8, 9, 12, 25, 50]
tree = BinaryTreePathSum(Node(nums[0]))
for num in nums[1:]:
    tree.insert(tree.root, num)

tree.root.printTree(tree.root)

targetSum = 17

print("targetSum: " + str(targetSum))
print("Recursive hasPathSum: " + str(tree.hasPathSumRecursive(tree.root, targetSum)))
print("Iterative hasPathSum: " + str(tree.hasPathSumIterative(tree.root, targetSum)))









