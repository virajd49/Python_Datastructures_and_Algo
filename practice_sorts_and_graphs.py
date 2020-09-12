

"""

Practice Sorts
Recollect linked list complexity theory
Recollect Graph + graph exploration + SSSP theory
Implement BST


"""


"""
Sorts
"""


def print_a(array, name):
    print("\nSorted by", name)
    for x in array:
        print(x, end=" ")

"""
Heap Sort 

 - we treat the given array as a Hesp
 - we convert the heap into a max heap
 - we remove the largest element
 - we repeat the process on the reduced array till we can't do it anymore
 - we will have a sorted array by the end
 
 - Complexity : O(n log n) - the maxheapify operation has a complexity of log n and we do that n times
 - In place sort
 - Not a stable sort
"""

def max_heapify(array, length, start_index):

    #implement the max heap principle for every subtree starting from start_index
    #parent has to be largest node in subtree - larger than both children

    largest = start_index

    l_child = 2*start_index + 1
    r_child = 2*start_index + 2

    if l_child < length and array[largest] < array[l_child]:
        largest = l_child

    if r_child < length and array[largest] < array[r_child]:
        largest = r_child

    if largest != start_index:
        #swap
        array[largest], array[start_index] = array[start_index], array[largest]
        max_heapify(array, length, largest)

    return

def heap_sort(array):

    l = len(array)

    start_node = int(l/2) - 1

    #we want to convert given array into a max heap
    for i in range(start_node, -1, -1):
        #run the max heap principle on every subtree
        #we need to start with the last non leaf node and go to the root
        #call maxheapify
        max_heapify(array, l, i)

    #we want to remove largest element
    #we want to repeat the above process on the reduced array
    for j in range(l-1, 0, -1):
        array[0], array[j] = array[j], array[0]
        #call maxheapify ON REDUCED ARRAY
        max_heapify(array, j, 0)

    return


input_array = [67, 13, 25, 0, 93, 46, 10, 3, 58]
heap_sort(input_array)
print_a(input_array, "Heap Sort")


"""
QuickSort

 - we divide the given array into two parts on the basis of a pivot
 - we select the last element as the pivot
 - we move all elements smaller than the pivot to the left
 - we move all elements greater than the pivot to the right
 - then we repeat the above process on the left and right arrays
 
 Complexity - O(n log n)
 In place sort
 Not a stable sort
"""

def partition(array, start, end):

    pivot = array[end]

    #we need something to keep track of the last swapped element in the array
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

        #bring pivot to middle
        #get pivot
        p = partition(array, start, end)

        #repeat on either side of pivot
        #recursive call
        quick_sort(array, start, p-1)
        quick_sort(array, p+1, end)

    return

input_array = [67, 13, 25, 0, 93, 46, 10, 3, 58]
l = len(input_array)
quick_sort(input_array, 0, l-1)
print_a(input_array, "Quick Sort")


"""
Insertion Sort

 - we split the array into two sections: sorted and unsorted
 - as we iterate through the array - for every element, we find the right place for it in the sorted array and insert it there
 
 Complexity: O(n^2) worst case and average case O(n) in best case  - which is already sorted array
 In place sort
 Stable sort
 
"""


def insertion_sort(array):

    l = len(array)

    for i in range(1,l):
        if array[i] < array[i-1]:
            j = i
            while j > 0 and array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1

    return

input_array = [67, 13, 25, 0, 93, 46, 10, 3, 58]
insertion_sort(input_array)
print_a(input_array, "Insertion Sort")


"""

Merge Sort

 - we split the array into half till we reach it's individual elements
 - we build the array up by joining all the half's into 1's
 - when we build we sort
 
 Complexity: O(n log n)
 Not in place sort
 Not stable
"""


