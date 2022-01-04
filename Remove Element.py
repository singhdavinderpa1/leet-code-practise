from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        queue = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                queue.append(i)
                nums[i] = "_"
            else:
                #i < queue[0]  :
                count += 1
                if queue:
                    if i > queue[0]:
                        nums[queue.pop(0)] = nums[i]
                        nums[i]  = "_"
                        queue.append(i)
        print()   
        print(nums)

        return count


obj = Solution()

nums = [0,1,2,2,3,0,4,2]

print(obj.removeElement(nums, 2))