class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        x = str(x)
        return x == x[::-1]
            

sol = Solution()
result = sol.isPalindrome(121)
print(result)
