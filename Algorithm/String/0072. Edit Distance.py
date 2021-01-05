# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)
        
        # If one of the strings is empty
        if n * m == 0:
            return n + m
        
        # Create a distance matrix
        d = [[0] * (m+1) for _ in range(n+1)]
        
        # Init boundaries
        for i in range(n+1):
            d[i][0] = i
        for j in range(m+1):
            d[0][j] = j
            
        # DP
        for i in range(1, n+1):
            for j in range(1, m+1):
                left = d[i-1][j] + 1
                down = d[i][j-1] + 1
                left_down = d[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    left_down += 1
                
                d[i][j] = min(left, down, left_down)
                
        return d[n][m]
        
 # The minimum edit distance algorithm. 构建一个距离矩阵，初始化第一行第一列，即相对应的行数/列数，
 # 然后每一步取上一步三个结果的最小值，即从上往下的insert；从左往右的delete；从左上往右下的substitute
