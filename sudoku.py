from time import sleep

class SudokuSolver():
    def __init__(self, grid, show_solving=False):
        """
        Solves sudoku puzzle for inputted grid using basic backtracking
        Numbers should be inputted as strings, with '.' indicating a blank cell
        :param grid: List[List[int]]
        :param show_solving: bool
        """
        self.grid = grid
        self.show_solving = show_solving
        self.true_grid = [row[:] for row in grid]
        self.grid_converter = {0: range(0,3), 1: range(3,6), 2: range(6,9)}
        self.main()

    ##########################################################################

    def check_row(self, guess, row):
        """
        Returns False if guess is in row, True otherwise
        :param guess: int
        :param row: int
        """
        if guess in self.grid[row]:
            return False
        return True

    def check_column(self, guess, column):
        """
        Returns False if guess is in column, True otherwise
        :param guess: int
        :param column: int
        """
        for row in self.grid:
            if row[column] == guess:
                return False
        return True

    def check_3x3(self, guess, row, column):
        """
        Returns False if guess is in 3x3, True otherwise
        :param guess: int
        :param row: int
        :param col: int
        """
        
        box_row = row//3
        box_col = column//3

        for i in self.grid_converter[box_row]:
            for j in self.grid_converter[box_col]:
                if guess == self.grid[i][j]:
                    return False
        return True

    ##########################################################################

    def solve_cell(self, row, col):
        """
        Return the grid with the specified cell assigned to a viable number
        :param row: int
        :param col: int
        """
        guess = self.grid[row][col]
        while True:
            guess += 1
            if guess > 9:
                self.grid[row][col] = 0
                break
            if not self.check_row(guess, row):
                continue
            if not self.check_column(guess, col):
                continue
            if not self.check_3x3(guess, row, col):
                continue
            self.grid[row][col] = guess
            break

    ##########################################################################

    def main(self):
        """
        Main backtracking function, called implicitly during class' __init__
        """
        solving = True
        has_err = False
        row = col = 0
        while solving:
            try:
                if not has_err:
                    if self.true_grid[row][col] == 0:
                        self.solve_cell(row, col)
                        if self.grid[row][col] == 0:
                            has_err = True
                            continue
                    col += 1
                    if col > 8:
                        row, col = row+1, 0
                else:
                    col -= 1
                    if col < 0:
                        row, col = row-1, 8
                    if self.true_grid[row][col] == 0:
                        has_err = False

                if self.show_solving:
                    for spacer in range(5): #pylint: disable=unused-variable
                        print()
                    for x in self.grid:
                        print(x)
                    sleep(0.01)
                
                if row == 9:
                    solving = False
                    if self.show_solving:
                        print("Puzzle solved")

            except KeyboardInterrupt:
                solving = False
                print("Solver stopped")

##########################################################################

if __name__ == '__main__':
    test_grid = [[5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]]

    test_grid_two = [[0,9,0,5,0,6,0,7,0],
    [6,7,0,0,9,0,5,0,1],
    [1,0,0,0,0,7,0,0,9],
    [0,0,0,0,2,0,0,9,0],
    [0,0,0,7,0,4,0,0,0],
    [0,2,0,1,0,0,0,0,7],
    [7,0,0,0,0,0,1,0,0],
    [0,8,0,0,0,0,0,0,0],
    [4,0,0,6,3,0,0,0,0]]

    a = SudokuSolver(test_grid)
    for a_line in a.grid:
        print(a_line)
    print()

    b = SudokuSolver(test_grid_two, True)
    for b_line in b.grid:
        print(b_line)
