import time
import random
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        if seed:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i, j)
                
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        pos_x1 = (i * self.cell_size_x) + self.x1
        pos_y1 = (j * self.cell_size_y) + self.y1
        pos_x2 = pos_x1 + self.cell_size_x
        pos_y2 = pos_y1 + self.cell_size_y

        self._cells[i][j].draw(pos_x1, pos_y1, pos_x2, pos_y2)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols -1,self.num_rows -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # right
            if i+1 < self.num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            # bottom
            if j+1 < self.num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            # left
            if i-1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
            # top
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))

            # If no directions to go, draw the cell and return
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            # Choose a random direction
            rand_i, rand_j = to_visit[random.randrange(len(to_visit))]

            if rand_i == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            elif rand_i == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            elif rand_j == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            elif rand_j == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            
            # Recursive call to explore from the chosen cell
            self._break_walls_r(rand_i,rand_j)
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

        


