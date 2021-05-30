sudoku_size = int(input("Enter the number of sudoku list "))

print("\n")
final_list = [[int(input("Enter single number and press enter: "))
               for _ in range(sudoku_size)] for _ in range(sudoku_size)]
print("List is", final_list)


def show_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")

        for column in range(len(board[0])):
            if column % 3 == 0 and column != 0:
                print("|", end=" ")

            if column == 8:
                print(board[row][column])
            else:
                print(board[row][column], end=" ")


class SudokuBoard:
    # Private methods
    def __find_empty_space_in_board(self):
        for rowIndex in range(len(self.board)):
            for columnIndex in range(len(self.board[0])):
                if self.board[rowIndex][columnIndex] == self.emptySpace:
                    return rowIndex, columnIndex

        return None

    def match(self, number, position):
        for rowIndex in range(len(self.board[0])):
            if self.board[position[0]][rowIndex] == number and self.board[1] != rowIndex:
                return False

        for columnIndex in range(len(self.board)):
            if self.board[columnIndex][position[1]] == number and self.board[0] != columnIndex:
                return False

        square_x = position[1] // 3
        square_y = position[0] // 3

        for rowIndex in range(square_y * 3, square_y * 3 + 3):
            for column in range(square_x * 3, square_x * 3 + 3):
                if self.board[rowIndex][column] == number and (rowIndex, column) != position:
                    return False
        return True

    # Public methods
    def __init__(self, board):
        self.board = board
        self.emptySpace = 0

    def solve(self):
        find = self.__find_empty_space_in_board()
        if not find:
            return True
        else:
            row, column = find

        sudokuMinNumber = 1
        sudokuMaxNumber = 10

        for number in range(sudokuMinNumber, sudokuMaxNumber):
            if self.match(number, (row, column)):
                self.board[row][column] = number

                if self.solve():
                    return True

                self.board[row][column] = self.emptySpace

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board


def main():
    sudokuBoard = SudokuBoard(final_list)

    print("\nInit board:")
    show_board(sudokuBoard.get_board())

    # Solve sudoku
    sudokuBoard.solve()

    print("\nOutput board")
    show_board(sudokuBoard.get_board())


if __name__ == "__main__":
    main()
