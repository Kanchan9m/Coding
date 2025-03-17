class Mystack:
    def __init__(self,size = 5):
        self.size = size
        self.stack = []*self.size
        self.top = -1
    
    def push(self, new_val):
        if len(self.stack) != self.size:
            self.stack.append(new_val)
            self.top += 1
        else:
            print("stack Overflow")
    
    def popelement(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def Top(self):
        return self.stack[self.top]
    
    def isempty(self):
        if len(self.stack) == 0:
            return True
        return False
    

st = Mystack()
print(st.popelement())
st.push(5)
st.push(4)
st.push(6)
print(st.Top())
st.push(9)
st.push(10)
print(st.Top())
st.push(8)
print(st.isempty())