def merge_sort(array):
    #we need to find the middle of the array
    # check if array can be split into two
    l = len(array)

    if l > 1:


        #split into 2

        m = int(l/2)

        l_array = merge_sort(array[:m])
        r_array = merge_sort(array[m:])

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

        #if we still have any remaining elements
        while i < len(l_array):
            array[k] = l_array[i]
            k += 1
            i += 1

        while j < len(r_array):
            array[k] = r_array[j]
            k += 1
            j += 1

    return array


input_array = [67, 13, 25, 0, 93, 46, 10, 3, 58]
sorted_array = merge_sort(input_array)
print_a(sorted_array, "Merge Sort")

"""
Selection Sort

 - the array is split into two sections - sorted and unsorted
 - for every element - we scan through the rest of the array and pick the smallest element - and replace it with the current element
 
 Complexity: O (n^2)
 In place sort
 Not a stable sort
 
"""


def selection_sort(array):

    l = len(array)

    for i in range(l):
        smallest = i
        for j in range(i+1, l):
            #get the smallest element
            if array[j] < array[smallest]:
                smallest = j
        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]

    return


input_array = [67, 13, 25, 0, 93, 46, 10, 3, 58]
selection_sort(input_array)
print_a(input_array, "Selection Sort")

"""
Counting Sort

 - we operate within a given range of numbers
 - we count the occurance of every number in the array
 - and we sort the numbers on the basis of that count
 
 Complexity: O(n + range) - linear but it depends on the range of the numbers
 Not an in place sort
 Not a stable sort
 
"""


def counting_sort(array, key):

    l = len(array)

    #we need an array to store the counts of each number in the given range
    count_array = [0 for i in range(key)]

    #we need an array to store the sorted order
    sorted_array = [0 for j in range(l)]

    #count the number of occurances
    for x in array:
        count_array[x] += 1

    #modify the count such that it gives us the place of the number in the sorted array
    for i in range(1, key):
        count_array[i] = count_array[i] + count_array[i-1]

    #place them in sorted order
    for x in array:
        sorted_array[count_array[x] -1] = x
        count_array[x] -= 1

    return sorted_array

input_array = [67, 13, 25, 0, 93, 46, 10, 3, 58]
sorted_array = counting_sort(input_array, 100)
print_a(sorted_array, "Counting Sort")

"""
Bubble Sort

 - for every element - if it is greater than the element that comes after it - swap them 
 - this basically moves large elements to the right - and small elements to the left
 - we do this for reducing lenghts !!!!!!!!!!!
 
 Complexity: O(n^2)
 In place sort
 Stable sort
 
"""

