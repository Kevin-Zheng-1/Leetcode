# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        n = len(s)
        m = len(t)
        
        # Ensure that s is shorter than t
        if n > m:
            return self.isOneEditDistance(t, s)
        
        # The strings are NOT one edit away distance 
        # if the length diff is more than 1
        if m - n > 1:
            return False
        
        for i in range(n):
            if s[i] != t[i]:
                # If strings have the same length
                if n == m:
                    return s[i+1:] == t[i+1:]
                # If strings have different lengths
                else:
                    return s[i:] == t[i+1:]
        
        # If there is no diffs on n distance,
        # the strings are one edit away only if t has one more char
        return n + 1 == m
        
# 从头开始遍历，当遇到s[i]!=t[i]时，分长度相同或不同两种情况讨论，
# 长度相同时剩余部分若相同则返回true，长度不同时短字符串从第i位起到末尾和长字符串从第i+1位起到末尾相同则返回true       
