from collections import defaultdict
import sys

class graph:
    def __init__(self,v):
        self.graph=defaultdict(list)
        self.vertex=v
        self.dist=0
        self.visited=[False]*self.vertex
        self.connected=[0]*self.vertex

    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfsutill(self,i):
        self.visited[i]=True
        self.connected[self.dist-1]+=1
        for j in self.graph[i]:
            if self.visited[j]==False:
                self.dfsutill(j)

    def dfs(self):
        for i in range(self.vertex):
            if self.visited[i]==False:
                self.dist+=1
                self.dfsutill(i)


n,m,k=map(int,input().split())

g=graph(n)
for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    g.addedge(u,v)

g.dfs()
if g.dist>k:
    print(-1)
    sys.exit()

else:
    m1=0
    for i in g.connected:
        if i!=0:
            m1+= (i-1)

    print(m-m1+(k-g.dist))