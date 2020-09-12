

"""
Linked Lists

Slower than arrays
Not a fixed size

Singly linked
Doubly linked
With tail
Without tail

things to do with linked list

addFirst - constant time
addLast - constant time if we have tail - else O(n)
removeFirst - constant time
removeLast - constant time if we have a tail - else O(n)
removeValue - could be anywhere O(n)
insertInMiddle - O(n)

contains - O(n)
findAndRemove - O(n)

detectLoop - m + l * c - where m + l = n - so it is O(n)
returnStart of loop - m = n - l - so O(n)

reverse a linked list - we need to do today

"""

class Node:
    def __init__(self,value):
        self.next = None
        self.data = value


class LinkedList:
    def __init__(self):
        self.head = None
        #no tail node


    def addFirst(self,value):
        #create new Node
        newNode = Node(value)

        #if list is empty
        if self.head == None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode
        return

    def addLast(self, value):
        #create a new Node
        newNode = Node(value)

        #if list is empty
        if self.head == Node:
            self.head = newNode
            return

        temp = self.head

        #iterate till we reach last node - O(n)
        while temp.next != None:
            temp = temp.next

        temp.next = newNode
        return

    def removeFirst(self):

        #if list is empty
        if self.head == None:
            return

        #if list has only one element
        if self.head.next == None:
            self.head = None
            return

        temp = self.head
        self.head = self.head.next
        temp.next = None
        return

    def removeLast(self):
        #we have no tail  - so iterate to last - need 2 pointer = for singly linked list

        #if list is empty
        if self.head == None:
            return

        #if list has only one element:
        if self.head.next == None:
            self.head = None
            return

        #iterate to last and remove
        temp1 = None
        temp2 = self.head
        while temp2.next != None:
            temp1 = temp2
            temp2 = temp2.next

        temp1.next = None
        return

    def removeValue(self, value):

        #if list is empty
        if self.head == None:
            print("List is empty!")
            return

        #if first element has the value we are looking for
        if self.head.data == value:
            print("Found a node with given value - removing!")
            self.head = None
            return

        #iterate - we will need two pointers
        temp1 = None
        temp2 = self.head
        while temp2.next != None:
            #already checked for first element - so we first increment  - then compare
            temp1 = temp2
            temp2 = temp2.next

            if temp2.data == value:
                temp1.next = temp2.next
                temp2.next = None
                print("Found the value - removing !")
                return

        #if we reach here we are at the end of the list and we did not find the value
        print("Did not find the value we are looking for!")
        return

    def loopTheListAtPosition(self, pos):
        #For position - we number starting with 1 - 1, 2, 3, 4, 5

        #if list is empty:
        if self.head == None:
            print("Your list is empty - cannot loop an empty list!")
            return

        #to create a loop - we need to point the last node to the node at the given position
        #so we need access to both nodes at the same time
        #so we need two pointers - we need to iterate through the entire list
        #One for storing the given position
        #second to iterate to the last element
        #we also need a counter to keep track of the position we are at

        position = None
        lastNode = self.head
        pos_count = 0
        while lastNode.next != None:
            #first node can be the given position - looping on single node
            #so we first compare and then iterate
            pos_count += 1
            if pos_count == pos:
                position = lastNode

            lastNode = lastNode.next

        if position != None:
            #given position was within list length
            #point last node to node at position
            lastNode.next = position
            print("Loop created at position", pos)
        else:
            #given position was out of length bound
            print("Given position is out of list bounds! Loop not created - please provide position within list bounds")

        return

    def detectIfLoopExists(self):

        #if list is empty
        if self.head == None:
            print("List is empty - an empty list can have no LOOP!")
            return

        #hare and tortoise approach
        #two pointers
        h = self.head
        t = self.head

        #if we reach the end of the List - we catch that and return saying there is no loop
        while h.next != None:
            t = t.next

            if h.next.next != None:
                h = h.next.next
            else:
                print("List has no LOOP!")
                return

            if t == h:
                print("List has a LOOP")
                return

        print("List has no LOOP!")
        return

    def detectStartOfLoop(self):
        #first detect if loop exists
        #hare and tortoise approach

        #check if list is empty
        if self.head == None:
            print("List is empty - empty list cannot have a LOOP!")
            return

        #two variables - hare and tortoise
        h = self.head
        t = self.head

        while h.next != None:
            t = t.next

            if h.next.next != None:
                #move two nodes ahead
                h = h.next.next
            else:
                #we reached end of the list
                print("List has no LOOP!")
                return

            if t == h:
                #we found a loop
                break

        if t == h:
            #we found a loop so now find starting point
            t = self.head
            #if we number positions as 1,2,3,4...
            position = 1
            while t != h:
                t = t.next
                h = h.next
                position += 1
            print("Start of loop found at position", position)
            return position

        else:
            #list has no loop
            print("List has no LOOP!")
            return None

    def printAll(self):
        #make this loop aware

        #empty list
        if self.head == None:
            print("Head -> None")
            return

        loopPos = self.detectStartOfLoop()
        if loopPos == None:
            temp = self.head
            print("Head", end=" -> ")
            while temp != None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")
        else:
            counter = 1
            #first we count from head to start of loop
            temp = self.head
            while counter != loopPos:
                print(temp.data, end=" -> ")
                counter += 1
                temp = temp.next
            temp2 = temp
            print(temp2.data, end=" -> ")
            temp2 = temp2.next
            while temp2 != temp:
                print(temp2.data, end=" -> ")
                temp2 = temp2.next
            print("Loops back to node",loopPos)

    def reverseList(self):

        #if list is empty
        if self.head == None:
            print("Empty list! cannot reverse!")

        #if list has only one elemnent
        if self.head.next == None:
            print("List has single element only - cannot reverse !")
        #first try with 3 pointers
        prev = None  #NODE 1
        curr = self.head #NODE 2
        next = None #NODE 3

        while curr != None:
            next = curr.next
            curr.next = prev
            #we are done with prev
            prev = curr
            curr = next

        self.head = prev

    def reverseList2(self):

        #check if list is empty
        if self.head == None:
            print("List is empty cannot reverse an empty List!")
            return

        #check if list has only one element
        if self.head.next == None:
            print("List has only one element - cannot reverse a single element!")
            return

        #we need 3 pointers
        prev = None
        curr = self.head
        next = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev
        return





array = [22, 56, 71, 89, 17, 45, 64, 90, 28, 65]

newll = LinkedList()

for x in array:
    newll.addFirst(x)

newll.printAll()

newll.removeFirst()
newll.printAll()
newll.removeLast()
newll.printAll()
newll.removeValue(43)
newll.printAll()
newll.removeValue(17)
newll.printAll()
newll.addFirst(103)
newll.printAll()
newll.reverseList()
newll.printAll()
newll.reverseList2()
newll.printAll()
newll.detectIfLoopExists()
newll.detectStartOfLoop()
newll.loopTheListAtPosition(3)
newll.detectIfLoopExists()
newll.detectStartOfLoop()
newll.printAll()


