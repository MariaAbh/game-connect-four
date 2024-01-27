class Game():
    def __init__(self):
        self.grid = [[' ' for i in range(7)] for j in range(6)]

    def __str__(self):
        # grid_str = '\n'.join(''.join(row) for row in self.grid)
        grid_str = '\n'.join(map(''.join, self.grid))
        return grid_str

    def place_mark(self,col,mark):
        for r in range(len(self.grid)):
            if self.grid[r][col] != ' ':
                self.grid[r-1][col] = mark
                return self.is_winner(mark,r-1,col)
        self.grid[r][col] = mark
        return self.is_winner(mark,r,col)

    def is_winner(self,mark,row,col):
        return self.check_vertical(mark,row,col) or self.check_horizontal(mark,row,col) or self.check_diagonal(mark,row,col)

    def check_vertical(self,mark,row,col):
        count = 0
        for i in range(1,4):
            if (row-i > -1 and self.grid[row-i][col] == mark):
                count += 1
            if (row+i < 6 and self.grid[row+i][col] == mark):
                count += 1
        if count == 3:
            return True
        else:
            return False

    def check_horizontal(self,mark,row,col):
        count = 0
        i = 1
        while col-i > -1 and self.grid[row][col-i] == mark:
            count += 1
            i += 1
        i = 1
        while col+i < 7 and self.grid[row][col+i] == mark:
            count += 1
            i += 1

        if count == 3:
            return True
        else:
            return False

    def check_diagonal(self,mark,row,col):
        count = 0
        for i in range(1,4):
            if (col-i > -1 and row+i < 6 and self.grid[row+i][col-i] == mark):
                count += 1
            if (col+i < 7 and row-i > -1 and self.grid[row-i][col+i] == mark):
                count += 1
        if count == 3:
            return True
        else:
            return False
