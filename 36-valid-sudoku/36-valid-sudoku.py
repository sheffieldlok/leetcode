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
                print(dict)
        
        # check each column
        print("")
        for i in range(len(board)):
            dict = {}
            for j in range(len(board)):
                if board[j][i] in dict and board[j][i] != ".":
                    return False
                else:
                    dict[board[j][i]] = 1
                print(dict)
                    
        # check each 3x3 box
        print("")
        for x in range(len(board) // 3):
            for i in range(len(board) // 3):
                dict = {}
                for j in range(len(board) // 3):
                    for k in range(len(board) // 3):
                        if board[j + 3*x][k + 3*i] in dict and board[j + 3*x][k+3*i] != ".":
                            return False
                        else:
                            dict[board[j+ 3*x][k+3*i]] = 1
                        print(dict)
                        
        return True
        