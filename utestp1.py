from unittest import TestCase
from Project1 import MazeRunner


class TestMazeSolver(TestCase):

    def test_solve(self):
        maze = [
            [' ', 'V', ' ', ' ', ' '],
            [' ', 'V', ' ', 'V', ' '],
            ['S', ' ', ' ', ' ', ' '],
            [' ', 'V', ' ', 'V', ' '],
            [' ', 'V', ' ', ' ', 'E'],
        ]
        expected_shorted_path = 6
        mazeSolver = MazeRunner(maze)
        mazeSolver.solve_maze()
        actual_shorted_path = mazeSolver.shortest_path()
        self.assertEqual(expected_shorted_path, actual_shorted_path)

    def test_solve_opposite_maze(self):

        maze = [
            ['E', 'W', ' ', ' ', 'S'],
            [' ', 'W', ' ', 'W', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', ' '],
            [' ', 'W', ' ', ' ', ' '],
        ]
        expected_shorted_path = 8
        mazeSolver = MazeRunner(maze)
        mazeSolver.solve_maze()
        actual_shorted_path = mazeSolver.shortest_path()
        self.assertEqual(expected_shorted_path, actual_shorted_path)

    def test_solve_rectangle(self):

        maze = [
            ['S', 'W', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'W', ' ', 'W', 'E', ' '],
            [' ', 'W', ' ', ' ', ' ', ' '],
        ]
        expected_shorted_path = 7
        mazeSolver = MazeRunner(maze)
        mazeSolver.solve_maze()
        actual_shorted_path = mazeSolver.shortest_path()
        self.assertEqual(expected_shorted_path, actual_shorted_path)


    def test_solve_no_walls(self):

        maze = [
            ['S', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'E'],
        ]
        expected_shorted_path = 8
        mazeSolver = MazeRunner(maze)
        mazeSolver.solve_maze()
        actual_shorted_path = mazeSolver.shortest_path()
        self.assertEqual(expected_shorted_path, actual_shorted_path)