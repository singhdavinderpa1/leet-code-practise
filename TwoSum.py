class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(str(nums) + " "+ str(target))
        hmap = {}
        result = []
        for i in range(len(nums)):
            hmap[nums[i]] = i
        for j in range(len(nums)):
            try:
                hmap[target - nums[j]]
                if j == hmap[target - nums[j]]:
                    continue
                result = [j, hmap[target - nums[j]]]
                break
            except KeyError:
                continue
        return result