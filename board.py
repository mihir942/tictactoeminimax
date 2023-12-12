class Game:
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

newGame = Game()
newGame.play()
