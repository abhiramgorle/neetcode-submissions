import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sym = ['+', '-', '*', '/']
        for i in tokens :
            if i in sym :
                l2 = stack.pop()
                l1 = stack.pop()
                if i == "+":
                    stack.append(l2+l1)
                elif i == "*":
                    stack.append(l1*l2)
                elif i =="-":
                    stack.append(l1-l2)
                else:
                    stack.append(math.trunc(l1/l2))
            else:
                stack.append(int(i))
        return int(stack.pop())
        