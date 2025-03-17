# Queue using two stacks

class MyStack:
    def __init__(self):
        self.stack = []
        self.length = 0
        self.top = -1

    def isEmpty(self):
        if self.length == 0:
            return True
        return False
    
    def pushele(self, x):
        self.stack.append(x)
        self.length += 1
        self.top += 1
    
    def popl(self):
        item = self.stack.pop()
        self.length -= 1
        self.top -= 1
        return item
    
    def Front(self):
        return(self.stack[self.top])

    def stacksize(self):
        return self.length

class MyQueue:

    def __init__(self):
        self.s1 = MyStack()
        self.s2 = MyStack()

    def push(self, x: int) -> None:
        
        while not self.s1.isEmpty():
            self.s2.pushele(self.s1.Front())
            self.s1.popl()

        self.s1.pushele(x)

        while not self.s2.isEmpty():
            self.s1.pushele(self.s2.Front())
            self.s2.popl()

    def pop(self) -> int:
        return self.s1.popl()

    def peek(self) -> int:
        return self.s1.Front()

    def empty(self) -> bool:
        return self.s1.isEmpty()


obj = MyQueue()
obj.push(10)
obj.push(20)
print(obj.pop())
print(obj.peek())
print(obj.empty())