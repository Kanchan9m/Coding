# Stack using two queues

class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.l = 0

    def push(self, x):
        self.queue.append(x)
    
    def popele(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)


    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    def front(self):
        return self.queue[0]

class MyStack:

    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()

    def push(self, x: int) -> None:
        while not self.q1.isEmpty():
            self.q2.push(self.q1.front())
            self.q1.popele()
        self.q1.push(x)
        while not self.q2.isEmpty():
            self.q1.push(self.q2.front())
            self.q2.popele()

    def pop(self) -> int:
        ans = self.q1.front()
        self.q1.popele()
        return ans

    def top(self) -> int:
        return self.q1.front()

    def empty(self) -> bool:
        return self.q1.isEmpty()


obj = MyStack()
obj.push(10)
obj.push(20)
print(obj.pop())
obj.push(30)
print(obj.top())
print(obj.empty())