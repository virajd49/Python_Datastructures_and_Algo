


def print_array(array, sort_name):
    print("")
    print("Sorted by ", sort_name)
    for x in array:
        print(x, end=" ")
"""
Heap Sort

 - You converting your array into a Max Heap
 - Max heap - basic principle - Every parent node should be greater than both it's children
 - Switch the first and last nodes - remove the last node
 - repeat the make max - switch - remove process on the remaining heap - till you end up with a single node.

 Complexity: n log(n)
"""

input_array = [97, 16, 53, 7, 111, 42]

#maxheapify function
def maxheapify(start_index, array, array_length):

    largest = start_index
    l = array_length

    #left child
    l_child = 2*start_index + 1

    #right child
    r_child = 2*start_index + 2

    if l_child < l and array[largest] < array[l_child]:
        largest = l_child

    if r_child < l and array[largest] < array[r_child]:
        largest = r_child

    if largest != start_index:
        swap = array[largest]
        array[largest] = array[start_index]
        array[start_index] = swap
        maxheapify(largest, array,l)

#find largest among parent, left child and right child
#if parent is not largest - swap parent and largest
#call maxheapify on the swapped position


#main_function

def heap_sort(array):

    n = len(array)
    start_index = int((n/2)) - 1

#converting into max heap
 #start with last leaf less node: (n/2) - 1
 #call maxheapify function
    for i in range(start_index, -1, -1):
        maxheapify(i,array,n)

    for last_element in range(n-1,0,-1):
        swap = array[last_element]
        array[last_element] = array[0]
        array[0] = swap
        maxheapify(0,array,last_element)
    return array
#swap first and last
#remove last
#maxheapify on (array - last)
#repeat

input_array = [97, 16, 53, 7, 111, 42]

sorted_array = heap_sort(input_array)
print_array(sorted_array, "Heap Sort")

"""
QuickSort

- We select a pivot
- We move all elements less than the pivot to the left
- Move all elements greater than the pivot to the right
- Repeat above three operations on left and right groups

Complexity - nlog(n)
- quicksort is in place


input_array = [97, 16, 53, 7, 111, 42]

#main operation

def partition(array, start, end):

#select pivot
    pivot = end
#position of the last swapped element
    s = start - 1

#iterate from 0 to pivot - 1
    for i in range(start,pivot,1):
        if array[i] < array[pivot]:
            s += 1
            array[i], array[s] = array[s], array[i]
#if less than pivot swap with 'last swapped element' + 1

#bring pivot to center
    array[s+1], array[pivot] = array[pivot], array[s+1]
#return postion of pivot
    return s+1


def quick_sort(array, start, end):
    if start < end:
        #m = mainoperation (array)
        m = partition(array, start, end)

        #recurse(left array)
        quick_sort(array,start,m-1)
        #recurse(right array)
        quick_sort(array,m+1,end)


quick_sort(input_array,0,len(input_array)-1)
print_array(input_array, "Quick Sort")
"""
"""
 - need to convert the array into a maxheap
    - we start with the last leaf less node:(n/2) - 1 and we keep going till pos 0
    - on every node we find the largest of parent, l child, r child - and swap so that parent is largest
    - run same comparison on swapped child sub tree
    
 - we need to swap first and last
 - then run above process on sub arrays formed by removing last element
 - call above operations with repeated n-1
"""

def new_maxheapify(array,start_node,length):

    #find largest

    largest = start_node
    l_child = 2*start_node + 1
    r_child = 2*start_node + 2

    if l_child < length and array[largest] < array[l_child]:
        largest = l_child

    if r_child < length and array[largest] < array[r_child]:
        largest = r_child

    if largest != start_node:
        #swap
        array[largest], array[start_node] = array[start_node], array[largest]
        new_maxheapify(array, largest, length)


def new_heap_sort(array):

    #convert to max heap
    n = len(array)
    start_index = int(n/2)- 1

    for i in range(start_index,-1,-1):
        new_maxheapify(array, i, n)

    #for reducing length of the array
    for j in range(n-1,0,-1):
        #swap
        array[j], array[0] = array[0], array[j]
        new_maxheapify(array, 0, j-1)

    return array

input_array = [97, 16, 53, 7, 111, 42]
new_heapsorted_array = new_heap_sort(input_array)
print_array(new_heapsorted_array, "New Heap Sort")

"""
Quick Sort
 - we select a pivot
 - we move everythin less than the pivot to the left
 - we move everything greater than the pivot to the right
 - we repeat the above on the left and the right sub arrays
"""

#function that does the comparision, the moving of elements and gives the position of the partition

def partition(array, start, end):

    pivot = end

    #need a variable to mark the last swapped element
    s = start - 1

    #iterate from start to pivot - 1 and do the comparison + moving
    for i in range(start, pivot, 1):
        if array[i] < array[pivot]:
            s += 1
            array[s], array[i] = array[i], array[s]

    array[s+1], array[pivot] = array[pivot], array[s+1]

    return s+1


def quick_sort(array, start, end):
    if start < end:
        m = partition(array, start, end)
        quick_sort(array, start, m-1)
        quick_sort(array, m+1, end)

input_array = [45, 66, 213, 9, 15, -8]
quick_sort(input_array, 0, (len(input_array)-1))
print_array(input_array, "latest quick sort")


