# Prefix to infix Conversion using stack

class Solution:
    def preToInfix(self, pre_exp):
        p = pre_exp[::-1]
        stack = []
        
        for i in p:
            if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9'):
                stack.append(i)
            else:
                s1 = stack.pop()
                s2 = stack.pop()
                s3 = '('+s1+ i+ s2 + ')'
                stack.append(s3)
        return stack.pop()

pi = Solution()
s = "*-A/BC-/AKL"
print(pi.preToInfix(s))