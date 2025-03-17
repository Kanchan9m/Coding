class Solution:
    def isValid(self, s):
        d = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i in d:
                if len(stack) != 0 and d[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if len(stack) == 0:
            return True
        return False
    
st = Solution()
p = '([])'
print(st.isValid(p))









