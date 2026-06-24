class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        a= 0
        b = len(s)-1
        while a<b:
            if s[a] == s[b]:
              a+=1 
              b-=1
            else:
                return False
        return True 

        