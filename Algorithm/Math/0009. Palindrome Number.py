# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.

# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False
        
        x_reverte = 0
        
        while x > x_reverte:
            x_reverte = x_reverte * 10 + x % 10
            x = x // 10
            
        return (x == x_reverte or x == x_reverte//10)
        
# 只需要反转一半的数字去进行比较就可以了
