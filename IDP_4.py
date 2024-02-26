grid = []

def get_adj_col(row, col):
  if grid[row][col] == 1:
    return col + 1
  return col - 1

def read_grid(no_rows, no_col):
  for i in range(no_rows):
    row = list(map(int, input().split()))
    grid.append(row)

def get_exit_position(entry_col):
  current_row = 0
  current_col = entry_col
  while current_row < no_rows:
    next_row, next_col = get_next_position(current_row, current_col)
    if next_row == current_row:
      return -1
    current_row, current_col = next_row, next_col
  return next_col
def get_next_position(current_row, current_col):
  adj_col = get_adj_col(current_row, current_col)
  if adj_col < no_col and adj_col >= 0:
    if grid[current_row][current_col] == grid[current_row][adj_col]:
      return current_row +1, adj_col
  return current_row, current_col

def main():
  global grid, no_rows, no_col
  no_rows, no_col = map(int, input().split())
  read_grid(no_rows, no_col)
  exit_positions_list = [] 
  for col in range(no_col):
    exit_position = get_exit_position(col)
    exit_positions_list.append(exit_position)
  print(exit_positions_list)

main()
