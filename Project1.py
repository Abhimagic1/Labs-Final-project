import copy
class MazeRunner:

    def __init__(self, maze):
        self._maze = copy.deepcopy(maze)
        self._solution_step_counts = []
        self._current_row, self._origin_column = self.starting_point()
        self._current_steps = 0
        self._shortest_path = 1000



    def starting_point(self):
        for row_index in range(len(self._maze)):
            for column_index in range(len(self._maze[row_index])):
                if self._maze[row_index][column_index] == 'S':
                    return row_index, column_index
        raise ValueError('There is no place to start!')

    def _can_move(self, row_index, column_index):
        return 0 <= row_index < len(self._maze) and \
            0 <= column_index < len(self._maze[row_index]) and \
                (self._maze[row_index][column_index] == ' ' or
                    self._maze[row_index][column_index] == 'E')


    def solve_maze(self):

        if self._maze[self._current_row][self._origin_column] == 'E':
            self._solution_step_counts.append(self._current_steps)

            if self._current_steps < self._shortest_path:
                self._shortest_path = self._current_steps

        else:
            self._maze[self._current_row][self._origin_column] = 'v'
            self._current_steps += 1
            if self._can_move(self._current_row - 1, self._origin_column):
                    self._current_row -= 1
                    self.solve_maze()
                    self._current_row += 1

            if self._can_move(self._current_row + 1, self._origin_column):
                    self._current_row += 1
                    self.solve_maze()
                    self._current_row -= 1

            if self._can_move(self._current_row, self._origin_column - 1):
                    self._origin_column -= 1
                    self.solve_maze()
                    self._origin_column += 1

            if self._can_move(self._current_row, self._origin_column + 1):
                    self._origin_column += 1
                    self.solve_maze()
                    self._origin_column -= 1
            self._maze[self._current_row][self._origin_column] = ' '
            self._current_steps -= 1

    def shortest_path(self):
        return min(self._solution_step_counts)

    def longest_path(self):
        return max(self._solution_step_counts)

    def __str__(self):
        return '\n'.join(str(row) for row in self._maze)

maze = [
    [' ', 'V', ' ', ' ', 'E'],
    [' ', 'V', 'V', 'V', ' '],
    ['S', ' ', ' ', 'V', ' '],
    [' ', 'V', ' ', ' ', ' '],
    [' ', 'V', ' ', 'V', ' '],
]

maze2 = [
    ['S', 'V', ' ', ' ', 'E'],
    [' ', 'V', 'V', 'V', ' '],
    [' ', ' ', ' ', 'V', ' '],
    [' ', 'V', ' ', ' ', ' '],
    [' ', 'V', ' ', 'V', ' '],
]
maze_solver = MazeRunner(maze)
maze_solver.solve_maze()
maze_solver2 = MazeRunner(maze2)
maze_solver2.solve_maze()
print('smallest amount of moves is', maze_solver.shortest_path())
print('largest amount of moves is', maze_solver.longest_path())
print('smallest amount of moves is', maze_solver2.shortest_path())
print('largest amount of moves is', maze_solver2.longest_path())


