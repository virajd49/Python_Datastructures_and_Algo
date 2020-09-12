



"""

Sorting algorithms


"""


def print_arr(array, sort_name):
    print("\nSorted by ", sort_name)
    for x in array:
        print(x, end=" ")




print("Sorting Algorithms ")
"""

Heap Sort

 - We treat the array as a max heap
 - We convert it into a max heap
 - And remove the largest element
 - repeat the process on the remaining array
 
 Time Complexity: O (n log n)
 Not a Stable sort
 In place sort
 
"""

def maxheapify(array, start_node, length):
    if length > 1:
        #core max heap principle
        #parent should be larger than both children

        largest = start_node

        #left_child
        l_child = 2*start_node + 1
        #right_child
        r_child = 2*start_node + 2

        if l_child < length and array[largest] < array[l_child]:
            largest = l_child

        if r_child < length and array[largest] < array[r_child]:
            largest = r_child

        #if we do need to swap,  then we need to maxheapify the swapped child's subtree as well
        if largest != start_node:
            array[largest], array[start_node] = array[start_node], array[largest]
            maxheapify(array, largest, length)

        return


def heap_sort(array):

    #length of the array
    l = len(array)

    #want to convert the array into a max heap
    #we need the last non leaf node as start node
    start_index = int(l/2) - 1
    #from start node to last node - do max heap operation
    for i in range(start_index, -1, -1):
        #call maxheapify
        maxheapify(array, i, l)

    #swap first and last
    #max heapify on array excluding last
    for last_element in range(l-1, 0, -1):
        #this needs to happen upto the point where last element is 1 - so loop needs to go upto 1
        array[0], array[last_element] = array[last_element], array[0]
        #this needs to happen upto the point where last element is 2 - so length of next array is 2 - but loop will go to 1 - so make a check in maxheapify
        maxheapify(array, 0, last_element)

    return


input_array = [7, 18, 93, 22, 45, 79, 56]
heap_sort(input_array)
print_arr(input_array, "Heap Sort")

"""

Quick Sort
 - pivot
 - move everything smaller than the pivot to the left
 - move everything greater than the pivot to the right
 - repeat the process on the two sub arrays on either side of the pivot
 
 Time Complexity: O (n log n)
 In place
 Not a stable sort
"""

def pivotize(array, start, end):

    #pivot
    pivot = array[end]

    #we need to iterate through the array and compare each element with the pivot
    #track the last swapped element
    #if current is smaller than pivot - increment swap counter and swap with pivot

    s = start - 1

    for i in range(start, end):
        if array[i] < pivot:
            s += 1
            array[s], array[i] = array[i], array[s]

    #bring pivot to middle
    array[end], array[s+1] = array[s+1], array[end]

    return s+1


def quick_sort(array, start, end):
    if start < end:
        #length of array
        l = len(array)

        #for current array

        #subfunction - pivotize
        #decide pivot
        #bring small to left
        #bring greater to right

        p = pivotize(array, start, end)

        #do above for left array
        #recursive call
        quick_sort(array, start, p-1)
        #do above for right array
        #recursive call
        quick_sort(array, p+1, end)

    return


input_array = [45, 33, 14, 21, 93, 6, 75]
end = len(input_array) - 1
quick_sort(input_array, 0, end)
print_arr(input_array, "Quick Sort")


"""
Insertion Sort

 - the array is split into two arrays
 - sorted array and unsorted array
 - we iterate through the array
 - at every element we find the right place for it in the sorted array and insert it there
 
 Time complexity: Worst and average case is O(n^2) - best case is O(n) - if the given array is already sorted and we want to insert a new element
 In place sort
 Is a stable sort
"""

def insertion_sort(array):

    #length of the array
    l = len(array)

    #interate through the array
    for i in range(1,l,1):
        #check if current is smaller then prev - if yes - we need to finc it's place in the sorted array
        if array[i] < array[i-1]:
            j = i
            while array[j] < array[j-1] and j > 0:
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1

    return