"""
Insertion Sort

 - dividing the array into two parts - sorted array and unsorted array
 - iterate through the array - for every element - we find the right location in the sorted array and insert it there.
 - sorted array starts from left and ends before current element
 
 Complexity - worst case = n^2 best case n
"""

def insertion_sort(array):

    l = len(array)

    #we need a marker for last element in the sorted array
    s = 0

    #iterate through every element
    for i in range(1, l, 1):
        #while this element is less than it's previous element move it back
        k = s
        if array[i] < array[s]:
            array[i], array[s] = array[s], array[i]
        while array[k] < array[k-1] and k > 0:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1
        s += 1
input_array = [45, 66, 213, 9, 15, -8]
insertion_sort(input_array)
print_array(input_array, "Insertion Sort")


"""
Merge Sort

- We divide the array into it's individual elements
- As we build it back up - we compare and sort

Complexity - n log(n)
"""

#split the array into left and right array
#sort left array and sort right array

def merge_sort(array):
    if len(array) > 1:

        l = len(array)
        middle = int(l/2)
        l_array = array[:middle]
        r_array = array[middle:]

        #we split those arrays further into half
        merge_sort(l_array)
        merge_sort(r_array)

        #now we have our sorted arrays - we use them to put together our original array

        i = j = k = 0

        while i < len(l_array) and j < len(r_array):
            if l_array[i] < r_array[j]:
                array[k] = l_array[i]
                i += 1
                k += 1
            else:
                array[k] = r_array[j]
                k += 1
                j += 1

        #if we have any leftover elements
        while i < len(l_array):
            array[k] = l_array[i]
            k += 1
            i += 1

        while j < len(r_array):
            array[k] = r_array[j]
            k += 1
            j += 1

        return array

input_array = [45, 66, 213, 9, 15, -8]
sorted_array = merge_sort(input_array)
print_array(sorted_array, "Merge Sort")


"""
Selection Sort

 - We have our array split into sorted and unsorted array
 - We iterate over the array and for every index - we select the smallest value from the unsorted array and swap it with the 
   current element
"""


def selection_sort(array):

    l = len(array)

    #iterate over the entire array
    for i in range(0,l):
        smallest = i
        #iterate over the rest of the array and select smallest element
        for j in range(i+1,l):
            if array[j] < array[smallest]:
                smallest = j
        if smallest != i:
            #swap
            array[i], array[smallest] = array[smallest], array[i]

input_array = [45, 66, 213, 9, 15, -8]
selection_sort(input_array)
print_array(input_array, "Selection Sort")

"""
Counting Sort

 - we count the number of times an element occurs in the array
 - We store these counts in another array
 - For each element - we add the counts of the elements less than itself
 - This tells us that the element is the nth largest element
 - we need a range value for this sort
 
"""

def counting_sort(array, max_value):

    #we need a count array
    count_array = [0 for i in range(max_value)]

    #we need the final sorted array
    sorted_array = [0 for i in range(len(array))]

    #we count the occurrence of each element and store it
    for x in array:
        count_array[x] += 1

    #for each element we add the counts of all the elements less than itself, i.e that come before it in the given range
    for i in range(1, max_value):
        count_array[i] += count_array[i-1]

    #put the elements into the sorted array as per the new count value
    for x in array:
        sorted_array[count_array[x]-1] = x
        count_array[x] -= 1

    return sorted_array

input_array = [6,6, 6, 1, 9, 4, 7, 3, 3, 4]
output_array = counting_sort(input_array,10)
print_array(output_array, "Counting Sort")


"""
Bubble Sort

 - For decreasing lenght of the array - by 1 element for each iteration
 - for adjacent elements - if right is less than left - swap them
 
 Complexity - n^2
"""

def bubble_sort(array):

    l = len(array)

    #for each iteration we need to do the following
    while l > 1:
        for i in range(1,l):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
        l -= 1

input_array = [45, 66, 213, 9, 15, -8]
bubble_sort(input_array)
print_array(input_array, "Bubble Sort")

"""
Radix Sort
 - Sorts progressively by going through each decimal place of all the numbers
 - uses counting sort as a sub routine
"""

def counting_sort(array, max_value, exponent):

    #array to store the counts
    count_array = [0 for i in range(max_value)]

    #sorted array
    sorted_array = [0 for i in range(len(array))]

    #Count the no of occurrences of each element and store it in the count array
    for x in array:
        index = int(x/exponent)
        count_array[index%10] += 1
        print(count_array[index%10])

    #for each element we add the counts of all the elements that are less than itself
    for i in range(1,len(count_array)):
        count_array[i] += count_array[i-1]

    #now we put the elements into the sorted array in the right order
    i = len(array) - 1
    while i > -1:
        index = int(array[i]/exponent)
        sorted_array[count_array[index%10]-1] = array[i]
        count_array[index%10] -= 1
        i -= 1

    return sorted_array




def radix_sort(array):

    #maximum value from among all the elements of the array
    largest_value = max(array)

    exp = 1

    while int(largest_value/exp) > 0:
        array = counting_sort(array, 10, exp)
        exp *= 10

    return array

arr = [56, 51, 43, 58]
sorted_arr = radix_sort(arr)
print_array(sorted_arr, "Radix Sort")
