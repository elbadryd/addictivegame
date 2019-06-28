f = open("level4/level4-0.in", "r").read()
from ag3 import is_number
import numpy as np
file = f.split()
no_rows = int(file[0])
no_cols = int(file[1])
no_points = int(file[2])
points = file[3:no_points*2 +3]
points = list(map(lambda x: int(x), points))
no_paths = int(file[no_points*2 +3])
paths = file[no_points*2 +4:]
points = file[3:no_points*2 +3]
points = list(map(lambda x: int(x), points))
points_matrix = np.array(points)
axis = int(no_points/2)
points_matrix = np.reshape(points_matrix, (no_points, 2))
points_matrix = points_matrix[points_matrix[:,1].argsort()]
points_matrix = points_matrix.reshape(axis, 2, 2)
nums = list(range(1, no_rows*no_cols + 1))
matrix = np.array(nums).reshape((no_rows, no_cols))
def filter_points(mtx, color):
    filtered = []
    for col in mtx:
        for x in col:
            if x[1] != color:
                filtered.append(x[0])
    return list(filtered)
def is_overlapping(position, foreign_pts):
    for i in foreign_pts:
        if position == i:
            return True
    return False
# print(filter_points(points_matrix, 1))
def find_next(prev_position, direction):
    if direction == 'N':
        return prev_position - no_cols
    if direction == 'S':
        return prev_position + no_cols
    if direction == 'E':
        return prev_position + 1
    if direction == 'W':
        return prev_position - 1 
def split_paths(paths):
    paths_matrix = []
    count = -1
    while len(paths) >= 0:
        sub_matrix = []
        count += 1
        try: 
            is_number(paths[count+1])
        except:
            paths_matrix.append(paths)
            return paths_matrix
        if is_number(paths[count]) and is_number(paths[count+1]) == False:
            paths_matrix.append(paths[:count+1])
            paths = paths[count+1:]
            count = -1
paths = split_paths(paths)
def get_path_nums(pos, directions, path = []):
    path.append(pos)
    if len(directions) == 0:
        return path
    next_pos = find_next(int(pos), directions[0])
    return get_path_nums(next_pos, directions[1:], path)
def find_coord(number, mtx):
    try:
        return list(np.argwhere(mtx == number)[0])
    except:
        return [0, 0]
def draw_path(mtx, path, color):
#need to determine color to determine if is overlapping
    path = path[1:-1]
    for i in path:
        x = find_coord(int(i), mtx)[0]
        y = find_coord(int(i), mtx)[1]
        if is_overlapping(mtx, filter_points(mtx, color)):
            return mtx
        else:
            mtx[x, y] = 0
    return mtx
#Place all points on Grid
def draw_points(mtx, points):
    for color in points:
        for point in color:
            x = find_coord(point[0], mtx)[0]
            y = find_coord(point[0], mtx)[1]
            mtx[x, y] = 0
    return mtx
print(draw_path(draw_points(matrix, points_matrix), get_path_nums(paths[3][1], paths[3][3:]), 1))

    
def draw_paths(matrix, paths, points_matrix):
    # print(matrix, paths, points_matrix)
    mtx_with_points = draw_points(matrix, points_matrix)
    for i in paths:
        color = i[0]
        mtx_with_points = draw_path(mtx_with_points, get_path_nums(i[1], i[3:]), color)
    return mtx_with_points
# print(draw_paths(matrix, paths, points_matrix))
#TODO determine if path crosses existing points
#TODO determine if path crosses an existing path

