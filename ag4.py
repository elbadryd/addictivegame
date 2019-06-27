f = open("level4/level4-0.in", "r").read()
from ag3 import is_number
file = f.split()
no_rows = int(file[0])
no_cols = int(file[1])
no_points = int(file[2])
points = file[3:no_points*2 +3]
points = list(map(lambda x: int(x), points))
no_paths = int(file[no_points*2 +3])
paths = file[no_points*2 +4:]
# def split_paths(paths):
#     paths_matrix = []
#     for i,e in enumerate(paths):
#         if (len(paths) == 0):
#             return paths_matrix
#         if is_number(e) and is_number(paths[i+1]) == False:
#             paths_matrix.append(paths[:i+1])
#             paths = paths[:i+1]
#             print(paths, 'paths')
#             print(paths_matrix, 'matrix')
#     # print(paths_matrix)
def split_paths(paths):
    paths_matrix = []
    count = -1
    while len(paths) >= 0:
        sub_matrix = []
        count += 1
        if is_number(paths[count]) and is_number(paths[count+1]) == False:
            paths_matrix.append(paths[:count+1])
            paths = paths[count+1:]
            count = -1
            print(paths_matrix)
    return paths_matrix
print(split_paths(paths))




print(split_paths(paths))