input_array = [45, 33, 14, 21, 93, 6, 75]
insertion_sort(input_array)
print_arr(input_array, "Insertion Sort")


"""
Merge Sort

 - Split the array into it's n individual elements
 - We sort them on the the way back up as we rebuild the array
 
 Time Complexity: O(n logn) - the max number of times that you can split an array into half is log n
 Not in place
 Stable
"""


def merge_sort(array):

    #length of the array
    l = len(array)

    if l > 1:

        middle = int(l/2)

        #first we split the array into half as many times as we can
        l_array = merge_sort(array[:middle])
        r_array = merge_sort(array[middle:])

        # we put the two halves together in such a way that they are sorted
        j = k = i = 0

        while j < len(l_array) and i < len(r_array):
            if l_array[j] < r_array[i]:
                array[k] = l_array[j]
                j += 1
                k += 1
            else :
                array[k] = r_array[i]
                i += 1
                k += 1

        while j < len(l_array):
            array[k] = l_array[j]
            j += 1
            k += 1

        while i < len(r_array):
            array[k] = r_array[i]
            i += 1
            k += 1

    return array

input_array = [45, 33, 14, 21, 93, 6, 75]
sorted_array = merge_sort(input_array)
print_arr(sorted_array, "Merge Sort")



"""
Selection Sort

 - iterate through the entire array
 - at every element, select the smallest element from the remaining array and replace it with the current element
 
 Time Complexity: O(n ^2)
 Not a stable sort
 In place sort
"""


def selection_sort(array):

    l = len(array)

    #iterate through the entire array
    for i in range(l):
        smallest = i
        for j in range(i+1, l):
            if array[j] < array[smallest]:
                smallest  = j
        if smallest != i:
            array[smallest], array[i] = array[i], array[smallest]

    return

input_array = [45, 33, 14, 21, 93, 6, 75]
selection_sort(input_array)
print_arr(input_array, "Selection Sort")



"""
Counting Sort

 - Operates within a given range for the values in the array
 - it is linear time complexity sort - but the complexity depends on the range of the values
 - we count the number of occurrances of each value in the given key range
 
 Time Complexity: O(n + range)
 Not an in place sort
 It is stable
"""



def counting_sort(array, key):

    #length of the array for our convenience
    l = len(array)

    #we need an array to store the count of every decimal place
    count_array = [0 for i in range(key)]

    #we need an array to put the sorted elements into
    sorted_array = [0 for j in range(l)]


    #count the the occurance of each elemnt
    for x in array:
        count_array[x] += 1

    #we adjust the count in such a way that it gives us the position of the value in the sorted array
    for i in range(1, key):
        count_array[i] = count_array[i] + count_array[i-1]

    #we place teh values into the sorted array as per the index in the count array
    for x in array:
        sorted_array[count_array[x]-1] = x
        count_array[x] -= 1

    return sorted_array

input_array = [1, 3, 4, 7, 2, 3, 4 ,1 ,1 ,7 ,8 ,4]
sorted_array = counting_sort(input_array, 10)
print_arr(sorted_array, "Counting Sort")


"""

Bubble Sort

 - for every iteration - compare all adjacent elements - if right is less than left - swap
 - reduce length
 
 Time Complexity: O(n^2)
 In place sort
 Stable
"""


def bubble_sort(array):


    #length of array
    l = len(array)

    #for decreasing lengths of the array
    for n in range(l, 1, -1):
        for i in range(1, n):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]

    return


input_array = [45, 33, 14, 21, 93, 6, 75]
bubble_sort(input_array)
print_arr(input_array, "Bubble Sort")



"""
Radix Sort

 - We sort the numbers in incremental steps using the digits in every decimal place
 - We use counting sort as a subroutine with a key of 10
 
 Time complexity: O(n)
 In place sort
 Not a stable sort
 
"""


