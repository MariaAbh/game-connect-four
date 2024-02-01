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
        return self.check_vertical(mark,row,col) or self.check_horizontal(mark,row,col) or self.check_diagonal_first(mark,row,col) or self.check_diagonal_second(mark,row,col)

    def check_alignement(self,mark,row,col,r,c):
        count = 0
        r_index = r
        c_index = c
        while row-r_index > -1 and col-c_index > -1 and row-r_index < 6 and self.grid[row-r_index][col-c_index] == mark:
            count += 1
            r_index += (1 if r_index > 0 else -1 if r_index < 0 else 0)
            c_index += (1 if c_index > 0 else -1 if c_index < 0 else 0)

        r_index = r
        c_index = c
        while row+r_index < 6 and col+c_index < 7 and row+r_index > -1 and self.grid[row+r_index][col+c_index] == mark:
            count += 1
            r_index += (1 if r_index > 0 else -1 if r_index < 0 else 0)
            c_index += (1 if c_index > 0 else -1 if c_index < 0 else 0)
        return count == 3

    def check_vertical(self,mark,row,col):
        return self.check_alignement(mark,row,col,1,0)

    def check_horizontal(self,mark,row,col):
        return self.check_alignement(mark,row,col,0,1)

    def check_diagonal_first(self,mark,row,col):
        return self.check_alignement(mark,row,col,-1,1)

    def check_diagonal_second(self,mark,row,col):
        return self.check_alignement(mark,row,col,1,1)
