# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Method 1
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

# Method 2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        i = 0
        
        while True:
            try:
                sets = set([string[i] for string in strs])
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except:
                break
                
        return result

# 利用set()函数来寻找各字符串在相同位置上的唯一值的个数
    
