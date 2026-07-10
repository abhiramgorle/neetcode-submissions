class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0 :
            return False
        stack = []
        for i in s :
            if i in [ '(',  '{',  '['] :
                stack.append(i)
            else:
                if len(stack) ==0:
                    return False
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
        if len(stack) ==0:
            return True
        else:
            return False
                        
        