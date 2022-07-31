import math

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:    
        n = len(matrix)
        beg = matrix[0][0]
        end = matrix[-1][-1]
        
        def check(m):
            i, j, cnt = 0, n-1, 0
            for i in range(n):
                while j >= 0 and matrix[i][j] > m: j -= 1
                cnt += (j + 1)
            return cnt
         
        while beg < end:
            mid = (beg + end)//2
            if check(mid) < k:
                beg = mid + 1
            else:
                end = mid
                
        return beg
        
        
        
        
        
        
            
        
        