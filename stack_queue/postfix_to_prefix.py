# Postfix to prefix Conversion using stack

class Solution:
    def postToPre(self, post_exp):
        stack = []
        
        for i in post_exp:
            if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9'):
                stack.append(i)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                op = i + operand2+ operand1
                stack.append(op)
                
        return stack.pop()

pi = Solution()
s = "ABC/-AK/L-*"
print(pi.postToPre(s))
