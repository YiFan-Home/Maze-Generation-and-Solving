class StackList():
    """
    栈及其基本操作：
        object=StackList()
        入栈 .Push(element)  栈的长度.Length  判断是否为空栈.IsEmpty()
        获得栈顶元素.Top  出栈.Pop()  删除栈顶元素.DeleteTop()
        清空栈.Clear()  全部出栈.AllPop()  显示栈.Show()
    """
    def __init__(self):
        """
        初始化：
            .__data : 栈储存空间
                类型：私有变量
            .__top : 栈顶位置
                类型：私有变量
        """
        self.__data=[]
        self.__top=0

    def Push(self,element):
        """
        入栈
            ：向栈中加入元素
            element : 插入的元素
        返回类型
            ：无
        """
        self.__data.append(element)
        self.__top=self.__top+1

    @property
    def Length(self):
        """
        获取栈长度
            ：返回栈的长度（即栈中元素个数）
        返回类型
            ：int
        """
        return self.__top


    def IsEmpty(self):
        """
        判断栈是否为空
            ：栈为空，返回True ; 栈非空，返回False
        返回类型
            ：bool
        """
        if self.__top==0:
            return True
        else:
            return False

    @property
    def Top(self):
        """
        获取栈顶元素
            ：返回栈顶元素，不进行出栈操作
        返回类型
            ：栈中元素类型
        """
        if self.__top == 0:
            print("错误：此栈为空Top")
        else:
            return self.__data[self.__top-1]

    def Pop(self):
        """
        出栈操作
            ：删除栈顶元素,并返回该元素
        返回类型
            ：栈中元素类型
        """
        if self.__top == 0:
            print("错误：此栈为空Pop")
        else:
            box=self.__data[self.__top-1]
            del self.__data[self.__top-1]
            self.__top=self.__top-1
            return box

    def DeleteTop(self):
        """
        删除栈顶元素
            ：区别于Pop, DeleteTop只删除不返回元素
        返回类型
            ：无
        """
        if self.__top == 0:
            print("错误：此栈为空")
        else:
            del self.__data[self.__top-1]
            self.__top=self.__top-1

    def Clear(self):
        """
        清空栈
            ：不同于AllPop,Clear仅出栈，不进行不返回操作
        返回类型
            ：无
        """
        self.__data.clear()
        self.__top=0

    def AllPop(self):
        """
        全部出栈
            ：栈中所有元素全部出栈，并以列表形式返回（列表0索引处为栈顶元素）
        返回类型
            ：列表
        """
        stack=[]
        if self.IsEmpty() :
            print("错误：此栈为空")
        else:
            while self.IsEmpty() != True :
                stack.append(self.Pop())
            return stack
            
    def Show(self):
        """
        显示栈
            ：不同于AllPop,Show无返回，不进行出栈操作，直接将列表元素以列表形式打印出，且第一个元素为栈顶元素
        返回类型
            ：无
        """
        if self.__top == 0:
            print("此栈为空")
        else:
            traver=[]
            for i in range (1,self.__top+1):
                traver.append(self.__data[self.__top-i])
            print(traver)
   