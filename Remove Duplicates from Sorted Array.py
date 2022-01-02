from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        current = -101
        index=0
        for i in range(len(nums)):
            print(i)
            if nums[i] != current and nums[i] != "_":
                current = nums[count] = nums[i]
                if i != count:
                    nums[i] = "_"
                count += 1                
            else:
                nums[i] = "_"
                #print(nums)
        
        print(nums)
        return count
obj = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]

print(obj.removeDuplicates(nums))