def counting_sort_subroutine(array, exp):

    #length
    l = len(array)

    #array to hold the counts
    count_array = [0 for i in range(10)]

    #array to hold sorted values
    sorted_array = [0 for i in range(l)]


    #count the number of times the decimal place value occurs
    for x in array:
        index = (int(x/exp)) % 10
        count_array[index] += 1

    #modify the counts such that they give us the position of the element in the array
    for i in range(1,10):
        count_array[i] = count_array[i] + count_array[i-1]

    #place the values into the sorted array
    for x in reversed(array):
        index = (int(x/exp)) % 10
        sorted_array[count_array[index] - 1] = x
        count_array[index] -= 1


    return sorted_array



def radix_sort(array):

    #largest value - so that we know how many decimal places we need to sort
    largest = max(array) #python in build function - O(n)

    exp = 1

    while int(largest/exp) > 0:
        #counting sort subroutine
        array = counting_sort_subroutine(array, exp)
        #move to next decimal place
        exp *= 10

    return array



input_array = [45, 2, 567, 83, 111, 24, 385, 1826]
sorted_array = radix_sort(input_array)
print_arr(sorted_array, "Radix Sort")


print("\n")

print("Linked Lists ")
"""

Linked list

 - addFirst - O(1)
 - addLast - O(n)
 - removeFirst - O(1)
 - removeLast - O(n)
 - removeValue - O(n)
 - contains - O(N)
 - createLoop 
 - detectLoop A + N*B : where A + B = n, B is length of the loop
 - detectStartofLoop
 - reverseList  - O(n)
 
"""



