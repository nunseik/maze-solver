from graphics import Window, Line, Point, Cell

def main():
    win = Window(800,600)
    # win.draw_line(Line(Point(50,50), Point(400,400)), "red")
    # win.draw_line(Line(Point(50,400), Point(400,50)), "blue")
    # win.draw_line(Line(Point(200,100), Point(200,500)), "green")
    cell = Cell(50, 200, 50, 200, win)
    cell.draw()
    win.wait_for_close()
    
    

main()