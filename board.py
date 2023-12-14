import copy
from typing import List, Tuple

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
        self.current_board = [[' ' for _ in range(3)] for _ in range(3)]

    def printCurrentBoard(self):
        print("\n".join(["|".join(row) for row in self.current_board]) + "\n")
    
    def printGivenBoard(self, board_state: List[List[str]]):
        print("\n".join(["|".join(row) for row in board_state]) + "\n")

    def _presetBoard(self, preset):
        self.current_board = preset

    def makeMove(self, move: Tuple[int, int]):
        self.current_board[move[0]][move[1]] = self.whoseTurnInState(self.current_board)

    def exploreStateFromMove(self, move: tuple[int, int], board_state: List[List[str]]):
        new_board = copy.deepcopy(board_state)
        new_board[move[0]][move[1]] = self.whoseTurnInState(board_state)
        return new_board

    def isWinnerInState(self, player: str, board_state: List[List[str]]) -> bool:
        rowsWin = any(all(cell == player for cell in row) for row in board_state)
        colsWin = any(all(row[col] == player for row in board_state) for col in range(0,3))
        diag1Win = all(board_state[i][i] == player for i in range(3))
        diag2Win = all(board_state[i][2-i] == player for i in range(3))
        return rowsWin or colsWin or diag1Win or diag2Win 

    def isBoardFullForState(self, board_state: List[List[str]]) -> bool:
        return all(cell != ' ' for row in board_state for cell in row)
    
    def possibleMovesForState(self, board_state: List[List[str]]) -> list:
        moves = []
        for r in range(3):
            for c in range(3):
                if board_state[r][c] == ' ':
                    moves.append((r,c))
        return moves

    def whoseTurnInState(self, board_state: List[List[str]]) -> str:
        x_count = sum(row.count('X') for row in board_state)
        o_count = sum(row.count('O') for row in board_state)
        if (x_count + o_count) % 2 == 0: return 'X'
        else: return 'O'
    
    def minimax(self, board_state: List[List[str]], depth: int) -> float:
        
        # print("Before Exploration Board:")
        # self.printGivenBoard(board_state)

        if self.isWinnerInState('X', board_state):
            return 1.0
        if self.isWinnerInState('O', board_state):
            return -1.0
        if self.isBoardFullForState(board_state):
            return 0.0
        
        player = self.whoseTurnInState(board_state)
        possibleMoves = self.possibleMovesForState(board_state)

        value = None

        # if maximising player's turn (X)
        if player == 'X':
            value = float('-inf')
            for move in possibleMoves:
                new_board_state = self.exploreStateFromMove(move, board_state)
            
                print(f"{int(depth+1)*3*'>'} Depth {depth+1}: Trying move {move} for <{player}>")

                self.printGivenBoard(board_state=new_board_state)

                new_value = self.minimax(new_board_state, depth + 1)

                print(f"{int(depth+1)*3*'>'} Depth {depth+1}: move {move} for <{player}> is assigned VALUE: {new_value}")

                value = max(value, new_value)

            return value

        # if minimising player's turn (O)
        else:
            value = float('inf')
            for move in possibleMoves:
                new_board_state = self.exploreStateFromMove(move, board_state)
                print(f"{int(depth+1)*3*'>'} Depth {depth+1}: Trying move {move} for <{player}>")

                self.printGivenBoard(board_state=new_board_state)

                new_value = self.minimax(new_board_state, depth + 1)

                print(f"{int(depth+1)*3*'>'} Depth {depth+1}: move {move} for <{player}> is assigned VALUE: {new_value}")

                value = min(value, new_value)
            return value

my_game = H_vs_C_Game()

# myboard = [['X','O','X'],
#            ['O','X','O'],
#            [' ','X','O']]


myboard = [['X','O','X'],
           ['O','O','X'],
           [' ','X',' ']]

myboard2 = [['X','O','X'],
           ['O','O','X'],
           ['O','X',' ']]

my_game._presetBoard(preset=myboard)

print(my_game.possibleMovesForState(my_game.current_board))
value = my_game.minimax(board_state=my_game.current_board, depth=0)
print(value)