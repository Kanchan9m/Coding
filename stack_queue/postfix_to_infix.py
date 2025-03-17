# Postfix to infix Conversion using stack

class Solution:
    def postToInfix(self, postfix):
        # Code here
        stack = []
        
        for i in postfix:
            if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9'):
                stack.append(i)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                op = '('+ operand2 + i + operand1 + ')'
                stack.append(op)
        
        return stack.pop()

pi = Solution()
s = "ab*c+"
print(pi.postToInfix(s))