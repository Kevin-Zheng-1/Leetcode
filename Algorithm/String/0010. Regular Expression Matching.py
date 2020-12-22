# Given an input string (s) and a pattern (p), 
# implement regular expression matching with support for '.' and '*' where: 

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # Initialize the table with False
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        
        # Update the corner case of matching two empty strings
        table[0][0] = True
        
        # Update the corner case of when s is an empty string but p is not
        for i in range(2, len(p) + 1):
            table[i][0] = table[i-2][0] and p[i-1] == '*'
            
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                
                if p[i-1] != '*':
                    # Update the table by referring the diagonal element
                    table[i][j] = table[i-1][j-1] and \
                            (p[i-1] == s[j-1] or p[i-1] == '.')
                else:
                    table[i][j] = table[i-2][j] or table[i-1][j]
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        table[i][j] = table[i][j] | table[i][j-1]
                        
        return table[-1][-1]
                
