# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d = {}
        cnt = 0
        
        for i in A:
            for j in B:
                d[i + j] = d.get(i + j, 0) + 1
                    
        for p in C:
            for q in D:
                cnt += d.get(-(p + q), 0)
                    
        return cnt
        
# 运用Hash Table，A+B=-(C+D)
