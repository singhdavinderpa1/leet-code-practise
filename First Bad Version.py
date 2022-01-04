# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        start = 1
        end = n
        mid = (n+1) // 2
        
        while(start <= end):
            if isBadVersion(mid):
                end = mid
                mid = (start+end) // 2
                if end == mid:
                    break
            else:
                start = mid+1
                mid = (start+end) // 2
                if end == mid :
                    break
                
        return mid