#Queue using Linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front  == None:
            return True
        return False
        
    def push(self, item): 
        newnode = Node(item)
        if self.rear == None:
            self.front = newnode
            self.rear = newnode
    
        else:
            self.rear.next = newnode
            self.rear = newnode
        
        
    def pop(self):
        if self.isEmpty():
            return 
        else:
            temp = self.front
            self.front = temp.next
            return temp.data
    
    def peek(self):
        return self.front.data
    
s = queue()
s.push(6)
s.push(3)
s.push(4)
s.push(5)
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())