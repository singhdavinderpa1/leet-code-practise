class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_filter = filter(str.isalnum, s)
        alphanumeric_string = "".join(alphanumeric_filter)
        print(alphanumeric_string)
        print(alphanumeric_string[::-1])
        return alphanumeric_string.lower() == alphanumeric_string[::-1].lower()

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))