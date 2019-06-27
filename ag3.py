import numpy as np
import collections
f = open("level3/level3-7.in", "r").read()
#variables
file = f.strip().split(' ')
no_rows = int(file[0])
no_cols = int(file[1])
no_points = int(file[2])
color = int(file[no_points*2 + 4])
start_pos = int(file[no_points*2 + 5])
slicer = slice(3, no_points*2 + 3)
points = file[3:no_points*2 +3]
points = list(map(lambda x: int(x), points))
#matrix of all points and colors
points_matrix = np.array(points).reshape((no_points, 2))
def filter_points():
    filtered = []
    for x in points_matrix:
        if x[1] != color:
            filtered.append(x[0])
    return list(filtered)
def end_pos():
    filtered = []
    for x in points_matrix:
        if x[1] == color:
            filtered.append(x)
    return list(filter(lambda x: int(x[0]) != start_pos, filtered))[0][0]
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
    indexed_coords =  list(np.argwhere(matrix == number)[0])
    return [indexed_coords[0] + 1, indexed_coords[1] + 1]
#predict next step TODO check if next step is valid on grid
def is_overlapping(position):
    for i in foreign_points:
        if position == i:
            return True
    return False
def is_crossing(point):
    try:
        return foreign_points.index(point)
    except:
        return -1

def find_next(prev_position, direction):
    step_count = 0
    if direction == 'N' and find_coord(prev_position)[0] != 1:
        return prev_position - no_cols
    if direction == 'S' and find_coord(prev_position)[0] < no_rows:
        return prev_position + no_cols
    if direction == 'E' and find_coord(prev_position)[1] < no_cols:
        return prev_position + 1
    if direction == 'W' and find_coord(prev_position)[1] != 1:
        return prev_position - 1 
    return False
def has_dupes(path):
    if len(set(path)) == len(path):
        return False
    return duplicates(path)
def duplicates(path):
    dups = collections.defaultdict(list)
    for i, e in enumerate(path):
        dups[e].append(i)
    for k, v in dups.items():
        if len(v) >= 2:
            return v[1]

def find_path(directions, point = start_pos, path = [start_pos]):
    if len(directions) == 0:
        if point != end_pos():
            return f'-1 {len(path) - 1}'
        return f'1 {len(path) - 1}'
    if find_next(point, directions[0]) == False:
        return f'-1 {len(path)}'
    path.append(find_next(point, directions[0]))
    if has_dupes(path):
        return f'-1 {has_dupes(path)}'
    if is_crossing(point) != -1:
        return f'-1 {path.index(point)}'
    return find_path(directions[1:], find_next(point, directions[0]), path)
print(find_path(directions))

