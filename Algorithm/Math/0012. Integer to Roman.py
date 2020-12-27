class Solution:
    def intToRoman(self, num: int) -> str:
        
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        
        for value, roman in digits:
            if num == 0:
                break
            
            count, num = divmod(num, value)
            roman_digits.append(count*roman)
        
        return ''.join(roman_digits)

# 贪心算法，把能表示出来的数全部列出，然后挨个遍历寻找当前数字与之最相近的数字
