# undirected G(V,E). V={s,r,v,w,t,x,u,y}
# each edge weight=1
# s-r-w/
# r-s-v/
# v-r/
# w-s-t-x/
# t-w-x-u/
# x-w-t-u-y/
# u-t-x-y/
# y-x-u/
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.make_graph()

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print(self):
        for k, v in self.graph.items():
            print(k, v)

    def make_graph(self):
        self.add_edge(1, 0)
        self.add_edge(1, 5)
        self.add_edge(0, 1)
        self.add_edge(0, 4)
        self.add_edge(4, 0)
        self.add_edge(5, 1)
        self.add_edge(5, 2)
        self.add_edge(5, 6)
        self.add_edge(2, 5)
        self.add_edge(2, 6)
        self.add_edge(2, 3)
        self.add_edge(6, 5)
        self.add_edge(6, 2)
        self.add_edge(6, 3)
        self.add_edge(6, 7)
        self.add_edge(3, 2)
        self.add_edge(3, 6)
        self.add_edge(3, 7)
        self.add_edge(7, 6)
        self.add_edge(7, 3)

    def do_bfs(self, start_node):
        print('do_bfs')
        visited = [False] * len(self.graph)
        queue = []
        queue.append(start_node)
        visited[start_node] = True

        while queue:
            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True
        print('\n')

    def do_dfs(self, start_node):
        print('do_dfs')
        visited = [False] * len(self.graph)
        stack = []
        stack.append(start_node)
        visited[start_node] = True

        while stack:
            s = stack.pop()
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] is False:
                    stack.append(i)
                    visited[i] = True
        print('\n')


g = Graph()
g.do_bfs(1)
g.do_dfs(1)
g.print()