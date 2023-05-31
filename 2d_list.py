# 2d list: Lists inside a list.
num_grid = [
    [1,3],[2,4],[5,7]
]

# print(num_grid[0][1])

for row in num_grid:
    for col in row:
        print(col)