from Stacklist import StackList

class Slove_maze():
    def __init__ (self,map):
        self.map = map
        self.size = len(map)
        self.solver = [1,1]
        self.road = StackList()
        self.road.Push([self.solver,0])

    def compass(self):
        i = self.solver[0]
        j = self.solver[1]
        way_num = 0
        nextway = 4
        if self.map[i-1][j] == 0 :
            way_num = way_num +1
            if nextway == 4 :
                nextway = 0
        if self.map[i][j-1] == 0 :
            way_num = way_num +1
            if nextway == 4 :
                nextway = 1
        if self.map[i+1][j] == 0 :
            way_num = way_num +1
            if nextway == 4 :
                nextway = 2
        if self.map[i][j+1] == 0 :
            way_num = way_num +1
            if nextway == 4 :
                nextway = 3
        return nextway , way_num
        
    def finding(self):
        i = self.solver[0]
        j = self.solver[1]

        while i != self.size-2 or j != self.size-2:
            self.map[i][j] = 2
            nextway , way_num = self.compass()
            if way_num == 0 :
                pre_record = self.road.Pop()
                while pre_record[1] == 0 :
                    pre_record = self.road.Pop()
                pre_record = self.road.Top
                self.solver = pre_record[0]
                i = self.solver[0]
                j = self.solver[1]
            else:
                if nextway == 0 :
                    self.solver = [i-1,j]
                    i = self.solver[0]
                    j = self.solver[1]
                    record = [self.solver,way_num-1]
                    self.road.Push(record)
                elif nextway == 1 :
                    self.solver = [i,j-1]
                    i = self.solver[0]
                    j = self.solver[1]
                    record = [self.solver,way_num-1]
                    self.road.Push(record)
                elif nextway == 2 :
                    self.solver = [i+1,j]
                    i = self.solver[0]
                    j = self.solver[1]
                    record = [self.solver,way_num-1]
                    self.road.Push(record)
                else:
                    self.solver = [i,j+1]
                    i = self.solver[0]
                    j = self.solver[1]
                    record = [self.solver,way_num-1]
                    self.road.Push(record)

        final_road = []
        roadlen = self.road.Length

        for i in range(0,roadlen):
            r = self.road.Pop()
            final_road.append(r[0])

        return final_road , roadlen


