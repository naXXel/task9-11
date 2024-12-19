def rotate_matrix_right(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]