class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def addFirst(self, value):

        newNode = Node(value)

        #check if list is empty
        if self.root == None:
            self.root = newNode
            return

        newNode.next = self.root
        self.root = newNode

        return


    def addLast(self, value):

        newNode = Node(value)


        #check if list is empty
        if self.root == None:
            self.root = newNode
            return

        #we need to iterate to the last element - actually second last element
        curr = self.root

        while curr.next != None:
            curr = curr.next

        #at this point curr is the last element
        curr.next = newNode

        return

    def removeFirst(self):

        #check if list is empty
        if self.root == None:
            return

        #check if list has only one element
        if self.root.next == None:
            self.root = None
            return

        temp = self.root
        self.root = temp.next
        temp.next = None

        return

    def removeLast(self):

        #check if list is empty
        if self.root == None:
            return

        #check if list has only one element
        if self.root.next == None:
            self.root = None
            return

        #we need to traverse to the second to last element
        curr = self.root
        prev = None

        while curr.next != None:
            prev = curr
            curr = curr.next

        #at this point curr is last node, prev is second to last node
        prev.next = None

        return

    def removeValue(self, value):

        #check if list is empty
        if self.root == None:
            return

        #check if list has only one value
        if self.root.next == None:
            if self.root.value == value:
                self.root = None
                print("Value found and removed !! ")
                return

        #else look through entire list
        curr = self.root
        prev = None

        while curr != None: #we want to evaluate the last node
            if curr.data == value:
                if prev == None:
                    #we are at the root
                    self.root = curr.next
                    curr.next = None
                    print("Value found and removed !! ")
                    return
                else:
                    #we are somewhere in teh middle of the list
                    prev = curr.next
                    curr.next = None
                    print("Value found and removed !! ")
                    return
            else:
                prev = curr
                curr = curr.next

        #if we get here that means we went through the entire list and did not find the value
        print("Value not found !!")

        return

    def contains(self, value):

        #check if list is empty
        if self.root == None:
            print("List is empty !! Does not contain value")
            return

        curr = self.head

        while curr != None:
            if curr.data == value:
                print("List contains given value !! ")
                return
            curr = curr.next

        #if we get here, that means we did not find the given value
        print("List does not contain given value !! ")

        return

    def createLoop(self, position):

        counter = 1
        hook = None
        latch = None

        #check if list is empty
        if self.root == None:
            print("List is empty - cannot create loop ! ")
            return

        curr = self.root

        while curr != None: # we want to evaluate the last node
            if counter == position:
                latch = curr
            if counter > position and latch == None:
                print("Cannot create loop at given position - out of bounds ")
                return
            if curr.next == None: #we are the last node
                hook = curr
            curr = curr.next
            counter += 1

        #then we make end point to position
        hook.next = latch
        print("\nLoop created at position", position)


    def detectLoop(self):
        #hare and tortoise method

        #check if list is empty
        if self.root == None:
            print("\nList is empty - there is no loop - because there is no list")
            return False

        h = self.root
        t = self.root

        while h.next != None:
            t = t.next
            if h.next.next != None:
                h = h.next.next
            else:
                print("\nThere is no loop !")
                return

            if t == h:
                print("\nLoop detected !")
                t = self.root
                counter = 1
                while t != h:
                    counter += 1
                    t = t.next
                    h = h.next
                print("\nLoop starts at position", counter)
                return True

        print("\nThere is no Loop in the list !")

        return False

    def getLoopStart(self):
        h = self.root
        t = self.root

        while h.next != None:
            t = t.next
            if h.next.next != None:
                h = h.next.next
            else:
                print("\nThere is no loop !")

            if t == h:
                t = self.root
                counter = 1
                while t != h:
                    counter += 1
                    t = t.next
                    h = h.next
                return counter

    def reverseList(self):

        #check if list is empty
        if self.root == None:
            print("\nList is empty - cannot reverse a list if it is empty !! ")
            return

        #we need three pointers to reverse the list
        prev = None
        curr = self.root
        next = None

        while curr != None:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        self.root = prev

        return

    def printList(self):

        #has to be immune to loops

        #check if list is empty
        if self.root == None:
            print("root - None")
            return

        hasLoop = self.detectLoop()
        if hasLoop:
            loopStart = self.getLoopStart()
            counter = 1
            curr = self.root
            print("root ", end="")
            while counter != loopStart:
                print(" -", curr.data, end="")
                curr = curr.next
                counter += 1

            print(" -", curr.data, end="")
            looper = curr
            curr = curr.next

            while curr != looper:
                print(" -", curr.data, end="")
                curr = curr.next

            print(" - loops back to ", looper.data)

        else:
            curr = self.root
            print("root", end="")
            while curr != None:
                print(" -",curr.data, end="")
                curr = curr.next

        return


input_array = [45, 2, 567, 83, 111, 24, 385, 1826]
new_list = LinkedList()
for x in input_array:
    new_list.addFirst(x)
new_list.printList()

new_list.addFirst(75)
new_list.addFirst(84)
new_list.printList()

new_list.removeFirst()

new_list.removeLast()
new_list.printList()

new_list.reverseList()
new_list.printList()

new_list.createLoop(4)
new_list.printList()



print("\n Binary Search Tree")


"""
BST

  - insert
        - self balancing
  - height
  - preordertraversal
  - postordertraversal
  - onordertraversal
  - levelordertraversal
  
  - contains
  - remove
  - findsuccesssor
  - findpredecessor
  
"""

class bstNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        self.height = 0


