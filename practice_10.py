



"""
Sorting algorithms
"""


def print_arr(arr, name):
    print("\nSorted by ", name)
    for x in arr:
        print(x, end=" ")


"""
Heap Sort
 - Heap sort is based on the concept of Heaps, specifically Max Heaps
 - We can consider the array to be a Heap
 - we convert it into a max Heap
 - switch the first and last element
 - remove the last element
 - convert the reduced array into a Max Heap
 - repeat the process
 
 Time Complexity: n log (n) : Each conversion to Max Heap takes log(n) time and we do this n times
 In place sort
 Not stable
"""

def maxheapify(array, start_index, length):

    #the parent has to be larger than both the children
    largest = start_index

    #left and right child
    left_child = 2*start_index + 1
    right_child = 2*start_index + 2

    if left_child < length and array[largest] < array[left_child]:
        largest = left_child

    if right_child < length and array[largest] < array[right_child]:
        largest = right_child

    if largest != start_index:
        array[largest], array[start_index] = array[start_index], array[largest]
        maxheapify(array, largest, length)

def heap_sort(array):

    #length of the array
    l = len(array)

    #convert the heap into a max heap
    #start with the last non leaf node

    start_index = int(l/2) - 1

    for i in range(start_index, -1, -1):
        #max heapify
        maxheapify(array, i, l)


    #swap
    #reduce
    #repeat

    for j in range(l-1, 0, -1):
        array[j], array[0] = array[0], array[j]
        #max heapify on reduced length
        maxheapify(array, 0, j)


input_array = [45, 64, 83, 21, 97, 33, 25, 17, 15, 6]
heap_sort(input_array)
print_arr(input_array, "Heap Sort")


"""
Quicksort

 - Basic principle involves the use of a pivot
 - you move the elements that are less than the pivot to the left
 - you move the elements that are greater than the pivot to the right
 - then you repeat the same on the two arrays on either side of the pivot
 
 Time complexity - n log (n)
 In place
 
"""

def sort_and_pivot(array, start, end):

    #we need the pivot
    pivot = array[end] #last element

    s = start - 1

    for i in range(start, end):
        if array[i] < pivot:
            s += 1
            array[s], array[i] = array[i], array[s]

    #bring pivot to middle
    array[s+1], array[end] = array[end], array[s+1]

    return s+1



def quick_sort(array, start, end):
    if start < end:
        #find pivot
        #move elements as per greater or less than
        #sort and pivot
        p = sort_and_pivot(array, start, end)

        #repeat process on the left
        quick_sort(array, start, p-1)
        #repeat process on the right
        quick_sort(array, p+1, end)

    return

input_array = [45, 64, 83, 21, 97, 33, 25, 17, 15, 6]
quick_sort(input_array, 0, len(input_array) - 1)
print_arr(input_array, "Quick Sort")



"""
Insertion Sort

 - splits the array into two parts
 - sorted and unsorted
 - iterate through the array over each element
 - find the right place to insert the element in the sorted array
 
 Time Complexity: Worst/average case: n^2, Best case: n
 In place
 
"""


def insertion_sort(array):

    #length
    l = len(array)

    for i in range(1, l):
        if array[i] < array[i-1]:
            j = i
            while array[j] < array[j-1] and j > 0:
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1


input_array = [45, 64, 83, 21, 97, 33, 25, 17, 15, 6]
insertion_sort(input_array)
print_arr(input_array, "Insertion Sort")



"""
Merge Sort

 - We keep dividing the array into it's smallest elements
  - then we sort on the way up
  
  Time Complexity: n log (n)
  not in place
  
  
"""


def mergeSort(array):
    if len(array) > 1:
        #split into half recursively

        l = len(array)

        m = int(l/2)

        l_array = array[:m]
        r_array = array[m:]

        l_array = mergeSort(l_array)
        r_array = mergeSort(r_array)

        i = j = k = 0

        while i < len(l_array) and j < len(r_array):
            if l_array[i] < r_array[j]:
                array[k] = l_array[i]
                k += 1
                i += 1
            else:
                array[k] = r_array[j]
                k += 1
                j += 1

        while i < len(l_array):
            array[k] = l_array[i]
            i += 1
            k += 1

        while j < len(r_array):
            array[k] = r_array[j]
            j += 1
            k += 1

    return array

input_array = [45, 64, 83, 21, 97, 33, 25, 17, 15, 6]
sorted_array = mergeSort(input_array)
print_arr(sorted_array, "Merge Sort")



"""

Selection Sort

 - divides array into two arrays
 - select next smallest element from unsorted arrays and add it to sorted array
 
 Time Complexity: n^2
 
"""




def selection_sort(array):

    #length
    l = len(array)

    for i in range(0, l):
        smallest = i
        for j in range(i+1, l):
            if array[j] < array[smallest]:
                smallest = j
            if smallest != i:
                array[i], array[smallest] = array[smallest], array[i]


input_array = [45, 64, 83, 21, 97, 33, 25, 17, 15, 6]
selection_sort(input_array)
print_arr(input_array, "Selection Sort")




"""


Counting Sort

 - operates within a given range
 - count the number of occurances of each element in the array from a given range
 - modify the count array so that each count now represents the position of the index in the sorted array
 - add the elements in the sorted array
"""


def counting_sort(array, max_range):

    l = len(array)

    #count array
    count_array = [0 for i in range(max_range)]

    #sorted array
    sorted_array = [0 for i in range(l)]

    #count the number of occurances of each element in the given array
    for x in array:
        count_array[x] += 1


    #modify the counts
    for i in range(1, max_range):
        count_array[i] = count_array[i] + count_array[i-1]


    #fill the sorted array
    for x in array:
        sorted_array[count_array[x] - 1] = x
        count_array[x] -= 1

    return sorted_array


input_array = [3, 3, 4, 5 , 5, 7, 7, 8, 6, 6, 1, 3]
sorted_array = counting_sort(input_array, 10)
print_arr(sorted_array, "Counting Sort")



"""

Bubble Sort

 - for reducing lengths
 - compare adjacent elements - if left is larger than right - swap
 - this moves largest element to the right every time
 
"""


def bubbleSort(array):

    #length
    l = len(array)

    for n in range(l, 1, -1):
        for i in range(1,n):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]

input_array = [45, 64, 83, 21, 97, 33, 25, 17, 15, 6]
bubbleSort(input_array)
print_arr(input_array, "Bubble Sort")



"""
Radix Sort

 - Sorting is done on the basis of decimal places
 - Counting sort is used as a sub routine
 
"""


def counting_subroutine(array, exp):

    l = len(array)

    #count array
    count_array = [0 for i in range(10)]

    #sorted array
    sorted_array = [0 for i in range(l)]

    #count the number of times a particular decimal place occurs in the array
    for x in array:
        index = int(x/exp) % 10
        count_array[index] += 1

    #modify count array
    for i in range(1,10):
        count_array[i] = count_array[i] + count_array[i-1]

    #fill up sorted array
    for x in reversed(array):
        index = int(x/exp) % 10
        sorted_array[count_array[index] - 1] = x
        count_array[index] -= 1


    return sorted_array


def radix_sort(array):

    largest = max(array)

    exp = 1

    while int(largest/exp) > 0:
        #counting sort
        array = counting_subroutine(array, exp)
        exp *= 10

    return array



input_array = [45, 64, 83, 21, 97, 33, 25, 17, 15, 6]
sorted_array = radix_sort(input_array)
print_arr(sorted_array, "Radix Sort")
