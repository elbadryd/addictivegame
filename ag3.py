import numpy as np
f = open("level3/level3-0.in", "r").read()
#variables
file = f.strip().split(' ')
no_rows = int(file[0])
no_cols = int(file[1])
no_points = int(file[2])
color = int(file[no_points*2 + 4])
slicer = slice(3, no_points*2 + 3)
points = file[slicer]
#matrix of all points and colors
points_matrix = np.array(points).reshape((no_points, 2))
def filter_points():
    filtered = []
    for x in points_matrix:
        if int(x[1]) != color:
            filtered.append(x[0])
    return np.array(filtered)
#points that are not part of path
foreign_points = filter_points()
def is_number(string):
    try: 
        int(string)
        return False
    except:
        return True
directions = list(filter(lambda x: is_number(x), file))
#numbers to create matrix
nums = list(range(1, no_rows*no_cols + 1))

matrix = np.array(nums).reshape((no_rows, no_cols))
#takes number on matrix to find coordinate on grid
def find_coord(number):
    return list(np.argwhere(matrix == number)[0])
#replaces points on matrix that are occupied by foreign points with zeroes
for x in np.nditer(matrix, op_flags=['readwrite']):
    for i in foreign_points:
        if int(x) == int(i):
            x[...] = 0
#predict next step TODO check if next step is valid on grid
def find_next(prev_position, direction):
    step_count = 0
    if direction == 'N':
        return prev_position - no_cols
    if direction == 'S':
        return prev_position + no_cols
    if direction == 'E':
        return prev_position + 1
    if direction == 'W':
        return prev_position - 1 
# def find_path():
#     for i in directions:
#         find_coord

