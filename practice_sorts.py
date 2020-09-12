


arr = [6, 102, 19, 43, -24, 0, 12]

def print_arr(array, sort_type):
    print("\nSorted by ", sort_type)
    for x in array:
        print(x, end=" ")
    print("\n")



"""
Heap Sort
1.You represent the array as a heap.
2.You convert the heap into a max heap.
3.You then swap the first and the last nodes.
4.You then remove the last node and maxheapify the reduced array.
5.Repeat from step 3 - till you reduce the array to it's last element.
6.You get a sorted array

Maxheap basic principle - parent node has to be larger than child nodes


"""


def max_heapify(array, start_node, l):

    largest = start_node

    #left child index
    left_node = 2*start_node + 1
    #right child index
    right_node = 2*start_node + 2


    #check if left child exists and if it is larger than parent
    if left_node < l and array[left_node] > array[largest]:
        largest = left_node
    #check if right child exists and if it larger than parent
    if right_node < l and array[right_node] > array[largest]:
        largest = right_node

    #if swap is required
    # swap and recurse down the swapped child
    if largest != start_node:
        swap = array[start_node]
        array[start_node] = array[largest]
        array[largest] = swap
        max_heapify(array, largest, l)


def heapSort(array):

    n = len(array)
    #have to start from last leaf less node
    start_index = int((n/2) - 1)

    #Convert this into a max heap
    for i in range(start_index, -1, -1):
        max_heapify(array, i, n)

    # Swap
    # reduce
    # maxheapify
    # repeat

    for j in range(n-1, 0, -1):
        swap = array[j]
        array[j] = array[0]
        array[0] = swap
        #maxheapify function - with reduced array
        max_heapify(array, 0, j)


    #return sorted array
    return array

sorted_arr = heapSort(arr)
print_arr(sorted_arr, "Heap Sort")


"""
Quick Sort

- divide and conquer method

1.We have a pivot
2.Move all things smaller than the pivot to the left
3.Move all things larger than the pivot to the right
4.Repeat process on left and right sub arrays.

"""



def quick_sort_partition(array, start, end):

    #pivot
    pivot = array[end]

    #two iterators - one to keep track of each element as we pass through the array and the other to keep trakc of the last swapped index
    k = start - 1

    #iterate and compare
    for i in range(start, end):
        if array[i] < pivot:
            k = k + 1
            swap = array[i]
            array[i] = array[k]
            array[k] = swap

    #bring pivot to partition point
    swap = pivot
    array[end] = array[k + 1]
    array[k + 1] = swap


    #return position of pivot
    return k + 1

def quick_sort(array, start, end):
    #partition given array and run quick sort on each partition

    #check if array can be partitioned
    if start < end:


        pivot = quick_sort_partition(array, start, end)


        quick_sort(array, start, pivot - 1)
        quick_sort(array, pivot + 1, end)


        return array


length = len(arr)
sorted_arr = quick_sort(arr, 0, length-1)

print_arr(sorted_arr, "Quick Sort")



'''
Insertion Sort


1. Treat the single array as two sub arrays - sorted on the left and unsorted on the right
2. Iterate through the unsorted array - if an element is smaller than the element on the left - insert it in the right position
   in the sorted array.
'''

def insertion_sort(array):

    #we need the length
    n = len(array)

    #we need the following markers for the iterate and compare operation
    #One marker for the current element
    #One marker for the last element of the sorted array
    #One marker to iterate backwards to insert at the right position

    s = 0

    for i in range(1, n):
        if array[i] < array[s]:
            s = s + 1
            #swap s and i
            swap = array[s]
            array[s] = array[i]
            array[i]  = swap
            for j in range(s, 0, -1):
                if array[j] < array[j-1]:
                    swap = array[j]
                    array[j] = array[j-1]
                    array[j-1] = swap

    return array


sorted_arr = insertion_sort(arr)
print_arr(sorted_arr, "Insertion Sort")

'''
Merge Sort

1. We divide the entire array into it's individual elements 
2. Sort the array back together


'''

def mergesort(array):
    if len(array) > 1:

        #find the middle of the array
        m = int(len(array) / 2)

        left_array = array[:m]
        right_array = array[m:]

        #split each sub array
        mergesort(left_array)
        mergesort(right_array)

        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i = i+1
                k = k+1
            else:
                array[k] = right_array[j]
                j = j+1
                k = k+1


        while i < len(left_array):
            array[k] = left_array[i]
            i = i + 1
            k = k + 1

        while j < len(right_array):
            array[k] = right_array[j]
            j = j + 1
            k = k + 1

    return array

arr = [6, 102, 19, 43, -24, 0, 12]
sorted_arr = mergesort(arr)
print_arr(sorted_arr, "Merge Sort")

'''
Selection Sort

1. You split the array in two sub arrays = sorted array and unsorted array
2. You iterate over the array and find the smallest value
3. You then place the element in the last positon of the sorted array
4. Repeat till you reach the end of the array

'''

