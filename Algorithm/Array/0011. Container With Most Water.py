# Given n non-negative integers a1, a2, ..., an, 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxA = 0
        left = 0
        right = len(height) - 1
        
        while left != right:
            A = min(height[left], height[right]) * (right - left)
            maxA = max(maxA, A)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return maxA
            
# 双指针，比较左右两个数字的大小，小的数字往前移。             
