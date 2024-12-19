def rotate_matrix_right(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_matrix_left(matrix):
    return [list(row) for row in list(zip(*matrix))[::-1]]
