from graphics import Window
from maze import Maze

def main():
    win = Window(800,600)
    # win.draw_line(Line(Point(50,50), Point(400,400)), "red")
    # win.draw_line(Line(Point(50,400), Point(400,50)), "blue")
    # win.draw_line(Line(Point(200,100), Point(200,500)), "green")
    # c = Cell(win)
    # c.has_left_wall = False
    # c.draw(50, 50, 100, 100)

    # d = Cell(win)
    # d.has_right_wall = False
    # d.draw(125, 125, 200, 200)

    # d.draw_move(c)

    m = Maze(0,0,10,10,80,60,win)

    win.wait_for_close()
    
    

main()