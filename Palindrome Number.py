class Solution:
    def isPalindrome(self, x: int) -> bool:
        lis = []
        #Negative numbers are not palindrome
        if x < 0:
                return False
        #while loop to convert the number in a list
        while x//10 >= 1:
            
            lis.append(x%10)
            x = x//10
        lis.append(x)
        print(lis)
        for i in range(len(lis)//2):
            #for j in range(len(lis)//2):
                print(f" 4i is {i} and j is {i}")
                if lis[i] == lis[-(i+1)]:
                    print(f" i is {lis[i]} and j is {lis[-(i+1)]}")
                    continue
                else:
                    print(f" i is {lis[i]} and j is {lis[-(i+1)]}")
                    return False
            

        return True



obj = Solution()

result = obj.isPalindrome(-121)
print(result)