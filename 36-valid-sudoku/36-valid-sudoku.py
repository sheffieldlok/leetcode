class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for i in range(len(board)):
            dict = {}
            for j in range(len(board)):
                if board[i][j] in dict and board[i][j] != ".":
                    return False
                else:
                    dict[board[i][j]] = 1
        
        # check each column
        for i in range(len(board)):
            dict = {}
            for j in range(len(board)):
                if board[j][i] in dict and board[j][i] != ".":
                    return False
                else:
                    dict[board[j][i]] = 1
                    
        # check each 3x3 box
        for x in range(len(board) // 3):
            for i in range(len(board) // 3):
                dict = {}
                for j in range(len(board) // 3):
                    for k in range(len(board) // 3):
                        if board[j + 3*x][k + 3*i] in dict and board[j + 3*x][k+3*i] != ".":
                            return False
                        else:
                            dict[board[j+ 3*x][k+3*i]] = 1
                       
        return True

#         # second soln (neetcode)
#         cols = collections.defaultdict(set)
#         rows = collections.defaultdict(set)
#         squares = collections.defaultdict(set) # key = (r // 3, c // 3)
        
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".": 
#                     continue
#                 if (board[r][c] in rows[r] or
#                     board[r][c] in cols[c] or
#                     board[r][c] in squares[(r//3, c//3)]):
#                     return False
#                 cols[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 squares[r//3, c//3].add(board[r][c])
                
#         return True
        
        
        