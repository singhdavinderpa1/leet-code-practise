from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        curr = len(nums) // 2
        lowind = 0
        highind = len(nums) - 1
        condition = True
        while(highind - lowind >= 2):
            if nums[curr] == target:
                print(f"match curr is {curr}")
                return curr
            elif nums[curr] < target:
                lowind = curr
                curr = (lowind + highind) //2
                print(f"ind in less than {curr}")
                print(f" high is {highind} low is {lowind} ")
               
            elif nums[curr] > target:
                highind =  curr
                curr = (highind - lowind) // 2
                print(f"ind in greater than {curr}")
                print(f" high is {highind} low is {lowind} ")
            

        if nums[lowind] >= target:
            return lowind
        elif nums[highind] >= target:
            return highind
        else:
             return highind + 1

obj = Solution()

lis = [1,3, 5 ,6]
tar = 2
print(obj.searchInsert(lis, tar))