class BST():
    def __init__(self):
        self.root = None


    def insert(self, root: bstNode, value):

        #tree needs to balance itself everytime we insert
        #every time we make an insertion at a subtree - the node above expects to get the updated child back - function should return the new root
        #recursive

        #decide if we insert in this subtree or move to the next
        if root == None:
            root = bstNode(value)
            return root
        if value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        #after the insertion we need to calculate the height fo the current node
        #call height function
        root.height = self.height(root)

        #check balance
        #height difference between left and right child should not be more than 1
        balance = self.height(root.left) - self.height(root.right)

        #4 cases to look at
            #balance > 1 and value < left child
            #balance > 1 and value > left child
            #balance < -1 and value > right child
            #balance < -1 and value < right child

        if balance > 1 and value < root.left.data:
            #rightRotation on root
            return self.right_rotate(root)
        if balance > 1 and value > root.left.data:
            #leftRightRotation
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and value > root.right.data:
            #leftRotation on root
            return self.left_rotate(root)
        if balance < -1 and value < root.right.data:
            #rightLeftRotation
            root.right = self.left_rotate(root.right)
            return self.right_rotate(root)

        return root

    def height(self, root: bstNode):
        if root == None:
            return -1

        return max(self.height(root.left), self.height(root.right)) + 1


    def right_rotate(self, root:bstNode):
        temp  = root.left
        root.left = temp.right
        temp.right = root
        root.height = self.height(root)
        return temp

    def left_rotate(self, root: bstNode):
        temp = root.right
        root.right = temp.left
        temp.left = root
        root.height = self.height(root)
        return temp

    def remove(self, root, value):

        #first we need to traverse to the value we want to remove
        #we may not find the value - so we need to let the user know if that is the case
        if root == None:
            return None
        if value == root.data:
            if root.left == None and root.right == None:
                return None
            elif root.right == None:
                root.left, succ = self.successor(root.left)
                root.data = succ
            else:
                root.right, pred = self.predeccessor(root.right)
                root.data = pred

        elif value > root.data:
            root.right = self.remove(root.right, value)
        else:
            root.left = self.remove(root.left, value)

        #when/if we do find the value - we then need to find it's successor
        #store the successor value
        #remove the successor
        #replace the found value with the successor value
        #what is a successor ? - the largest value smaller than the current value
        return root


    def successor(self, root):

        #keep going right
        if root.right == None:
            #this is it
            if root.left == None:
                return None, root.data
            else:
                return root.left, root.data

        else:
            root.right, successor = self.successor(root.right)

            root.height = self.height(root)
            return root, successor


    def predeccessor(self, root):
        # keep going left
        if root.left == None:
            # this is it
            if root.right == None:
                return None, root.data
            else:
                return root.right, root.data

        else:
            root.left, predeccessor = self.successor(root.left)

            root.height = self.height(root)
            return root, predeccessor


    def pre_order_traversal(self, root):

        #root - left - right
        if root == None:
            return

        print(root.data, " -", end="")

        self.pre_order_traversal(root.left)

        self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):

        #left - right - root

        if root == None:
            return

        self.post_order_traversal(root.left)

        self.post_order_traversal(root.right)

        print(root.data, " -", end="")

    def in_order_traversal(self, root):
        #left - root - right
        if root == None:
            return

        self.in_order_traversal(root.left)

        print(root.data, " -", end="")

        self.in_order_traversal(root.right)

    def level_order_traversal(self, root: bstNode):

        level: [bstNode] = [root]

        while level:
            new_level: [bstNode] = []
            for node in level:
                print(node.data, " -", end="")
                if node.left != None:
                    new_level.append(node.left)
                if node.right != None:
                    new_level.append(node.right)
            level = new_level

        return


input_array = [56, 9, 6, 44, 105, 72, 33, 21, 0, 5]
newtree = BST()
for x in input_array:
    #print("\nAdding", x)
    newtree.root = newtree.insert(newtree.root, x)
    #print("")
print("\nIn Order traversal")
newtree.in_order_traversal(newtree.root)

print("\n Post Order traversal")
newtree.post_order_traversal(newtree.root)

print("\n Pre Order Traversal")
newtree.pre_order_traversal(newtree.root)

print("\n Level Order Traversal")
newtree.level_order_traversal(newtree.root)

newtree.remove(newtree.root, 6)

print("\nIn Order traversal")
newtree.in_order_traversal(newtree.root)

newtree.insert(newtree.root, 6)

print("\nIn Order traversal")
newtree.in_order_traversal(newtree.root)

newtree.remove(newtree.root, 9)

print("\nIn Order traversal")
newtree.in_order_traversal(newtree.root)






