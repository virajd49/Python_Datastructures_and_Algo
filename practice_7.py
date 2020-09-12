

"""

Linked Lists

"""


#def a node class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

#def linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        #no tail node for this one

    #addFirst
    def addFirst(self,value):

        newNode = Node(value)

        #check if list is empty
        if self.head == None:
            #list is empty
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode

        return

    #addLast
    def addLast(self, value):

        newNode = Node(value)

        #if list is empty
        if self.head == None:
            self.addFirst(value)
            return

        #we need two pointers
        curr = self.head
        prev = None

        #we need to reach last element
        while curr.next != None:
            prev = curr
            curr = curr.next

        #now curr is last node and prev is second last node
        newNode.next = None
        curr.next = newNode

        return

    #removeFirst
    def removeFirst(self):

        #check if list is empty
        if self.head == None:
            print("List is empty!!")

        #if list has only one element
        if self.head.next == None:
            self.head = None
            return

        temp = self.head

        self.head = temp.next
        temp.next = None

        return

    #removeLast
    def removeLast(self):

        #check if list is empty
        if self.head == None:
            print("List is empty!!!")
            return

        #if list has only one element:
        if self.head.next == None:
            self.head = None
            return

        #we have to traverse to the last node and then remove it
        curr = self.head
        prev = None

        while curr.next != None:
            prev = curr
            curr = curr.next

        #at this point curr is last node, prev is second last node
        prev.next = None

        return

    # findAndRemove
    def findAndRemove(self, value):

        #check if list is empty:
        if self.head == None:
            print("List is empty!!!")

        prev = None
        curr = self.head

        while curr != None:
            if curr.data == value:
                break
            prev = curr
            curr = curr.next

        if curr != None:
            #at this point curr is the node we want to remove
            prev.next = curr.next
            curr.next = None
            print(value, "removed !")
            return
        else:
            print("List does not contain given value")

        return

    #loopTheListFunction
    def loopTheList(self, position):

        #check for empty list
        if self.head == None:
            print("List is empty!!!")
            return

        #if list has single element
        if self.head.next == None and position == 1:
            self.head.next = self.head
            print("List Looped !!!")
            return

        counter = 1
        latch = None
        key = self.head

        while key.next != None:
            if counter == position:
                #we are at the start if the loop - grab the latch
                latch = key
            key = key.next
            counter += 1

        #at this point key is the last node and latch is the node where we want the loop to start
        if latch != None:
            print("position was within length of the list")
            key.next = latch
            print("List Looped !!!")
            return
        else:
            print("Given position is not within the length of the list")
            print("Loop not created !!!")
            return

    #detectLoopFunction
    def detectLoop(self):

        #hare and tortoise method

        #check if list is empty
        if self.head == None:
            print("List is empty")
            return False

        t = h = self.head

        while h.next != None:
            t = t.next
            h = h.next
            if h.next != None:
                h = h.next
            else:
                print("We reached the end of the list - there is No Loop")
                return False

            if t == h:
                print("Loop Detected !!!")
                return False
        print("We reached the end of the list - there is No Loop ")

        return False


    #findLoopStartFunction
    def findLoopStartFunction(self):

        #first detect loop and bring h and t into position
        if self.head == None:
            print("List is empty - so no loop can exist !")
            return 0

        #detect loop - h and t method

        t = h = self.head

        while h.next != None:
            t = t.next
            h = h.next
            if h.next != None:
                h = h.next
            else:
                print("we have reached the end of the list - there is no loop")
                return 0

            #we have incremented t by 1 and h by two - so now compare them
            if t == h:
                print("we found a loop!")
                break
        if t == h:
            #we let h stay where it is
            #reinitialize t
            t = self.head
            counter = 1
            while t != h:
                t = t.next
                h = h.next
                counter += 1
            print("Loop starts at position", counter)
            return counter
        else:
            print("There is no loop")
            return 0


    #reverseTheList
    def reverseList(self):

        #if list is empty
        if self.head == None:
            print("List is empty - cannot reverse an empty list")
            return

        #if list has one element
        if self.head.next == None:
            print("List has only one element - cannot reverse single element list")
            return

        prev = None
        curr = self.head
        next = None

        while curr.next != None:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

        return

    def printList(self):

        if self.head == None:
            print("Head -> None")
            return

        loopPosition = self.findLoopStartFunction()
        if loopPosition > 0 :
            print("There is a loop !")
            loopPosition = self.findLoopStartFunction()
            counter = 1
            curr = self.head
            print("Head ->", end=" ")
            while counter != loopPosition:
                print(curr.data, " ->", end=" ")
                curr = curr.next
                counter += 1

            loopNode = curr
            print(curr.data, " ->", end=" ")
            curr = curr.next

            while curr != loopNode:
                print(curr.data, " ->", end=" ")
                curr = curr.next

            print("Loops back to ", loopNode.data)
            return
        else:

            curr = self.head
            print("Head ->", end=" ")
            while curr != None:
                print(curr.data,"->", end=" ")
                curr = curr.next
            print(None)

        return

    def createListFromArray(self, array):

        for x in array:
            self.addFirst(x)


input_array = [65, 71, 23, 44, 89, 12, 6, 5, 34, 27]
newll = LinkedList()
newll.createListFromArray(input_array)
newll.printList()

newll.addFirst(18)
newll.printList()
newll.addLast(38)
newll.printList()

newll.findAndRemove(49)
newll.findAndRemove(44)
newll.printList()

newll.reverseList()
newll.printList()

newll.detectLoop()

newll.loopTheList(5)
newll.detectLoop()
newll.findLoopStartFunction()
newll.printList()










