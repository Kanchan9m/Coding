class Myqueue:
    def __init__(self, size = 5):
        self.size = size
        self.queue = []*self.size
        self.front = 0
        self.rear = 0
    
    def inqueue(self,val):
        if self.size >= self.rear:
            self.queue.append(val)
            self.rear += 1
        print(self.queue)
    
    def dequeue(self):
        if self.front <= self.rear:
            popelement = self.queue[0]
            self.queue.pop(0)
            self.rear -= 1
            return popelement
        
    def frontele(self):
        return self.queue[self.front]
    
    def isempty(self):
        if self.rear == 0:
            return True
        return False
    
que = Myqueue()
que.inqueue(5)
que.inqueue(8)
que.inqueue(9)
print(que.dequeue())
print(que.frontele())
print(que.isempty())