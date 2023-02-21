matrix = [[2, 3,],
          [5, 7,],
          [0, 1,]]
matrix_transpose = [[0, 0, 0],
                    [0, 0, 0]]
for rows in range(len(matrix)):
    for columns in range(len(matrix[0])):
        matrix_transpose[columns][rows] = matrix[rows][columns]

for items in matrix_transpose:
    print(items)
