


"""
Linked lists
"""

"""

Boundary Conditions:

 - Empty data structure
 - Single element in the data structure
 - Adding/Removing at the beginning of thedata structure
 - Adding/Removing at the end of the data structure
 - Working in the middle of the data structure
 
 - Node class
 - Linked List class
 - addFirst
 - addLast
 - removeFirst
 - removeLast
"""

class Node:
    def __init__(self,value):
        self.next = None
        self.data = value

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.currentSize = 0

    def addFirst(self, value):
        newNode = Node(value)

        if self.head == None:
            self.head = self.tail = newNode
            self.currentSize += 1
            print("Node added to empty list", value)
            return

        newNode.next = self.head
        self.head = newNode
        self.currentSize += 1
        print("Node added", value)

        return

    def printElements(self):
        temp = self.head
        while temp.next != None:
            print(temp.data, end=" - ")
            temp = temp.next
        print("None")

    def addLast(self, value):
        newNode = Node(value)

        #check if list is empty
        if self.head == None:
            self.head = self.tail = newNode
            self.currentSize += 1
            print("Node added to empty list", value)
            return

        self.tail.next = newNode
        self.tail = newNode
        self.currentSize += 1
        print("Node added", value)

        return

    def removeFirst(self):

        #check to see if list is empty
        if self.head == None:
            return None

        #we have a tail - check to see if list has only one element
        if self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            self.currentSize -= 1
            return data

        #regular case
        data = self.head.data
        self.head = self.head.next
        self.currentSize -= 1
        return data

    #Singly linked list - so we have to traverse from first to second last node
    def removeLast(self):

        #check is list is empty
        if self.head == None:
            return None

        #check if list has only one element
        if self.head == self.tail:
            data = head.data
            self.head = self.tail = None
            return data

        #regular traversal and removal - we need 2 temp pointers
        prev = None
        curr = self.head

        while curr != self.tail:
            #OR curr.next != None
            prev = curr
            curr = curr.next

        data = curr.data
        self.tail = prev
        prev.next = None

        return data

    #find node containig this value and remove it
    def find_and_remove(self, value):

        #singly linked list - so have to iterate over all nodes to find the node
        #need 2 pointers
        #need to check for empty list, single element list, found at beginning, found at end and found in the middle

        #if list is empty
        if self.head == None:
            return None

        #if list has 1 element only
        if self.head == self.tail:
            if self.head.data == value:
                self.removeFirst()

        #2 pointers
        prev = None
        curr = self.head

        while curr != None:
            if curr.data == value:
                #we need to remove this node
                #are we removing first node ?
                if curr == self.head:
                    return self.removeFirst()
                    #are we removing last ?
                elif curr == self.tail:
                    return self.removeLast()
                    #we must be removing in the middle
                else:
                    data = curr.data
                    prev.next = curr.next
                    curr.next = None
                    return data
            prev = curr
            curr = curr.next

        return None


    def create_looped_linked_list(self, position, input_array):
        counter = 0
        temp = Node(None)

        #add elements from the array to the linked list
        for x in input_array:
            self.addLast(x)
            #increment counter for each add
            counter += 1
            #check if we have reached the given position
            if counter == position:
                #when we do - store that pointer in temp
                temp = self.tail
        # once we reach end of the array - point last node to temp
        self.tail.next = temp

    def detect_loop(self):
        p = self.head
        q = self.head

        while True:
            #p moves 1 step
            p = p.next
            #q moves 2 steps
            if q.next == None:
                print("There is no loop")
                return
            elif q.next.next == None:
                print("There is no loop")
                return
            q = q.next.next

            if p == q:
                break

        print("There is a loop")

        p = self.head
        counter = 1
        while p != q:
            q = q.next
            p = p.next
            counter += 1

        print("Loop starts at position", counter)




newll = LinkedList()

array = [45, 63, 17, 22, 98, 54, 39]

for x in array:
    newll.addLast(x)

newll.printElements()

newll.removeFirst()

newll.printElements()

newll.removeLast()

newll.printElements()

newll.find_and_remove(22)

newll.printElements()
newll.detect_loop()

loopll = LinkedList()

looparray = [22, 33, 41, 87, 99, 19, 53, 76, 62, 13]
loopll.create_looped_linked_list(4, looparray)
loopll.detect_loop()


