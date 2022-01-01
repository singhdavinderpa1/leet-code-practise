from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            print("returning from first len")
            return strs[0]
        if len(strs[0]) >= 1:
            for i in range(len(strs[0])):
                for j in range(len(strs)):
                    if len(strs[j]) < 1:
                        print("returning from second return")
                        return ""
                    if(strs[0][0:i+1] in strs[j][0:i+1]):
                        print(f"continuing  {strs[0][0:i+1]}")
                        continue
                    else:
                        print("entered else")
                        print(strs[0][0:i])
                        return strs[0][0:i]
            return strs[0]
        else:
            print("last return")
            return ""

strs = ["c","acc","ccc"]
obj = Solution()
print(obj.longestCommonPrefix(strs))