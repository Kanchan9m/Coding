# Infix to prefix Conversion using stack

class Solution:
    
    def InfixtoPrefix(self, s):
        preced = {'+':1, '-': 1,'*':2, '/':2, '^':3}
        stack = []
        ans = ''
        reverse_s = s[::-1]
        modified_s = ''
        
        for i in reverse_s:
            if i == '(':
                modified_s += ')'
            elif i == ')':
                modified_s += '('
            else:
                modified_s += i
        
        for i in modified_s:
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
        return ans[::-1]

ip = Solution()
s = "(A+B)*C-D+F"
print(ip.InfixtoPrefix(s))