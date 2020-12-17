# Implement atoi which converts a string to an integer.
'''
Example 1:
Input: str = "42"
Output: 42

Example 2:
Input: str = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: str = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: str = "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        l = []
        sign = 1
        
        for i in range(len(s)):
            
            if s[i] == ' ':
                continue
            elif s[i] == '-':
                sign = -1
                if i == len(s) - 1 or ord(s[i+1]) not in range(ord('0'), ord('9')+1):
                    break
            elif s[i] == '+':
                sign = 1
                if i == len(s) - 1 or ord(s[i+1]) not in range(ord('0'), ord('9')+1):
                    break
            elif ord(s[i]) in range(ord('0'), ord('9')+1):
                l.append(s[i])
                if i == len(s) - 1 or ord(s[i+1]) not in range(ord('0'), ord('9')+1):
                    break
                
            else:
                break
                
        if len(l) == 0:
            return 0
        
        result_str = ''.join(l)
        result_int = int(result_str)
        result_final = sign * result_int
        
        if result_final not in range(-2**31, 2**31):
            if sign == 1:
                return 2**31 - 1
            else:
                return -2**31
        
        return result_final
        
# 检查所有的条件        
