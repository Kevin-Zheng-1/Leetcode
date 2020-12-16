# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:  # handle positive numbers  
            a =  int(str(x)[::-1])  
        if x <=0:  # handle negative numbers  
            a = -1 * int(str(-x)[::-1])
            
        mina = -2**31
        maxa = 2**31 - 1
        if a not in range(mina, maxa):
            return 0
        else:
            return a
            
# string[::-1]可以直接反转字符串    
