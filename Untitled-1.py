def rotate_matrix_right(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_matrix_left(matrix):
    return [list(row) for row in list(zip(*matrix))[::-1]]

def sum_arrays(arr1, arr2):
    arr1.sort(reverse=True)
    arr2.sort()
    result = [a + b if a != b else 0 for a, b in zip(arr1, arr2)]
    result.sort()
    return result

def big_number_operation(arr1, arr2, operation):
    int_arr1 = int(''.join(map(str, arr1)))
    int_arr2 = int(''.join(map(str, arr2)))
    if operation == 'sum':
        result = int_arr1 + int_arr2
    elif operation == 'diff':
        result = int_arr1 - int_arr2
    return list(map(int, str(result)))

def get_array(length):
    return [int(input(f"Введите элемент {i+1}: ")) for i in range(length)]

def generate_array(length):
    return [random.randint(0, 9) for _ in range(length)]

def get_matrix(rows, cols):
    return [[int(input(f"Введите элемент [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

def generate_matrix(rows, cols):
    return [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]