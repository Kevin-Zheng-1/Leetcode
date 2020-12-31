# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.

import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        diff = math.inf
        nums.sort()
        
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                    
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
                    
            if diff == 0:
                break
                
        return target - diff
        
# 双指针，更新sum和target之间的差值
