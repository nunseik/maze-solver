from graphics import Window
from maze import Maze

def main():
    win = Window(900,700)

    m = Maze(50,50,10,10,80,60,win,10)
    m.solve()

    win.wait_for_close()
    
    

main()