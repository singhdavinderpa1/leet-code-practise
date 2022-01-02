class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) < 1:
            return 0
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i + len(needle)] == needle:
                    return i
        else:
            return -1        

        return 0

obj = Solution()

sentence1 = ""
sentence2 = ""

print(obj.strStr(haystack = "hello", needle = "ll"))