class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        divisor = 1

        while x >= divisor * 10:
            divisor *= 10

        while x:
            if x // divisor != x % 10: return False
            x = (x % divisor) // 10
            divisor = divisor / 100
            
        return True
    
sol = Solution()

res = int(input("Enter a number to check: "))

print(sol.isPalindrome(res))