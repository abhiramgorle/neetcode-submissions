class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s :
            if i in [ '(',  '{',  '['] :
                stack.append(i)
            else:
                k = stack.pop()
                if i == ')':
                    if k != "(":
                        return False
                elif i == "}":
                    if k != "{":
                        return False
                else :
                    if k != "[":
                        return False
        return True
                        
        