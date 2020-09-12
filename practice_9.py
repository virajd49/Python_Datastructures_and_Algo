





"""

Self balancing BST

"""


class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.data = value
        self.height = 0

class SB_BST:
    def __init__(self):
        self.root : Node = None

    #insert function

    def insert(self, root, value):

        #do regular inserts - recursive
        if root == None:
            return Node(value)

        if value > root.data:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)

        #update heights
        root.height = self.height(root)

        #check for imbalance
        balance = self.height(root.left) - self.height(root.right)

        # correct imbalance with rotations
        if balance > 1 and value < root.left.data:
            #rightRotate on root
            print("rightrotate on", root.data)
            return self.right_rotate(root)

        if balance > 1 and value > root.left.data:
            print("leftrightrotate on", root.data)
            #left rotate on root.left
            root.left = self.left_rotate(root.left)
            #right rotate on root
            return self.right_rotate(root)

        if balance < -1 and value > root.right.data:
            print("leftrotate on", root.data)
            #left rotate on root
            return self.left_rotate(root)

        if balance < -1 and value < root.right.data:
            print("rightleftrotate on", root.data)
            #right rotate on root.right
            root.right = self.right_rotate(root.right)
            #left rotate in root
            return self.left_rotate(root)

        # has to return newly rotated root to parent node
        return root
        #has to return newly rotated root to parent node

    #height function
    def height(self, root):

        if root == None:
            return -1
        else:
            height = 0
            if root.left == None and root.right == None:
                root.height = 0
                return 0
            if root.left != None:
                height = root.left.height
            if root.right != None:
                if root.right.height > height:
                    height = root.right.height
            return height + 1


    #left rotate function
    def left_rotate(self, root):

        temp = root.right
        root.right = temp.left
        temp.left = root
        root.height = self.height(root)
        return temp

    #right rotate function
    def right_rotate(self, root):

        temp = root.left
        root.left = temp.right
        temp.right = root
        root.height = self.height(root)
        return temp

    #BINARY SEARCH BROOO
    def does_it_contain(self, root, value):

        if root == None:
            print("Tree does not contain ", value)
            return

        if root.data == value:
            print("Value found !!!")
            return
        elif value > root.data:
            #go to the right
            self.does_it_contain(root.right, value)
        else:
            #go to the left
            self.does_it_contain(root.left, value)

        return

    def delete_this_value(self, root, value):

        #BST till we find the given value
        if root == None:
            return root
        if value > root.data:
            root.right = self.delete_this_value(root.right, value)
        elif value < root.data:
            root.left = self.delete_this_value(root.left, value)
        elif value == root.data:

            #check if leaf node/has any children
            if root.left == None and root.right == None:
                return None
            elif root.left == None or root.right == None:
                #it has one child
                if root.left != None:
                    return root.left
                else:
                    return root.right
            else:
                #it has two children
                #we need to find successor  - largest smaller than given value
                #traverse right on the left child
                to_be_deleted = root
                root.left = self.find_successor(to_be_deleted, root.left)

        return root

    def find_successor(self, delete_node, root):

        if root.right == None:
            #i am the successor
            print("I am the successor", root.data)
            delete_node.data = root.data
            return None
        else:
            root.right = self.find_successor(delete_node, root.right)

        return root

    #InOrderTraverse print function
    def in_order_traverse(self, root):
        #left - root - right

        if root == None:
            return

        self.in_order_traverse(root.left)

        print(root.data, "(", root.height, ")",end=" - ")

        self.in_order_traverse(root.right)

        return

    #preOrderTraverse print function
    def pre_order_traverse(self, root):
        #root left right

        if root == None:
            return

        print(root.data, "(", root.height, ")",end=" - ")

        self.pre_order_traverse(root.left)

        self.pre_order_traverse(root.right)

        return

    #postOrderTraverse print function
    def post_order_traverse(self, root):
        # left - right - root

        if root == None:
            return

        self.post_order_traverse(root.left)

        self.post_order_traverse(root.right)

        print(root.data, "(", root.height, ")",end=" - ")

        return



input_array = [56, 9, 6, 44, 105, 72, 33, 21, 0, 5]
#input_array = [15,53, 47, 89, 71, 32, 18, 22, 51]
newtree = SB_BST()
for x in input_array:
    print("\nAdding", x)
    newtree.root = newtree.insert(newtree.root, x)
    print("")
    newtree.in_order_traverse(newtree.root)

newtree.does_it_contain(newtree.root, 6)
newtree.does_it_contain(newtree.root, 111)

print("in order traverse")
newtree.in_order_traverse(newtree.root)


print("\npost order traverse")
newtree.post_order_traverse(newtree.root)


print("\npre order traverse")
newtree.pre_order_traverse(newtree.root)
print("\n")
print(newtree.root.data)

newtree.delete_this_value(newtree.root, 9)

print("in order traverse")
newtree.in_order_traverse(newtree.root)
