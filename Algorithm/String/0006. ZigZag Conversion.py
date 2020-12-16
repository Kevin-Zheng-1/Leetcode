# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
        
# 从头开始遍历，每个元素加入对应行的字符串，每次遍历到第n行时改变方向，回到第1行时再改变方向
