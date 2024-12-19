import random

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
    array = []
    for i in range(length):
        while True:
            value = input(f"Введите элемент {i+1}: ")
            if value == '':
                print("Ошибка: Ввод не может быть пустым. Попробуйте снова.")
            else:
                try:
                    array.append(int(value))
                    break
                except ValueError:
                    print("Ошибка: Введите целое число. Попробуйте снова.")
    return array

def generate_array(length):
    return [random.randint(0, 9) for _ in range(length)]

def get_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                value = input(f"Введите элемент строки {i+1}, столбца {j+1}: ")
                if value == '':
                    print("Ошибка: Ввод не может быть пустым. Попробуйте снова.")
                else:
                    try:
                        row.append(int(value))
                        break
                    except ValueError:
                        print("Ошибка: Введите целое число. Попробуйте снова.")
        matrix.append(row)
    return matrix

def generate_matrix(rows, cols):
    return [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

def choose_input_method(input_type):
    choice = input(f"Желаете ввести {input_type} вручную? (y/n): ")
    if choice.lower() == 'y':
        return True
    elif choice.lower() == 'n':
        return False
    else:
        print("Неверный выбор. Попробуйте снова.")
        return choose_input_method(input_type)

def menu_task1():
    length = int(input("Введите длину массивов: "))
    manual_input = choose_input_method("массивы")
    if manual_input:
        arr1 = get_array(length)
        arr2 = get_array(length)
    else:
        arr1 = generate_array(length)
        arr2 = generate_array(length)
    result = sum_arrays(arr1, arr2)
    print("Результат:", result)

def menu_task2():
    manual_input = choose_input_method("матрицу")
    if manual_input:
        rows = int(input("Введите количество строк матрицы: "))
        cols = int(input("Введите количество столбцов матрицы: "))
        matrix = get_matrix(rows, cols)
    else:
        rows = int(input("Введите количество строк матрицы: "))
        cols = int(input("Введите количество столбцов матрицы: "))
        matrix = generate_matrix(rows, cols)
    direction = input("Повернуть матрицу направо (right) или налево (left): ")
    if direction == 'right':
        result = rotate_matrix_right(matrix)
    elif direction == 'left':
        result = rotate_matrix_left(matrix)
    print("Результат:")
    for row in result:
        print(row)

def menu_task3():
    length = int(input("Введите длину массивов: "))
    manual_input = choose_input_method("массивы")
    if manual_input:
        arr1 = get_array(length)
        arr2 = get_array(length)
    else:
        arr1 = generate_array(length)
        arr2 = generate_array(length)
    operation = input("Сумма (sum) или разность (diff): ")
    result = big_number_operation(arr1, arr2, operation)
    print("Результат:", result)

def main_menu():
    while True:
        print("Задачи:\n1. Сумма чисел из двух массивов\n2. Поворот матрицы\n3. Сумма или разность больших чисел\n4. Завершить работу программы")
        choice = input("Выберите пункт меню: ")
        if choice == '1':
            menu_task1()
        elif choice == '2':
            menu_task2()
        elif choice == '3':
            menu_task3()
        elif choice == '4':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
