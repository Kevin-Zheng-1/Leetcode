# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        s1 = min(strs)
        s2 = max(strs)
                
        for i, ch in enumerate(s1):
            
            if ch != s2[i]:
                return s1[:i]
            
        return s1
            
# min()和max()两个函数应用于含有字符串的列表中时返回的值是基于字母的排序
