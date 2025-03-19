import time
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
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i, j)
                print(self._cells)

    def _draw_cell(self, i, j):
        pos_x1 = ((j + 1) * self.cell_size_x) + self.x1
        pos_y1 = ((i + 1) * self.cell_size_y) + self.y1
        pos_x2 = pos_x1 - self.cell_size_x
        pos_y2 = pos_y1 - self.cell_size_y

        self._cells[i][j].draw(pos_x1, pos_y1, pos_x2, pos_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)