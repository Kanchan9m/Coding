# Prefix to postfix Conversion using stack

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        stack = []
        
        for i in range(len(pre_exp)-1, -1, -1):
            if pre_exp[i].isalnum():
                stack.append(pre_exp[i])
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                op = operand1 + operand2 + pre_exp[i]
                stack.append(op)
                
        return stack.pop()

pi = Solution()
s = "*-A/BC-/AKL"
print(pi.preToPost(s))