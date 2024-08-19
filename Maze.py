import random

class GetMaze():
    def __init__(self, width : int=5, high : int=5):
        self.width = width // 2        
        self.high = high // 2    
        self.fa = {}             
        self.mp = []         
        for i in range(0, self.high * 2 + 1):
            self.mp.append([1] * (self.width * 2 + 1))
        for i in range(1, self.high * 2, 2):
            for j in range(1, self.width * 2, 2):
                self.mp[i][j] = 0
                self.fa[(i, j)] = (i, j)

        self.gen()
 
    def get(self):
        return self.mp
 
    def gen(self):
        wait = []
        for i in range(1, self.high * 2, 2):
            for j in range(2, self.width * 2, 2):
                wait.append((i, j))

        for i in range(2, self.high * 2, 2):
            for j in range(1, self.width * 2, 2):
                wait.append((i, j))
        while len(wait):
            idx = random.randint(0, len(wait) - 1)
            e = wait.pop(idx)
            p1, p2 = self.arround(e)
            if self.find(p1) != self.find(p2):
                self.union(p1, p2)
                self.mp[e[0]][e[1]] = 0
 
    def arround(self, e):
        if e[0] % 2:
            return (e[0], e[1] - 1), (e[0], e[1] + 1)
        else:
            return (e[0] - 1, e[1]), (e[0] + 1, e[1])
 
    def find(self, p1):
        if p1 != self.fa[p1]:
            self.fa[p1] = self.find(self.fa[p1])
        return self.fa[p1]
 
    def union(self, p1, p2):
        pp1 = self.find(p1)
        pp2 = self.find(p2)
        self.fa[pp1] = pp2


