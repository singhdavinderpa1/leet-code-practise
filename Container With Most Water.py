from typing import List
class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        temp = 0
        leftpt = 0
        rightpt = len(height) - 1
        
        while(leftpt < rightpt):
            
            if(height[rightpt] > height[leftpt]):
                temp = (rightpt - leftpt) * (height[leftpt])
                leftpt += 1
            else:
                temp = (rightpt - leftpt) * height[rightpt]
                rightpt -= 1

            if area < temp:
                area = temp
        
        return area
obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))





