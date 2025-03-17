class MinStack:

    def __init__(self):
        self.stack= []
        self.minstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            x = min(self.minstack[-1],val)
            self.minstack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
print(obj.top())
print(obj.getMin())