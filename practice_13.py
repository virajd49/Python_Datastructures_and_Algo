


"""
Agenda

Practice Sorts
Recollect linked list complexity theory
Recollect Graph + graph exploration + SSSP theory
Implement BST
Solve CCI Graph and Tree end of chapter problems


"""



"""
Graph exploration

 - bfs and dfs Complexity: V + E - where V is the total number of vertices and E is the total number of edges
     - BFS - gives us shortest paths - this can be implemented using a queue or a frontier type system
                                     - as we vist every node - we set the node's parent to be the previous node - to track shortest paths
    - DFS - gives us topological sort and Cycle detection - via edge classification
        - recursion
        - outer for loop that uterates over each vertex as potential starting vertex - to cover for disconnected graph case
         - inner fucntion call is recursive to go as deep as possible for a particular vertex

          - when doing topological sort - whne you visit a node - add it to an array - after the discovery is done - reverse the array
           - cycle detection - if we detect a backward edge - how to detect a backward edge ?
                                                             - if for u in adj[v]
                                                                    u has been visited and u is not a parent of v - we have a backward edge. - so we have a cycle.
"""


adj_list_num = { 1: [2, 4], 2: [5], 3: [5, 6], 4:[2], 5: [4], 6:[6]}

adj_list_dag = {1 : [5], 2 : [1, 5], 3 : [1], 4 : [7], 6 : [1, 2, 3] }

print("\n BFS")

class bfs:
    def __init__(self):
        self.parent = {}

    def bfs_visit(self, adj, start):
        frontier = {start}
        self.parent[start] = None

        while frontier:
            new = []
            for u in frontier:
                for v in adj[u]:
                    #only if we haven't already visited v
                    if v not in self.parent:
                        self.parent[v] = u
                        new.append(v)
            frontier = new

    def bfs_explore(self, adj):

        for v in adj.keys():
            #do a bfs visit on all nodes
            if v not in self.parent:
                self.parent[v] = None
                self.bfs_visit(adj, v)

    def shortest_path_for(self, node):
        curr = node
        path = []

        while curr != None:
            path.append(curr)
            curr = self.parent[curr]


        for x in reversed(path):
            print(x,end=" - ")



    def parent_of(self, node):
        #if we are given a disconnected graph - some node might not have a parent
        if node in self.parent:
            print("\nThe parent of", node, "is", self.parent[node])
        else:
            print("\nThis node has no parent")


bfs_obj = bfs()
bfs_obj.bfs_explore(adj_list_num)
bfs_obj.shortest_path_for(5)
bfs_obj.parent_of(3)
bfs_obj.parent_of(6)
bfs_obj.parent_of(4)

print("\n DFS")

class dfs:
    def __init__(self):
        self.parent = {}


    def dfs_visit(self, adj, u):
        for v in adj[u]:
            print(v)
            if v not in self.parent:
                self.parent[v] = u
                self.dfs_visit(adj, v)

    def dfs_explore(self, adj):

        #for every vertice in the graph - this way we cover the possibility of a disconnected graph as well
        for u in adj.keys():
            #if we haven't already visited the vertice
            if u not in self.parent:
                self.parent[u] = None
                self.dfs_visit(adj, u)

    def parent_of(self, node):
        print("Parent of ", node, "is", self.parent[node])

dfs_obj = dfs()
dfs_obj.dfs_explore(adj_list_num)
dfs_obj.parent_of(4)
dfs_obj.parent_of(6)



"""

Single Source Shortest Path Algorithms

Djikstra's, Bellman Ford and one for DAG'
 - core principle - select vertices in some order - then relax the vertices
  - relax  if d[u] > d[v] + w(v,u)
                then d[u] = d[v] + w(v,u)
  - when you relax set the predecessor of the vertex you are relaxing

Djiktra's O(VlgV + E) - fibonacci heap
 - BFS + DFS - greedy approach Complexity is O(VlogV + E) - using fibonacci heap
 - we add all the vertices to a queue - we set the starting vertex to have distance 0
 - then we we extract the minimum distance vertex from the queue and relax all it's adjacent vertices
 - keep doing this till we can't relax any further.
 
 
 Bellman Ford O(VE) - can also detect negative cycles - will only give shortest paths with non negative cycle graphs
  - We iterate over all edges (u,v) |V| - 1 times and relax the edges
  - set the predecessor for every v
  
 After we are done with |V| - 1 counts - iterate once more - if you can still relax any edge - that means we have a negative cycle
 
 DAG: O(V + E)
  - do a topological sort
  - in topological sort order - relax all the vertices - that should give you shortest path
 """