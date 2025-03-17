# Infix to postfix Conversion using stack
class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        #code here
        preced = {'+':1, '-': 1,'*':2, '/':2, '^':3}
        stack = []
        ans = ''
        
        for i in s:
            if i.isalnum():
                ans += i
                
            elif i == '(':
                stack.append(i)
                
            elif i == ')':
                while len(stack) != 0 and stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()
            
            else:
                while len(stack) != 0 and stack[-1] != '(' and preced[i] <= preced[stack[-1]]:
                    ans += stack.pop()
                stack.append(i)
        
        while len(stack) != 0:
            ans += stack.pop()
        return ans

ip = Solution()
s = "a+b*(c^d-e)^(f+g*h)-i"
print(ip.InfixtoPostfix(s))