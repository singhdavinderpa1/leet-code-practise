from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        i=0
        result = nums1
        nums1 = []
        while i <= m+n:
            if result[i] == 0:
                print(nums1)
                nums1.append(nums2[j])
                print(f'appending {nums2[j]} = zero')
                i += 1
                j += 1
                if j>=(len(nums2)):
                        break
            else :
                if result[i] == nums2[j]:
                    nums1.append(result[i])
                    nums1.append(result[i])
                    print(f'appending {result[i]} two times')
                    j+=1
                    i+=1
                    if j>=(len(nums2)-1):
                        break
                elif result[i] < nums2[j]:
                    print(f'appending {result[i]} in less than')
                    nums1.append(result[i])
                    i+=1
                    continue
                elif result[i] > nums2[j]:
                    print(f'appending {nums2[j]} greater than')
                    nums1.append(nums2[j])
                    
                    j+=1
                    if j>=(len(nums2)-1):
                        break
                    
        print(nums1)   
        nums1 = result
        


obj = Solution()

list1 = [1,2,3,0,0,0]
list2 = [2,5,6]

obj.merge(list1,3,list2,3)