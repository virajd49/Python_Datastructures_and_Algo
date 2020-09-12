


"""
Graphs

BFS, DFS, Topological sort , etc
"""


adj_list = { 'A':['B', 'C', 'D'], 'B':['A'], 'C':['A', 'D', 'E'], 'D' :['A', 'C', 'E', 'G'], 'E':['D', 'C'], 'G':['D', 'F'], 'F':['G']}


class bfs:
    def __init__(self):
        self.parent = {}
        self.level = {}
        self.start_node = None

    def bfs_explore(self,adj, start):

        self.start_node = start
        frontier = [self.start_node]
        self.parent[self.start_node] = None
        self.level[self.start_node] = 0
        lvl = 0
        while frontier:
            node = frontier[0]
            print(node)
            print(frontier)
            lvl += 1
            for nbr in adj[node]:
                if nbr not in self.level:
                    self.level[nbr] = lvl
                    self.parent[nbr] = node
                    frontier.append(nbr)
            frontier.pop(0)

    def shortest_path_for(self, node):
        parent = None
        path = [node]

        while node != self.start_node:
            path.append(self.parent[node])
            node = self.parent[node]


        for x in reversed(path):
            print(x," - ", end="")

    def parent_of(self, node):
        print("\nParent of ", node, "is", self.parent[node])


bfs_obj = bfs()
bfs_obj.bfs_explore(adj_list, 'A')
bfs_obj.shortest_path_for('G')
bfs_obj.parent_of('C')
bfs_obj.parent_of('F')
bfs_obj.parent_of('E')


adj_list_num = { 1: [2, 4], 2: [5], 3: [5, 6], 4:[2], 5: [4], 6:[6]}

adj_list_dag = {1 : [5], 2 : [1, 5], 3 : [1], 4 : [7], 6 : [1, 2, 3] }

class dfs:
    def __init__(self):
        self.parent = {}
        self.topo_sort = []

    def dfs_visit(self, adj, start):
        for v in adj[start]:
            if v not in self.parent:
                self.parent[v] = start
                self.dfs_visit(adj, v)

    def dfs(self, adj):
        #do dfs visit for all Vertices
        for v in adj.keys():  #this helps if we have disconnected graph
            if v not in self.parent:
                self.parent[v] = None
                self.dfs_visit(adj, v)

    def parent_of(self, node):
        print("Parent of", node, "is", self.parent[node])

    def dfs_visit_for_topo(self, adj, start):
        if start in adj.keys():
            for v in adj[start]:
                if v not in self.parent:
                    self.parent[v] = start
                    self.dfs_visit_for_topo(adj, v)
        self.topo_sort.append(start)

    def dfs_for_topo(self, adj):
        for v in adj.keys():
            if v not in self.parent:
                self.parent[v] = None
                self.dfs_visit_for_topo(adj, v)

    def topological_sort(self, adj):
        self.dfs_for_topo(adj)
        for x in reversed(self.topo_sort):
            print(x, end= " ")




dfs_obj = dfs()
"""
dfs_obj.dfs(adj_list_num)
dfs_obj.parent_of(1)
dfs_obj.parent_of(2)
dfs_obj.parent_of(5)
dfs_obj.parent_of(4)
"""

dfs_obj.topological_sort(adj_list_dag)







