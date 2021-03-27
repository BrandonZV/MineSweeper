#https://www.geeksforgeeks.org/backtracking-algorithms/
#https://www.geeksforgeeks.org/category/algorithm/backtracking/
#https://www.geeksforgeeks.org/minesweeper-solver/

import random

dxy = [-1, 0, 1]
dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

def is_index_edge(x, y, field):
  pass


# Build the basic grid with m, n dimensions and a density of p 
def build_grid(m, n, p):
  mine_field = [[False for i in range(m)] for j in range(n)]
  hidden_field = [[0 for i in range(m)] for j in range(n)]

  # Fill in field with mines
  for x in range(m):
    for y in range(n):
      if random.randint(0,100) < p:
        mine_field[x][y] = True

  # Fill in field with numbers corresponding to how many mines surround it
  for x in range(m):
    for y in range(n):
      for z in range(9):
        if ()

def display_field():


def ifvalid(n):
  for x in range (3):
    for y in range(3):
      if 0 <= x < n and mine[dxy[x]][dxy[y]]

def main():
  pass

if __name__ == "__main__":
  main()