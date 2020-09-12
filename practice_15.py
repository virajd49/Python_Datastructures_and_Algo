

"""
BST

 - insert (self balancing)
 - contains
 - remove (how to make self balancing ??)
 - traversals
    - pre order
    - post order
    - on order
    - level order
 - find successor
 - find predecessor

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left : Node = None
        self.right: Node = None
        self.height = 0


class SB_bst:
    def __init__(self):
        self.root = None

    def insert(self, root: Node, value):

        newNode = Node(value)

        #check if tree is empty
        if root == None:
            print("\ninserting", newNode.data)
            return newNode

        #check if we need to insert at left child or at right child
        if value > root.data:
            #go right
            print("\n going right")
            root.right = self.insert(root.right, value)
        else:
            #go left
            print("\n going left")
            root.left = self.insert(root.left, value)

        #recalculate the height of the root
        root.height = self.height(root)

        #check balance of the current sub tree
        balance = self.height(root.left) - self.height(root.right)

        #balance > 1 - imbalance in left subtree
        #balance < -1 - imbalance in right subtree

        if balance > 1 and value < root.left.data:
            #imbalance is in left child's left subtree
            #right rotate
            root = self.right_rotate(root)
            return root
        if balance > 1 and value > root.left.data:
            #imbalance is in left child's right subtree
            #leftrightrotate
            root.left = self.left_rotate(root.left)
            root = self.right_rotate(root)
            return root
        if balance < -1 and value > root.right.data:
            #imbalance is in right child's right subtree
            #left rotate
            root = self.left_rotate(root)
            return root
        if balance < -1 and value < root.right.data:
            #imbalance is in right child's left subtree
            #rightleftrotate
            root.right = self.right_rotate(root.right)
            root = self.left_rotate(root)
            return root

        return root


    def height(self, node: Node):

        if node == None:
            return -1

        if node.left != None and node.right != None:
            return max(node.left.height, node.right.height) + 1
        elif node.left != None:
            return node.left.height + 1
        elif node.right != None:
            return node.right.height + 1
        else:
            return 0



    def left_rotate(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        node.height = self.height(node)
        temp.height = self.height(temp)
        return temp



    def right_rotate(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        node.height = self.height(node)
        temp.height = self.height(temp)
        return temp

    def contains(self, root, value):

        #binary search through the tree - till you reach None

        if root == None:
            print("\nValue not found !")
            return

        if root.data == value:
            print("\nValue found !!")
            return
        elif value > root.data:
            self.contains(root.right, value)
        else:
            self.contains(root.left, value)

    def pre_order_traversal(self, root: Node):

        #root - left - right
        if root == None:
            return

        print(root.data, end=" -")

        self.pre_order_traversal(root.left)

        self.pre_order_traversal(root.right)

        return

    def post_order_traversal(self, root: Node):

        #left - right - root

        if root == None:
            return

        self.post_order_traversal(root.left)

        self.post_order_traversal(root.right)

        print(root.data, end=" -")

        return

    def in_order_traversal(self, root: Node):

        #left - root - right

        if root == None:
            return

        self.in_order_traversal(root.left)

        print(root.data, end=" -")

        self.in_order_traversal(root.right)

        return

    def level_order_traversal(self, root):

        if root == None:
            return

        queue = [root]

        while queue:
            curr = queue.pop(0)
            print("\n",curr.data)

            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)

        return


    def delete(self, root, value):

        if root == None:
            print("Tree dfoes not contain this value !!")
            return

        if root.data == value:
            #delete this node
            #find successor/predecessor and replace

            #successor is going to be on the right
            #predecessor is going to be on the left

            #does this node have any children ?
            #if no children
            if root.left == None and root.right == None:
                #we simply delete this guy
                return None
            if root.right == None:
                #we have to go left - find predecessor
                succParent = root.left

                if succParent.right == None:
                    root = root.left
                else:
                    succ = succParent.right

                    # keep going left till we find succ
                    while succ.right != None:
                        succParent = succ
                        succ = succ.right

                    root.data = succ.data
                    succParent.right = None

                    # have to check balance going up starting from succParent

            else:
                #node has left child - we'll find successor
                # we have to go right - find successor
                succParent = root.right

                if succParent.left == None:
                    root = root.right
                else:
                    succ = succParent.left

                    # keep going left till we find succ
                    while succ.left != None:
                        succParent = succ
                        succ = succ.left

                    root.data = succ.data
                    succParent.left = None

                    # have to check balance going up starting from succParent
        elif value > root.data:
            #go right
            root.right = self.delete(root.right, value)
        else:
            #go left
            root.left = self.delete(root.left, value)

        #re calculate height
        root.height = self.height(root)

        #check balance
        balance = self.height(root.left) - self.height(root.right)

        #if balance if off - check the required subtree's balance
        #then do required rotation
        if balance < -1:
            #we need to go right
            right_balance = self.height(root.right.left) - self.height(root.right.right)
            if right_balance < 0:
                #right rotation
                root = self.right_rotate(root)
                return root
            else:
                #left right rotation
                root.left = self.left_rotate(root.left)
                root = self.right_rotate(root)
                return root

        if balance > 1:
            #we need to go left
            left_balance = self.height(root.left.left) - self.height(root.left.right)
            if left_balance < 0:
                # right left rotation
                root.right = self.right_rotate(root.right)
                root = self.left_rotate(root)
                return
            else:
                # left rotation
                root = self.left_rotate(root)
                return root

        return root





new_tree = SB_bst()
input_array = [56, 9, 6, 44, 105, 72, 33, 21, 0, 5]

for x in input_array:
    new_tree.root = new_tree.insert(new_tree.root, x)


new_tree.in_order_traversal(new_tree.root)
new_tree.contains(new_tree.root, 21)
new_tree.post_order_traversal(new_tree.root)


print("\n",2^31)





