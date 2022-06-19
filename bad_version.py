class Solution:
    def isBadVersion(self, n):
        if n  == 4:
            return True
        else:
            return False

    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            if self.isBadVersion(n):
                return n
        for i in range(n,0,-1):
            if self.isBadVersion(i):
                return i
sol = Solution()
print('>',sol.firstBadVersion(4))