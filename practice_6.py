


"""
Sorting Algorithms

"""


#Print function to print arrays

def printArr(array, sort_name):
    print("")
    print("Sorted by ", sort_name)
    for x in array:
        print(x, end=", ")



"""
Heap Sort
    -Look at the array as a Heap
    -convert the Heap to a max heap
    -Repeatedly:
        - switch the first and last element
        - remove the last element
        - reduce length of array by one
        - convert to max heap
        
    Complexity: n log(n) : Converting into max heap takes log(n) time - and we do this 'n' times.
    In place sort
    Not a stable sort - duplicates order is not preserved
"""


def maxheapify(array, start_node, l):
    #max heapify procedure
    #parent node should be largest node
    largest = start_node

    #left_child
    l_c = 2*start_node + 1

    #right_child
    r_c = 2*start_node + 2

    #compare

    if l_c < l and array[largest] < array[l_c]:
        largest = l_c

    if r_c < l and array[largest] < array[r_c]:
        largest = r_c

    if largest != start_node:
        array[largest], array[start_node] = array[start_node], array[largest]
        maxheapify(array, largest, l)

def heap_sort(array):

    #length of the array
    l = len(array)

    #last non leaf node
    start_index = int(l/2) - 1

    #convert the array to a max heap
    #start from last non leaf node and go up to the root
    for i in range(start_index, -1, -1):
        #maxheapify
        maxheapify(array, i, l)

    #switch first and last
    #reduce length by one
    #max heapify starting from root
    #repeat from the switch
    for n in range(l-1, 0, -1):
        array[n], array[0] = array[0], array[n]
        #max heapify on root with length = n
        maxheapify(array, 0, n)

    return


input_array = [22, 66, 94, 71, 59, 17, 4, 103]
heap_sort(input_array)
printArr(input_array, "Heap Sort")

"""
Quicksort

    - We select a pivot
    - we move all elements less than the pivot to the left 
    - we keep all elements greater than the pivot to the right
    - then the repeat this process on the left and right arrays - excluding the pivot

    Complexity: n log n - best case - n^2 worst case (if we select the largest element as the pivot everytime)
    In place sort
    Stable sort - No
"""

def pivotFunction(array, start, end):

    pivot = end

    #last swapped element
    s = start - 1

    for i in range(start, pivot):
        if array[i] < array[pivot]:
            s += 1
            array[s], array[i] = array[i], array[s]


    #bring pivot to split point
    array[s+1], array[pivot] = array[pivot], array[s+1]

    return s+1

def quickSort(array, start, end):
    if start < end:

        #pivot function
        #give us the pivot index
        p = pivotFunction(array, start, end)

        #recursive call on the subarrays formed on either side of the pivot
        quickSort(array, start, p-1)
        quickSort(array, p+1, end)

    return

input_array = [22, 66, 94, 71, 59, 17, 4, 103]
length = len(input_array) - 1
quickSort(input_array, 0, length)
printArr(input_array, "Quick Sort")

"""

Insertion Sort

 - Split the given array into two arrays - sorted array and unsorted array
 - You iterate over each element
 - And find the right place to insert it in the sorted array
 
 Complexity - n^2 - best case is n
 In place sort
 Stable - yes
 
"""


def insertionSort(array):

    l = len(array)

    for i in range(1,l):
        if array[i] < array[i-1]:
            j = i
            while array[j] < array[j-1] and j > 0:
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1

    return


input_array = [22, 66, 94, 71, 59, 17, 4, 103]
insertionSort(input_array)
printArr(input_array, "Insertion Sort")

"""
Merge Sort

 - First divide the array into it's smallest elements
 - Sort the elements into place on the way up
 
 Complexity - nlog(n)
 In place sort - Nope
 Stable sort - yes
"""


