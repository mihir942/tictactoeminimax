class H_vs_H_Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.currentPlayer = 'X'

    def printBoard(self):
        print("\n".join(["|".join(row) for row in self.board]) + "\n")
    
    def makeMove(self, i: int, j: int):
        self.board[i][j] = self.currentPlayer 

    def switchPlayer(self):
        self.currentPlayer = 'X' if self.currentPlayer == 'O' else 'O'

    def isWinner(self, player: str):
        rowsWin = any(all(cell == player for cell in row) for row in self.board)
        colsWin = any(all(row[col] == player for row in self.board) for col in range(0,3))
        diag1Win = all(self.board[i][i] == player for i in range(3))
        diag2Win = all(self.board[i][2-i] == player for i in range(3))
        return rowsWin or colsWin or diag1Win or diag2Win 

    def boardFull(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def play(self):

        print("Let's begin!\n")
        self.printBoard()

        while True:
            
            if (self.isWinner('X')):
                print("X is the winner\n")
                self.printBoard()
                break

            if (self.isWinner('O')):
                print("O is the winner\n")
                self.printBoard()
                break

            if (self.boardFull()):
                print("It's a draw!\n")
                self.printBoard()
                break

            move = input(f"What is your move, player {self.currentPlayer}? >> ")
            i,j = [int(k) for k in move.split(',')]
            self.makeMove(i,j)
            self.switchPlayer()
            print("")
            self.printBoard()

class H_vs_C_Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def printBoard(self):
        print("\n".join(["|".join(row) for row in self.board]) + "\n")
    
    def _presetBoard(self, preset):
        self.board = preset

    def makeMove(self, move: tuple[int,int]):
        self.board[move[0]][move[1]] = self.whoseTurn()

    def isWinner(self, player: str) -> bool:
        rowsWin = any(all(cell == player for cell in row) for row in self.board)
        colsWin = any(all(row[col] == player for row in self.board) for col in range(0,3))
        diag1Win = all(self.board[i][i] == player for i in range(3))
        diag2Win = all(self.board[i][2-i] == player for i in range(3))
        return rowsWin or colsWin or diag1Win or diag2Win 

    def boardFull(self) -> bool:
        return all(cell != ' ' for row in self.board for cell in row)
    
    def possibleMoves(self) -> list:
        moves = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == ' ':
                    moves.append((r,c))
        return moves

    def whoseTurn(self) -> str:
        x_count = sum(row.count('X') for row in self.board)
        o_count = sum(row.count('O') for row in self.board)
        if (x_count + o_count) % 2 == 0: return 'X'
        else: return 'O'

newGame = H_vs_C_Game()

myboard = [['X','O','X'],
           [' ','X','O'],
           [' ','X','O']]

newGame._presetBoard(preset=myboard)

print(newGame.possibleMoves())