def selection_sort(array):

    #length
    n = len(array)

    #smallest
    s = 0

    #iterate over every element
    for i in range(0, n):
        #current position of last element of sorted array
        s = i
        #iterate over remaining elements and find smallest element
        for j in range(i+1, n):
            if array[j] < array[s]:
                s = j
        #if we have found a smaller element - swap
        if s != i:
            swap = array[i]
            array[i] = array[s]
            array[s] = swap

    return array

arr = [6, 102, 19, 43, -24, 0, 12]
selection_sorted_arr = selection_sort(arr)
print_arr(selection_sorted_arr, "Selection Sort")

'''
Counting Sort

1. We have an array and we have a range for the values
2. We count the occurence of each individual value in the array and store it in a count array
3. Then we modify the count array such that every count is a sum of itself and the previous number's count
4. Then we add the values into a new sorted array as they appear in the given array and place them based on the count value, every time 
   we place a value, we decrease it's count.
'''



def count_sort(array, max_range):

    #we need two new arrays

    #count array
    count_array = [0 for i in range(max_range)]

    #sorted_array
    sorted_array = [0 for i in range(len(array))]


    #count the occurance of each individual value in the given array
    for x in array:
        count_array[x] += 1

    #modify the count_array
    for i in range(1, max_range):
        count_array[i] = count_array[i] + count_array[i-1]

    #place the values into the sorted array
    for x in array:
        sorted_array[count_array[x] - 1] = x
        count_array[x] -= 1

    return sorted_array

arr = [5, 7, 3, 8, 5, 7, 2, 7, 1, 5, 8]
sorted_arr = count_sort(arr, 10)
print_arr(sorted_arr, "Counting Sort")


'''

Bubble Sort

1. We iterate over the entire array comparing adjacent elements. If the element on the right is less than the element
  on the left - we swap them.
2. Once we reach the end of the array, we then repeat the same on a sub array formed by eliminating the right most element.
3. We repeat till we reach the first element - subarray of 1.


'''

def bubble_sort(array):

    #length
    n = len(array)

    #keep reducing size of sub array by eliminating last element
    while n > 0:
        #iterate over entire sub array - compare adjacent elements and swap if right is less than left
        for i in range(0, n-1):
            if array[i + 1] < array[i]:
                swap = array[i + 1]
                array[i+1] = array[i]
                array[i] = swap
        n -= 1

    return array

arr = [6, 102, 19, 43, -24, 0, 12]
sorted_arr = bubble_sort(arr)
print_arr(sorted_arr, "Bubble Sort")



'''
Radix Sort

1. We go from the smallest decimal place to the largest decimal place and for every decimal place we implement counting sort


'''


def radix_counting_sort(c_arr, exp):

    #max range value is 10 (range is 0-9)

    #length
    n = len(c_arr)

    #count_array
    count_array = [0 for i in range(10)]

    #sorted_array
    c_sorted_array = [0 for i in range(n)]

    #count the number of occurences of each individual element
    for x in arr:
        index = x/exp
        count_array[int(abs(index)%10)] += 1

    for i in range(len(count_array)):
        print("count array value at ", i, "is", count_array[i])

    print("")
    #modify the count array so each index contains the place where the value should go
    for i in range(1,10):
        count_array[i] = count_array[i] + count_array[i-1]

    for i in range(len(count_array)):
        print("count array value at ", i,"is", count_array[i])

    #place the values into the sorted array
    i = n - 1
    while i >= 0:
         index = c_arr[i]/exp
         print("for x in arr printing count array value",count_array[int(abs(index)%10)]," at",int(abs(index)%10))
         c_sorted_array[count_array[int(abs(index)%10)] - 1] = c_arr[i]
         count_array[int(abs(index)%10)] -= 1
         i -= 1

    print("")

    for x in c_sorted_array:
        print(x)

    return c_sorted_array


def radix_sort(c_array):

    #find the maximum value
    maximum_value = max(c_array)
    print("max value is",maximum_value)
    exp = 1

    while int(maximum_value/exp) > 0:
        print("maximum_value/exp = ", maximum_value/exp)
        print("Run for exp", exp)
        c_array = radix_counting_sort(c_array, exp)
        exp *= 10

    return c_array

arr = [56, 51, 43, 58]
sorted_arr = radix_sort(arr)
print_arr(sorted_arr, "Radix Sort")


"""

n = 7

Round 1
count array:
0 1 1 3 4 5 5 6 6 6
0 1 2 3 4 5 6 7 8 9

sorted array
0 12 102   43  24   6 19
0  1   2    3   4   5  6

Round 2
0 12 102   43  24   6 19
div by 10
0 1  10    4   2    0 1
count array:
0 4 5 6 6 7 7 7 7 7
0 1 2 3 4 5 6 7 8 9

sorted array
6  102  0  19 12 24 43
0  1    2  3  4  5  6

Round 3
6  102  0  19 12 24 43
div by 100

0  1    0  0  0  0  0
mod by 10
count array
3 6 7 7 7 7 7 7 7 7
0 1 2 3 4 5 6 7 8 9

sorted array
43 24 12 19 0 6 102 
0 1 2 3 4 5 6

"""


