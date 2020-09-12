



"""

Trees

BST
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
        self.parent = None
        self.height = 0

#self balancing binary search tree
class BinarySearchTree:

    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value, root:Node):
        #this has to be a recursive function

        #we might be adding the first value for this subtree - so root will be null
            #so we just have to add a new node here - this is also used for adding a new left child or right child
        if root == None:
            return Node(value)
        #value can be greater than given root
            #recursive call on right child - that will return whatever the balanced subtree right child is
        if value > root.data:
            root.right = self.insert(value, root.right)
            root.right.parent = root
        else:
            root.left = self.insert(value, root.left)
            root.left.parent = root
        #value can be smaller than given root
            #recursive call on left child - that will return whatever the balanced subtree left child is

        #so at this point we should have the root, the left.child and the right.child and our parent is expecting the 'root' to be returned

        #we just added a child to the current 'root' - so recalculate it's height

        #call height
        root.height = self.height(root)

        #check balance for this node
        balance = self.height(root.left) - self.height(root.right)
        #height of left child
        #height of right child
        #get difference

        #4 cases
        #imbalance can be in
            #right subtree of right child
            #left subtree of right child
            #right subtree of left child
            #left subtree of left child

        #left child and if value is > leftchild.value - then right subtree of left child - leftRight rotate
         #if we have a new root - return that to teh recursive parent waiting for the 'root'
        if balance > 1 and value < root.left.data:
            return self.rightRotate(root)

        if balance > 1 and value > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and value > root.right.data:
            return self.leftRotate(root)

        if balance < -1 and value < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        #similarly we have other cases

        #this function has to return the root because the root of the tree/subtree can change
        return root


    def leftRotate(self, node:Node):
        print("leftrotate")
        temp = node.right
        node.right = temp.left
        if temp.left != None:
            temp.left.parent = node
        temp.left = node
        temp.parent = node.parent
        node.parent = temp
        node.height =self.height(node)
        temp.height = self.height(temp)
        return temp

    def rightRotate(self, node:Node):
        print("rightRotate")
        temp = node.left
        node.left = temp.right
        temp.parent = node.parent
        temp.right = node
        node.parent = temp
        node.height = self.height(node)
        temp.height = self.height(temp)
        return temp

    def height(self, node: Node):
        if node == None:
            return -1
        else:
            height = 0
            if node.left == None and node.right == None:
                node.height = 0
                return 0
            else:
                if node.left != None:
                    height = node.left.height

                if node.right != None:
                    if node.right.height > height:
                        height = node.right.height
            return height + 1

    def contain(self,value,node:Node):

        print("Current node is ", node.data)
        if node.data == value:
            print("Value found!")
            return

        if value < node.data:
            if node.left != None:
                self.contain(value, node.left)
            else:
                print("Value not found !")
                return
        else:
            if node.right != None:
                self.contain(value, node.right)
            else:
                print("Value not found !")
                return

        return


    def inOrderTraverse(self, node: Node):
        #first process left node
        if node.left != None:
            self.inOrderTraverse(node.left)

        #then process root node
        print(node.data, "(", node.height, ")", end=" - ")

        #then process right node
        if node.right != None:
            self.inOrderTraverse(node.right)

        return

    def postOrderTraverse(self, root: Node):
        #left - right - root

        if root == None:
            return

        self.postOrderTraverse(root.left)

        self.postOrderTraverse(root.right)

        print(root.data, "(", root.height, ")", end=" - ")

        return


    def preOrderTraverse(self, root: Node):
        #root - left - right

        if root == None:
            return

        print(root.data, "(", root.height, ")", end=" - ")

        self.preOrderTraverse(root.left)

        self.preOrderTraverse(root.right)

        return

input_array = [53, 47, 89, 71, 32, 18, 22, 51]
newtree = BinarySearchTree(15)
for x in input_array:
    print("")
    print("Adding", x)
    newtree.root = newtree.insert(x, newtree.root)

newtree.contain(71, newtree.root)
newtree.contain(32, newtree.root)
newtree.contain(99, newtree.root)
print("inOrderTraverse")
newtree.inOrderTraverse(newtree.root)
print("\npostOrderTraverse")
newtree.postOrderTraverse(newtree.root)
print("\npreOrderTraverse")
newtree.preOrderTraverse(newtree.root)

