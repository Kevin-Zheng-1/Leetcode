# Given a string s, find the length of the longest substring without repeating characters.

class Solution:

    def lengthOfLongestSubstring(self, s):
        longest = 0
        left, right = 0, 0
        char = set()
        
        while right < len(s):
            if s[right] not in char:
                char.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                char.remove(s[left])
                left += 1
        
        return longest
