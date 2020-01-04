#!/usr/bin/env python3

import mortorary_path_finding as mpf

maze = mpf.create_maze_wall(20,12)

finder = mpf.Finder()
finder.set_board(maze.board)
finder.run()