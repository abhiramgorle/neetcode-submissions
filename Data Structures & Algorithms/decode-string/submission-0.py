class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        # while i < n:
        #     while s[i] != "]":
        #         if s[i].islower():
        #             stck.append(stck.pop()+s[i])
                    
        #         elif s[i].isnumeric():
        #             stck.append(s[i])
        #             i+=1
        for i in range(n):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1]!= "[":
                    substr = stack.pop() +substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit() :
                    k = stack.pop()+k
                stack.append(int(k)*substr)  
        return "".join(stack)     

            
            