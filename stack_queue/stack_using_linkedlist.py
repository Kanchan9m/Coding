#Stack using Linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Mystack:
    def __init__(self):
        self.head = None

    def push(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    
    def pop(self):
        if self.head == None:
            return -1
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.data

    def top(self):
        return self.head.data

    def empty(self):
        if self.head == None:
            return True
        return False

s = Mystack()
s.push(5)
s.push(6)
s.push(9)
print(s.empty())
print(s.pop())
print(s.top())