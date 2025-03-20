from graphics import *

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        left_color = "white"
        right_color = "white"
        top_color = "white"
        bottom_color = "white"
        if self.has_left_wall:
            left_color = "red"
        self._win.draw_line(Line(Point(self._x1,self._y1), Point(self._x1,self._y2)), left_color)
        
        if self.has_right_wall:
            right_color = "blue"
        self._win.draw_line(Line(Point(self._x2,self._y1), Point(self._x2,self._y2)), right_color)
        
        if self.has_top_wall:
            top_color = "green"
        self._win.draw_line(Line(Point(self._x1,self._y1), Point(self._x2,self._y1)), top_color)
        
        if self.has_bottom_wall:
            bottom_color = "purple"
        self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), bottom_color)

    def draw_move(self, to_cell, undo=False):
        x_center = (self._x1 + self._x2)/2
        y_center = (self._y1 + self._y2)/2
        to_cell_x = (to_cell._x1 + to_cell._x2)/2
        to_cell_y = (to_cell._y1 + to_cell._y2)/2
        
        if undo:
            self._win.draw_line(Line(Point(x_center,y_center), Point(to_cell_x,to_cell_y)), "gray")
        else:
            self._win.draw_line(Line(Point(x_center,y_center), Point(to_cell_x,to_cell_y)), "red")