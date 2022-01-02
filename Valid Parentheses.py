class Solution:
    def isValid(self, s: str) -> bool:
        openbrack = [] 
        closebrack = []
        ob = ["{", "[", "("]
        cb = ["}", "]", ")"]

        brackdict = {"{" : "}", "[":"]", "(":")"}

        for i in range(len(s)):
            if s[i] in ob:
                openbrack.append(s[i])
            else:
                closebrack.append(s[i])
                if len(openbrack) <= 0:
                    return False
                if  brackdict[openbrack.pop()] == s[i]:
                    closebrack.pop()
                    continue
                else:
                    return False      
        if len(openbrack) > 0 :
            return False
        
        return True