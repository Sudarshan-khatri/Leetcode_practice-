class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome=x
        rev=0
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        if(rev==palindrome):
            return True
        else:
            return False

obj1=Solution()
print(obj1.isPalindrome(121))
print(obj1.isPalindrome(-121))