def mergeSort(array):
    if len(array) > 1:

        l = len(array)
        #find midpoint
        m = int(l/2)

        #create the two subarrays
        l_array = array[0:m]
        r_array = array[m:]

        #recurse on the two subarrays
        mergeSort(l_array)
        mergeSort(r_array)

        i = j = k = 0
        #iterate over each of the two sub arrays

        while i < len(l_array) and j < len(r_array):
            if l_array[i] < r_array[j]:
                array[k] = l_array[i]
                i += 1
                k += 1
            else:
                array[k] = r_array[j]
                j += 1
                k += 1

        while i < len(l_array):
            array[k] = l_array[i]
            i += 1
            k += 1

        while j < len(r_array):
            array[k] = r_array[j]
            j += 1
            k += 1

        return array



input_array = [22, 66, 94, 71, 59, 17, 4, 103]
output_array = mergeSort(input_array)
printArr(output_array, "Merge Sort")


"""
Selection Sort
    - splits the array into two subarrays - sorted array and unsorted array
    - Iterate over each position
    - for each position - we select the smallest element in the unsorted array and swap it with the element in the current position
    
    Complexity - n^2
    Inplace sort - yes
    Stable Sort - yes
"""

def selectionSort(array):

    #length of the array
    l = len(array)

    for i in range(l):
        smallest = i
        for j in range(i+1,l):
            if array[j] < array[smallest]:
                array[j], array[smallest] = array[smallest], array[j]

    return

input_array = [22, 66, 94, 71, 59, 17, 4, 103]
selectionSort(input_array)
printArr(input_array, "Selection Sort")


"""

Counting Sort

   - we are dealing with values in a particular range
   - Count the number of occurances of each value in the array
   - Store those values in a count array
   - Use those values to put the elements in the sorted array
   
   - Complexity: linear - n - only works for values in a particular range
   - Not an in place sort
   - It is a stable sort
   
"""


def countingSort(array, key):


    l = len(array)

    #a count array
    count_array = [0 for _ in range(key)]

    #the sorted array
    sorted_array = [0 for _ in range(l)]


    #count the number of occurances of each elements in the array
    for x in array:
        count_array[x] += 1

    #we need to do the addition operation on the counts
    for i in range(1, key):
        count_array[i] = count_array[i] + count_array[i-1]

    #we need to place the elements into the sorted array based on their count value
    for x in array:
        sorted_array[count_array[x]-1] = x
        count_array[x] -= 1


    return sorted_array



input_array = [9, 6, 3, 3, 4, 9, 9, 7, 6, 4, 4]
output_array = countingSort(input_array, 10)
printArr(output_array, "Counting Sort")


"""
BubbleSort

 - We iterate through the array
 - we compare adjacent elements
 - if left element is less than right element - we swap them - end result is - largest element moves to last place
 - we repeat this for reducing lengths
 
 Complexity: n^2
 Stable - yes
 In place sort
"""


def bubbleSort(array):

    l = len(array)

    for n in range(l,0,-1):
        for i in range(1,n):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]

    return


input_array = [22, 66, 94, 71, 59, 17, 4, 103]
bubbleSort(input_array)
printArr(input_array, "Bubble Sort")



"""
Radix Sort

    - here we sort numbers based on their decimal places
    - start from units place and go on till the largest decimal place of the largest number in the array
    
    Complexity - linear
    Very slow - it is type of mechanical sort
    not an in place sort
    not a stable sort

"""

def countSort(array, exp):

    l = len(array)

    count_array = [0 for _ in range(10)]

    sorted_array = [0 for _ in range(l)]

    #count the elements
    for x in array:
        index = int(x/exp)
        count_array[index%10] += 1

    #increment count value
    for i in range(1, 10):
        count_array[i] = count_array[i] + count_array[i-1]

    #place the elements into the sorted array base on the count value:

    for x in reversed(array):
        index = int(x/exp)
        sorted_array[count_array[index%10]-1] = x
        count_array[index%10] -= 1

    return sorted_array


def radixSort(array):

    l = len(array)

    #largest value in the array
    largest = max(array) #thankyou python

    exp = 1

    while int(largest/exp) > 0:
        array = countSort(array, exp)
        exp *= 10

    return array


input_array = [22, 66, 94, 71, 59, 17, 4, 103]
sortedArr = radixSort(input_array)
printArr(sortedArr, "Radix Sort")


