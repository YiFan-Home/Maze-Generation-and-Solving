import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from Maze import GetMaze
from MazeSlove import Slove_maze
from Stacklist import StackList
import copy
import time
import keyboard

class MazePage():
    def __init__(self,root):
        self.root=root
        self.root.title('MAZE_Show')
        self.root.geometry('1300x800')
        self.root.resizable(height = False,width = False)
        self.size = tk.StringVar()
        self.CraetPage()

    def CraetPage(self):
        s = ttk.Style()
        s.configure('my.TButton', font=('FangSong',20,'bold'))
        self.figure = tk.Canvas(self.root,bg='palegreen',width=800,height=760)
        self.figure.place(x=20,y=20)

        ttk.Label(self.root,text="迷 宫",font=('FangShong',30)).place(x=1020,y=50,width=100,height=50)
        ttk.Label(self.root,text="迷宫大小：",font=('FangShong',20)).place(x=895,y=200,width=150,height=50)
        self.entry_Size = ttk.Entry(self.root,textvariable=self.size,font=30)
        self.entry_Size.place(x=1045,y=200,width=200,height=50)

        ttk.Button(self.root,text="生成迷宫",style='my.TButton',command = self.maze_show).place(x=1000,y=300,width=150,height=50)
        ttk.Button(self.root,text="直接求解",style='my.TButton',command = self.just_slove).place(x=1000,y=400,width=150,height=50)
        ttk.Button(self.root,text="解迷动画",style='my.TButton',command = self.Slove).place(x=1000,y=500,width=150,height=50)
        ttk.Button(self.root,text="清 空",style='my.TButton',command = self.Clear).place(x=1150,y=700,width=100,height=50)
        ttk.Button(self.root,text="重置",style='my.TButton',command = self.Reset).place(x=1000,y=700,width=100,height=50)

    def maze_show(self):
        self.figure.delete(tk.ALL)
        size = int(self.size.get())
        maze = GetMaze(size,size)
        self.maze_ormap = maze.get()
        self.num = ((size // 2)*2 + 1)
        self.cell_len = 720 // self.num
        self.cell = []
        for i in range(0,self.num):
            self.cell.append([])

        for i in range(0,self.num):
            for j in range(0,self.num):
                leftx = 40 + self.cell_len*j
                lefty = 20 + self.cell_len*i
                rightx = leftx + self.cell_len
                righty = lefty +self.cell_len
                if self.maze_ormap[i][j] == 1 :
                    rec = self.figure.create_rectangle(leftx,lefty,rightx,righty,fill='saddlebrown',outline='saddlebrown')
                    self.cell[i].append(rec)
                else:
                    if i == 1 and j == 1 :
                        rec = self.figure.create_rectangle(leftx,lefty,rightx,righty,fill='pink',outline='pink')
                        self.cell[i].append(rec)
                    elif i == self.num-2 and j == self.num-2 :
                        rec = self.figure.create_rectangle(leftx,lefty,rightx,righty,fill='red',outline='red')
                        self.cell[i].append(rec)
                    else:
                        rec = self.figure.create_rectangle(leftx,lefty,rightx,righty,fill='white',outline='white')
                        self.cell[i].append(rec)


    def Clear(self):
        self.entry_Size.delete(0,'end')
        self.figure.delete(tk.ALL)


    def Slove(self):
        self.solver = [1,1]
        self.road = StackList()
        self.road.Push([self.solver,0])
        self.maze_map = copy.deepcopy(self.maze_ormap)

        i = self.solver[0]
        j = self.solver[1]
        leftx = 40 + self.cell_len*j
        lefty = 20 + self.cell_len*i
        rightx = leftx + self.cell_len
        righty = lefty +self.cell_len
        self.finder = self.figure.create_oval(leftx,lefty,rightx,righty,fill='orange',outline='orange')
        #self.figure.itemconfig(self.cell[i][j], fill='lightcoral',outline='lightcoral')
        self.figure.update_idletasks()

        while i != self.num-2 or j != self.num-2:
            self.maze_map[i][j] = 2

            self.figure.itemconfig(self.cell[i][j], fill='lightcoral',outline='lightcoral')
            self.figure.update_idletasks()
            
            nextway , way_num = self.compass()
            if way_num == 0 :
                pre_record = self.road.Pop()
                while pre_record[1] == 0 :
                    pre_record = self.road.Pop()

                    time.sleep(0.15)
                    self.figure.itemconfig(self.cell[self.solver[0]][self.solver[1]], fill='silver',outline='silver')
                    self.solver = pre_record[0]
                    i = self.solver[0]
                    j = self.solver[1]
                    leftx = 40 + self.cell_len*j
                    lefty = 20 + self.cell_len*i
                    rightx = leftx + self.cell_len
                    righty = lefty +self.cell_len
                    self.figure.coords(self.finder,leftx,lefty,rightx,righty)
                    self.figure.update_idletasks()


                pre_record = self.road.Top
                self.figure.itemconfig(self.cell[self.solver[0]][self.solver[1]], fill='silver',outline='silver')
                self.solver = pre_record[0]
                i = self.solver[0]
                j = self.solver[1]

                leftx = 40 + self.cell_len*j
                lefty = 20 + self.cell_len*i
                rightx = leftx + self.cell_len
                righty = lefty +self.cell_len
                time.sleep(0.15)
                self.figure.coords(self.finder,leftx,lefty,rightx,righty)

            else:
                if nextway == 0 :
                    self.solver = [i-1,j]
                    i = self.solver[0]
                    j = self.solver[1]

                    leftx = 40 + self.cell_len*j
                    lefty = 20 + self.cell_len*i
                    rightx = leftx + self.cell_len
                    righty = lefty +self.cell_len
                    time.sleep(0.15)
                    self.figure.coords(self.finder,leftx,lefty,rightx,righty)

                    record = [self.solver,way_num-1]
                    self.road.Push(record)
                elif nextway == 1 :
                    self.solver = [i,j-1]
                    i = self.solver[0]
                    j = self.solver[1]

                    leftx = 40 + self.cell_len*j
                    lefty = 20 + self.cell_len*i
                    rightx = leftx + self.cell_len
                    righty = lefty +self.cell_len
                    time.sleep(0.15)
                    self.figure.coords(self.finder,leftx,lefty,rightx,righty)

                    record = [self.solver,way_num-1]
                    self.road.Push(record)
                elif nextway == 2 :
                    self.solver = [i+1,j]
                    i = self.solver[0]
                    j = self.solver[1]

                    leftx = 40 + self.cell_len*j
                    lefty = 20 + self.cell_len*i
                    rightx = leftx + self.cell_len
                    righty = lefty +self.cell_len
                    time.sleep(0.15)
                    self.figure.coords(self.finder,leftx,lefty,rightx,righty)

                    record = [self.solver,way_num-1]
                    self.road.Push(record)
                else:
                    self.solver = [i,j+1]
                    i = self.solver[0]
                    j = self.solver[1]

                    leftx = 40 + self.cell_len*j
                    lefty = 20 + self.cell_len*i
                    rightx = leftx + self.cell_len
                    righty = lefty +self.cell_len
                    time.sleep(0.15)
                    self.figure.coords(self.finder,leftx,lefty,rightx,righty)

                    record = [self.solver,way_num-1]
                    self.road.Push(record)


    def compass(self):
        i = self.solver[0]
        j = self.solver[1]
        way_num = 0
        nextway = 4
        if self.maze_map[i-1][j] == 0 :
            way_num = way_num +1
            if nextway == 4 :
                nextway = 0
        if self.maze_map[i][j-1] == 0 :
            way_num = way_num +1
            if nextway == 4 :
                nextway = 1
        if self.maze_map[i+1][j] == 0 :
            way_num = way_num +1
            if nextway == 4 :
                nextway = 2
        if self.maze_map[i][j+1] == 0 :
            way_num = way_num +1
            if nextway == 4 :
                nextway = 3
        return nextway , way_num


    def just_slove(self):
        mazemap = copy.deepcopy(self.maze_ormap)
        road = Slove_maze(mazemap)
        final_road , roadlen = road.finding()

        for r in range(1,roadlen):
            i = final_road[r][0]
            j = final_road[r][1]
            self.figure.itemconfig(self.cell[i][j], fill='teal',outline='teal')
        
            
    def Reset(self):
        self.figure.delete(tk.ALL)
        self.cell = []
        for i in range(0,self.num):
            self.cell.append([])

        for i in range(0,self.num):
            for j in range(0,self.num):
                leftx = 40 + self.cell_len*j
                lefty = 20 + self.cell_len*i
                rightx = leftx + self.cell_len
                righty = lefty +self.cell_len
                if self.maze_ormap[i][j] == 1 :
                    rec = self.figure.create_rectangle(leftx,lefty,rightx,righty,fill='saddlebrown',outline='saddlebrown')
                    self.cell[i].append(rec)
                else:
                    if i == 1 and j == 1 :
                        rec = self.figure.create_rectangle(leftx,lefty,rightx,righty,fill='pink',outline='pink')
                        self.cell[i].append(rec)
                    elif i == self.num-2 and j == self.num-2 :
                        rec = self.figure.create_rectangle(leftx,lefty,rightx,righty,fill='red',outline='red')
                        self.cell[i].append(rec)
                    else:
                        rec = self.figure.create_rectangle(leftx,lefty,rightx,righty,fill='white',outline='white')
                        self.cell[i].append(rec)


root=tk.Tk()
MazePage(root)
root.mainloop()