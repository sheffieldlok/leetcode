class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rotate 90 degrees clockwise: row become col, col become row
        # swap first, then transpose
        
        left, right = 0, len(matrix) - 1
        
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                
                # Save topleft element into a temporary variable
                topLeft = matrix[top][left + i]
                
                # Shift bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # Shift bottom right into the bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # Shift top right into the bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # Shift top left into top right
                matrix[top + i][right] = topLeft
            
            left += 1
            right -=1
        
        
        
        
        