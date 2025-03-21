# Maze Solver

A Python application that generates and solves random mazes using recursive backtracking algorithms. The program creates a visual representation of the maze and animates the solving process in real-time.

## Features

- Random maze generation using depth-first search with recursive backtracking
- Animated maze creation process
- Visual representation of the maze-solving algorithm
- Distinct wall colors for better visualization (red for left walls, blue for right walls, green for top walls, purple for bottom walls)
- Path tracking with colored lines showing the solution path and backtracking

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/maze-solver.git
cd maze-solver
```

2. Make sure you have Python installed (the project was developed with Python 3.x)

3. No additional dependencies are required beyond the standard library

## Usage

Run the main program:

```bash
python main.py
```

The application will:
1. Open a window displaying the maze generation process
2. Automatically break the entrance (top of first cell) and exit (bottom of last cell)
3. Create a random maze by breaking walls between cells
4. Solve the maze using a depth-first search algorithm
5. Display the solution path in red
6. Show backtracking in gray when the algorithm hits dead ends

## Project Structure

- `main.py` - Entry point that initializes the window and maze
- `maze.py` - Contains the Maze class that handles generation and solving logic
- `cell.py` - Contains the Cell class for individual maze cells and drawing functionality
- `graphics.py` - Provides the graphical interface using Tkinter

## How It Works

### Maze Generation

The maze is generated using a depth-first search with recursive backtracking:

1. Start with a grid where all cells have four walls
2. Begin at the entrance cell (0,0)
3. Randomly choose an unvisited neighboring cell
4. Remove the walls between the current cell and chosen cell
5. Move to the chosen cell and mark it as visited
6. Recursively repeat until all cells are visited

### Maze Solving

The maze is solved using a similar recursive backtracking approach:

1. Start at the entrance (0,0)
2. Try each possible direction (right, bottom, left, top)
3. Move to a neighboring cell only if there is no wall between them and the cell hasn't been visited
4. Draw the path as it explores
5. If a dead end is reached, backtrack and mark the path in gray
6. Continue until the exit is reached or all possibilities are exhausted

## Configuration

The maze dimensions and properties can be adjusted in `main.py`:

```python
m = Maze(50, 50, 10, 10, 80, 60, win, 10)
```

Parameters:
- `x1, y1`: Starting position of the maze in the window (50, 50)
- `num_rows, num_cols`: Number of rows and columns in the maze (10, 10)
- `cell_size_x, cell_size_y`: Size of each cell in pixels (80, 60)
- `win`: Window object for rendering
- `seed`: Random seed for reproducible mazes (10)

## Ideas for Future Improvements

- **Alternative Algorithms**: Implement breadth-first search or A* for comparison
- **Enhanced Visuals**: Customize colors, wall thickness, and cell appearance
- **Animation Controls**: Add options to adjust animation speed (faster for new paths, slower for backtracking)
- **User Interface**: Implement Tkinter buttons and inputs to allow users to change maze size, speed, and other parameters
- **Scalability**: Support for much larger mazes
- **Interactive Mode**: Make it a game where users can navigate the maze
- **Competition Mode**: Allow users to race against the solving algorithm
- **3D Mazes**: Extend the concept to three dimensions
- **Performance Analysis**: Time different solving algorithms to compare efficiency

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## Acknowledgments

- Created as part of the Boot.dev programming curriculum
- Inspired by classic maze generation and solving algorithms
