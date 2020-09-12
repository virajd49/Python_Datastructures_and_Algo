



"""
Sorts
"""

def printArr(array, sort_name):
    print("")
    print("Array sorted by ", sort_name)
    for x in array:
        print(x, end=" ")
    print("")


"""
Heap Sort

 - We look at the array as a Heap structure
 - We convert the Heap to a max heap
 - We swap the first the last - then remove the last
 - Now we convert remaining array in to a Max heap and repeat the process till we reach one element
"""

def maxHeapify(array, index, length):
    #the parent must be greater than both children

    largest = index
    l_child = 2*index + 1
    r_child = 2*index + 2

    if l_child < length and array[largest] < array[l_child]:
        largest = l_child

    if r_child < length and array[largest] < array[r_child]:
        largest = r_child

    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        maxHeapify(array, largest, length)

def heapSort(array):

    l = len(array)
    start_index = int(l/2) - 1
    #convert heap into Max Heap
    #start with the last non-leaf node
    for i in range(start_index, -1, -1):
        maxHeapify(array, i, l)

    for j in range(l-1, 0, -1):
        #swap
        array[j], array[0] = array[0], array[j]
        maxHeapify(array, 0, j)

    return


input_array = [90, 75, 64, 33, 27, 84, 109, 22, 55]
heapSort(input_array)
printArr(input_array, "Heap Sort")


"""
QuickSort

 - We select a pivot
 - we put all values less than the pivot to the left
 - we put all values greater than the pivot to the right
 - then we repeat this process on the left and right arrays
 
"""
def sort_and_part(array, start, end):

    #pivot
    pivot = end

    #iterator to keep track of the last swapped element
    s = start - 1
    #iterate from first to pivot-1 and compare
    for i in range(start, pivot):
    #if less than pivot push to left
        if array[i] < array[pivot]:
            s += 1
            array[i], array[s] = array[s], array[i]

    #bring the pivot to the middle
    array[s+1], array[pivot] = array[pivot], array[s+1]

    return s+1

def quickSort(array, start, end):
    if start < end:
        l = len(array)
        #sort around pivot and partition the array
        m = sort_and_part(array, start, end)

        #do the same on left array
        quickSort(array, start, m-1)
        #do the same on right array
        quickSort(array, m+1, end)

input_array = [45, 62, 78, 99, 102, 25, 17, 47]
quickSort(input_array, 0, len(input_array)-1)
printArr(input_array, "Quick Sort")


"""
Insertion Sort
- splits the array into two arrays - sorted array and unsorted array
- iterate over all the elements
- at each element you find the right place in the sorted array and insert it there.
"""

def insertion_sort(array):
    #iterate over every element
    #build the sorted array from the left
    #initially sorted array ends at position 0
    #sorted array position moves by 1 every time

    l = len(array)

    #sorted array position
    s = 0

    for i in range(1,l):
        if array[i] < array[s]:
            n = i
            while n > 0 and array[n] < array[n-1]:
                array[n], array[n-1] = array[n-1], array[n]
                n -= 1
        s += 1

    return



input_array = [45, 67, 83, 12, 56, 72, 33, 111, 29]
insertion_sort(input_array)
printArr(input_array, "Insertion Sort")

"""
Merge Sort

-Divide the array into it's smallest elements
-then we sort them on the way back up.

"""


def mergeSort(array):
    if len(array) > 1:
        l = len(array)
        m = int(l/2)

        l_array = array[:m]
        r_array = array[m:]

        mergeSort(l_array)
        mergeSort(r_array)

        i = j = k = 0

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

input_array = [22, 36, 75, 81, 76, 99, 37, 28]
mergeSort(input_array)
printArr(input_array, "Merge Sort")

"""
Selection Sort
- Iterate over each position
- At every position find the smallest element from the remaining array and swap it with the element in the current position.
"""

def selectionSort(array):

    l = len(array)


    for i in range(l):
        smallest = i
        for j in range(i+1, l):
            if array[j] < array[smallest]:
                smallest = j
        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]

    return


input_array = [78, 34, 56, 79, 82, 32, 21, 19, 17, 43]
selectionSort(input_array)
printArr(input_array, "Selection Sort")


"""

Counting Sort

- You count the occurrance of every element in the given array and store the count in a count array
- You modify the count so that every value is a sum of itself and the value before it
- You add the elements into a new array - value in the count array indicates position
"""


def counting_sort(array, key):

    l = len(array)

    #count array
    count_array = [0 for i in range(key)]

    #sorted array
    sorted_array = [0 for j in range(l)]

    for x in array:
        count_array[x] += 1

    for i in range(1,key):
        count_array[i] = count_array[i] + count_array[i-1]

    for x in array:
        sorted_array[count_array[x]-1] = x
        count_array[x] -= 1

    return sorted_array


input_array = [9, 5, 6, 3, 6, 2, 9, 6, 3, 3, 9, 7]
output_array = counting_sort(input_array, 10)
printArr(output_array, "Counting Sort")

"""
Bubble Sort
-For reducing length of the array
-compare adjacent elements and if right element is smaller than left element - swap the two elements

"""

def bubbleSort(array):

    l = len(array)


    for n in range(l, 1, -1):
        for i in range(1,n):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]

    return


input_array = [47, 84, 65, 99, 32, 44, 13, 78]
bubbleSort(input_array)
printArr(input_array, "Bubble Sort")




"""
Radix Sort

- We sort numbers in individual steps
- In each step we sort them in the basis of one decimal place
- we using counting sort as a subroutine with the range being 0-9
 
"""
def countSortRoutine(array, exp):

    l = len(array)

    #count_array
    count_array = [0 for i in range(10)]

    #sorted_array
    sorted_array = [0 for j in range(l)]

    for x in array:
        index = int(x/exp)
        count_array[index%10] += 1

    for i in range(1, 10):
        count_array[i] = count_array[i] + count_array[i-1]

    for x in reversed(array):
        index = int(x/exp)
        sorted_array[count_array[index%10] - 1] = x
        count_array[index%10] -= 1

    return sorted_array


def radixSort(array):

    l = len(array)
    exp = 1

    largest_value = max(array)

    while int(largest_value/exp) > 0:
        #counting sort
        array = countSortRoutine(array, exp)
        exp = exp*10

    return array

input_array = [111, 25, 213, 450, 98, 320, 120, 154]
sorted_array = radixSort(input_array)
printArr(sorted_array, "Radix sort Array")





