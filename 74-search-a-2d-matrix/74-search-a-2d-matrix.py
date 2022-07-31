class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0]) 
#         left_m = 0
#         left_n = 0
#         right_m = m-1
#         right_n = n-1
        
#         while left_m < right_m:
#             mid_m = m // 2
#             mid_n = n // 2
            
#             if target == matrix[mid_m][mid_n]:
#                 return True
#             elif target < matrix[mid_m][mid_n]:
#                 right_m = mid_m
#                 right_n = mid_n
#                 mid_m = (mid_m - left_m) // 2
#                 mid_n = (mid_n - left_n) // 2
#             else:
#                 left_m = mid_m
#                 left_n = mid_n
#                 mid_m = (right_m - mid_m) // 2
#                 mid_n = (right_n - mid_n) // 2
        
#         return false

        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
            