class Solution:
    def addBinary(self, a: str, b: str) -> str:
        boo = False
        temp = '0'
        result = []
        if len(a) > len(b):
            b = (len(a)-len(b))*"0" + b
        elif len(b) > len(a):
            a = (len(b) - len(a))*"0" + a
        print(a)
        print(b)

        for i in range(len(a)):
            if a[-(i+1)] == b[-(i+1)]:

                if(a[-(i+1)] == "1"):
                    if temp == "1":
                        result.append("1")
                        temp = "1"
                        boo = True
                    else:
                        result.append("0")
                        temp = "1"
                        boo = True
                else:
                    if temp == "0":
                        result.append("0")
                        temp = "0"
                        boo = False
                    else:
                        result.append("1")
                        temp = "0"
                        boo = False
            else:
                if temp == "0":
                        result.append("1")
                        temp = "0"
                        boo = False
                else:
                    result.append("0")
                    temp = "1"
                    boo = True
        if boo:
            result.append(temp)
        result.reverse()
        print(result)
        return ("".join(result))


obj = Solution()

a = "11" 
b = "1"

print(obj.addBinary(a, b))