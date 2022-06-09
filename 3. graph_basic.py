class Graph:
    def __init__(self, N=1000):
        self.N =N
        self.M =[[0 for _ in range(N)] for _ in range(N)]

    def insert_edge(self,v1,v2):
        vs =[]
        self.M[v1][v2] = 1
        self.M[v2][v1] = 1

    def adjacent_vertices(self,v):
        vs =[]
        for j in range(self.N):
            if self.M[v][j] ==1:
                vs.append(j)
            # 뭐 더 적어야하나
        return vs
class DFS:
    def __init__(self,G):
        self.G = G
        self.N = G.N

        self.UNEXPLORED, self.VISITED = 'unxp','vstd'
        self.DISCOVERY, self.BACK = 'dscv','back'

        self.V_label = [self.UNEXPLORED for _ in range(N)]
        self.E_label = [[self.UNEXPLORED for _ in range(N)] for _ in range(N)]

        self.visit_order = []

        for v in range(self.N):
            if self.V_label[v] == self.UNEXPLORED:
                self.dfs(v)
    def dfs(self,v):
        self.V_label[v] = self.VISITED
        self.visit_order.append(v)

        v_adj = self.G.adjacent_verices(v)
        for w in v_adj:
            if self.E_label[v][w] ==self.UNEXPLORED and self.E_label[w][v] ==self.UNEXPLORED:
                if self.V_label[w] ==self.UNEXPLORED:
                    self.E_label[v][w] =self.DISCOVERY
                    self.dfs(w)
                else:
                    self.E_label[v][w] = self.BACK