def bubble_sort(array):

    l = len(array)

    for n in range(l, 0, -1):
        for i in range(n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

    return


input_array = [67, 13, 25, 0, 93, 46, 10, 3, 58]
bubble_sort(input_array)
print_a(input_array, "Bubble Sort")


"""

Radix sort

 - we sort on the basis of the different decimal place values
 - we use counting sort as a subroutine with range of 0-9
 
 Complexity: O(n * size of largest number in the array)
 Not in place
 Not stable
 
"""

def counting_subroutine(array, exp):

    l = len(array)

    count_array = [0 for i in range(10)]

    sorted_array = [0 for i in range(l)]

    #count the occurances
    for x in array:
        index = int(x/exp) % 10
        count_array[index] += 1

    #modify the counts
    for i in range(1, 10):
        count_array[i] = count_array[i] + count_array[i-1]

    #place into sorted array
    for x in reversed(array):
        index = int(x/exp) % 10
        sorted_array[count_array[index] - 1] = x
        count_array[index] -= 1

    return sorted_array


def radix_sort(array):

    largest_value = max(array)

    exp = 1

    while int(largest_value/exp) > 0:
        #call counting subroutine
        array = counting_subroutine(array, exp)
        exp *= 10

    return array

input_array = [67, 13, 25, 0, 93, 46, 10, 3, 58]
sorted_array = radix_sort(input_array)
print_a(sorted_array, "Radix Sort")



"""

Graph Theory

 - Graph Exploration
  -BFS and DFS
   - when we want to traverse a graph, when we want to explore the entire graph, detect cycles, shortest paths, etc
   
   - BFS
    - breadth first search
    - gives us shortest paths from 1 to any node/ find if a path exists between two nodes
    - can be coded using a queue or frontier array method
    - for shortest paths, when we visit a node - we have to set it's parent
    - Complexity: O(V + E)
 
   - DFS
    - depth first search
    - allows us to detect cycles and do topological sort(scheduling of interdependent things)
    - implemented using recursion
    - at every node set it's parent
    - Complexity: O(V + E)
 
 - Single Source Shortest Paths with weighted graphs
  - Djikstra's, Bellman Ford and DAG with topological sort
    - general principle is 'relaxing vertices', so select the vertices in certain order and relax them
    - the different algorihtms basically give us different orders to relax the vertices
    - Djikstra's - only works with positive weights, can handle cycles
                 - Complexity is O(V lg V + E) - using a fibonacci heap for the min queue
                 - Order of selection: start with starting node having distance 0, add all nodes to min queue, 
                                       extract min distance node,
                                       relax all adjacent nodes, 
                                       repeat.
                 - when we visit a node, relax it and set it's predecessor at the same time.
                 
    - Bellman Ford - works with negative weights, can detect negative weight cycle, can't give you an answer if negative weight cycle exists.
                  - Complexity is O(VE)
                  - Order of selection method: no actual order, 
                                               - set distance of starting node to 0
                                               - then just go over all edges (u,v) V-1 times  
                                                    - this will take AT MOST |V| - 1 times - we can make it more efficient
                                                      by checking if any of the distances have changed between iterations.
                                                    - by going through all vertices and using their adj edges.
                                               - and relax v  - this should give you shortest path from starting node.
    
    - topological sort for DAG - negative and positive weights
     - If we have a DAG 
         - run topological sort (basically DFS)
         - relax edges in topological sort order.
         
     
"""


adj_list_num = { 1: [2, 4], 2: [5], 3: [5, 6], 4:[2], 5: [4], 6:[6]}

adj_list_dag = {1 : [5], 2 : [1, 5], 3 : [1], 4 : [7], 6 : [1, 2, 3] }

print("\nBFS")
class bfs:
    def __init__(self):
        self.parent = {}

    def bfs_visit(self, adj, s):

        frontier = [s]
        self.parent[s] = None

        while frontier:
            new = []
            for u in frontier:
                if u in adj.keys():
                    for v in adj[u]:
                        if v not in self.parent:
                            self.parent[v] = u
                            new.append(v)
            frontier = new

    def bfs_explore(self, adj):

        for x in adj:
            if x not in self.parent:
                self.parent[x] = None
                self.bfs_visit(adj, x)

    def parent_of(self, node):
        if node in self.parent and self.parent[node] != None:
            print("\nParent of", node, "is", self.parent[node])
        else:
            print(node,"has no parent")

    def does_path_exist(self, node1, node2):

        #path to node1 by following parent
            #see if path contains node2
        path_exists = False
        node = node1
        while node in self.parent.keys() and self.parent[node] != None:
            if self.parent[node] == node2:
                path_exists = True
                print("\nPath exists !!")
                return
            else:
                node = self.parent[node]

        path_exists = False
        node = node2
        while node in self.parent.keys() and self.parent[node] != None:
            if self.parent[node] == node1:
                path_exists = True
                print("\nPath exists !!")
                return
            else:
                node = self.parent[node]

        print("\nPath does not exist !!")
        return

    def bfs_visit_find_path(self, adj, start, end):
        if start == end:
            print("\n Path exists !!!")
            return

        frontier = [start]
        self.parent = {}
        self.parent[start] = None

        while frontier:
            new = []
            for u in frontier:
                if u in adj.keys():
                    for v in adj[u]:
                        if v == end:
                            print("\nPath exists !!!")
                            return

                        if v not in self.parent:
                            self.parent[v] = u
                            new.append(v)
            frontier = new

        print("Path does not exist!!")
        return




        #path to node2 by following parent
            #see if path contains node1

bfs_obj = bfs()
bfs_obj.bfs_explore(adj_list_dag)
bfs_obj.parent_of(6)
bfs_obj.parent_of(3)
bfs_obj.bfs_visit_find_path(adj_list_dag, 5, 6)


print("\nDFS")
class dfs:
    def __init__(self):
        self.parent = {}
        self.topo_sort = []
        self.topo = False


    def dfs_visit(self, adj, s):
        for v in adj[s]:
            if v not in self.parent:
                self.parent[v] = s
                self.dfs_visit(adj, v)
        if self.topo == True:
            self.topo_sort.append(s)

    def dfs_explore(self, adj):
        for x in adj:
            if x not in self.parent:
                self.parent[x] = None
                self.dfs_visit(adj, x)

    def parent_of(self, node):
        if self.parent[node] != None :
            print("Parent of ", node, "is", self.parent[node])
        else:
            print(node,"has no parent")


    def topological_sort(self, adj):

        self.topo = True
        print("\n Topologically sorted order is")

        self.dfs_explore(adj)
        for x in reversed(self.topo_sort):
            print(x, end=" ")

        self.topo = False

        return

dfs_obj = dfs()
#dfs_obj.dfs_explore(adj_list_num)
#dfs_obj.parent_of(3)
#dfs_obj.parent_of(6)
dfs_obj.topological_sort(adj_list_num)

print("\nDjikstra's")

positive_weighted_graph = {1:[3], 2:[1,3,6], 3:[4,6], 4:[6], 5:[6,7], 6:[8,9], 7:[8], 8:[9], 9:[]}
weights = {(1,3):7, (2,1): 5, (2,3):1, (2,4):6, (3,4): 3, (3,6):4, (4,6):3, (5,6): 9, (5,7): 10, (6,8): 8, (6,9): 2, (7,8): 1, (8,9): 2}

class djikstra_shortest_path:
    def __init__(self):
        self.distance = {int: int}
        self.weight = {(int,int):int}
        self.parent = {int:int}
        self.shortest_path_set = [int]

    def findmin(self, adj: {int: [int]}, dist: {int: int}):

        minimum = 100
        #print("max weight + 1 is ", minimum)
        closest_node = None

        for x in dist.keys(): #O(number of keys)
            print(x)
            if x not in self.shortest_path_set: #O(n) - complexity - BAD
                #print(x, "not in shortest path")
                #print("dist of ", x, "is", dist[x])
                if dist[x] < minimum:
                    #print("dist of ", x, "is", dist[x])
                    minimum = dist[x]
                    closest_node = x

        return closest_node


    def relax(self,u,v):
        #print("u is",u, " v is",v)

        if v not in self.distance.keys(): # this means distance is infinity
            self.distance[v] = self.distance[u] + self.weight[(u, v)]
            self.parent[v] = u
        else:
            if self.distance[v] > self.distance[u] + self.weight[(u,v)]:
                self.distance[v] = self.distance[u] + self.weight[(u,v)]
                self.parent[v] = u

        return


    def djisktras(self, adj, edge_weights, start_node):
        self.weight = edge_weights
        self.distance[start_node] = 0
        parent = {start_node: None}

        #termination condition is what
            #while we can extract min?
            #while we can relax
        while 1:
            #get the vertice with the minimum distance at this iteration
            min = self.findmin(adj, self.distance)
            print("\n min is", min)
            #
            if min != None:
                self.shortest_path_set.append(min)
            if min != None and adj[min] != None:
                for v in adj[min]:
                    self.relax(min, v)
            else:
                break

    def shortest_path_to(self, node):
        print(self.parent)
        path = [node]

        while node in self.parent.keys() and self.parent[node] != None:
            path.append(self.parent[node])
            node = self.parent[node]

        for x in reversed(path):
            print(x, end=" ")


dk = djikstra_shortest_path()
dk.djisktras(positive_weighted_graph,weights,1)
dk.shortest_path_to(8)
dk.shortest_path_to(9)

print("\n Bellman Ford ")

class bellman_ford_SP:
    def __init__(self):
        self.parent = {}
        self.distance = {}

    def bellman_ford(self, adj, num_v, start_node, weights):

        self.distance[start_node] = 0
        self.parent[start_node] = None
        #for V-1 iterations relax all edges
        for i in range(1, num_v - 1):

        #how to access all edges?
            #access all vertices from the adj list and then access the edges from there
            for u in adj.keys():
                #if u is reachable
                if u in self.distance.keys():
                    for v in adj[u]:
                        #if v is at infinity - set it's value
                        #also set predecessor
                        if v not in self.distance.keys():
                            self.distance[v] = self.distance[u] + weights[(u,v)]
                            self.parent[v] = u
                        else:
                            #check if it's value can be set to something lower
                            #also set predecessor
                            if self.distance[v] > self.distance[u] + weights[(u,v)]:
                                self.distance[v] = self.distance[u] + weights[(u, v)]
                                self.parent[v] = u

            # run another iteration - if we can still relax an edge that means we have a cycle.
            #do the above ONCE more - if any edge can still be relaxed - that means we have a cycle
            for u in adj.keys():
                #if u is reachable
                if u in self.distance.keys():
                    for v in adj[u]:
                        #if v is at infinity - set it's value
                        #also set predecessor
                        if v not in self.distance.keys():
                            self.distance[v] = self.distance[u] + weights[(u,v)]
                            self.parent[v] = u
                        else:
                            #check if it's value can be set to something lower
                            #also set predecessor
                            if self.distance[v] > self.distance[u] + weights[(u,v)]:
                                print("We have a cycle")
                                self.distance[v] = self.distance[u] + weights[(u, v)]
                                self.parent[v] = u



    def shortest_path_to(self, node):
        print("shortest_path_bmf")
        path = [node]

        while self.parent[node] != None:
            path.append(self.parent[node])
            node = self.parent[node]

        for x in reversed(path):
            print(x, end=" ")


bmf = bellman_ford_SP()
bmf.bellman_ford(positive_weighted_graph, 9, 1, weights)
bmf.shortest_path_to(8)
bmf.shortest_path_to(9)

print("\n Topo SP for DAG")
class DAG_topo_SP:
    def __init__(self):
        self.dfs_parent = {int:int}
        self.parent = {int: int}
        self.topo_order = []
        self.distance = {}


    def dfs_visit(self, adj, u):
        for v in adj[u]:
            if v not in self.dfs_parent:
                self.dfs_parent[v] = u
                self.dfs_visit(adj, v)
        self.topo_order.append(u)

    def dfs_explore(self, adj):
        for u in adj.keys():
            if u not in self.dfs_parent.keys():
                self.dfs_parent[u] = None
                self.dfs_visit(adj, u)

    def find_sp(self, adj, start_node, weights):

        self.dfs_explore(adj)
        #we get our topo order
        self.topo_order = reversed(self.topo_order)

        self.distance[start_node] = 0
        self.parent[start_node] = None
        print("\n The topo order is")
        for v in self.topo_order:
            print(v, end=" ")
            if v in self.distance.keys():
                for u in adj[v]:
                    if u not in self.distance.keys():
                        self.distance[u] = self.distance[v] + weights[(v,u)]
                        self.parent[u] = v
                    else:
                        if self.distance[u] > self.distance[v] + weights[(v,u)]:
                            self.distance[u] = self.distance[v] + weights[(v,u)]
                            self.parent[u] = v

        return

    def find_sp_to(self, node):
        path = [node]

        while self.parent[node] != None:
            path.append(self.parent[node])
            node = self.parent[node]

        print("\n Shortest Path")
        for x in reversed(path):
            print(x, end=" ")


dtsp = DAG_topo_SP()
dtsp.find_sp(positive_weighted_graph, 1, weights)
dtsp.find_sp_to(9)

































