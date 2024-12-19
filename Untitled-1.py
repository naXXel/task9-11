import random
import threading

def rotate_matrix_right(matrix):
    """
    Поворачивает матрицу на 90 градусов по часовой стрелке.

    :param matrix: Исходная матрица
    :return: Повернутая матрица
    """
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_matrix_left(matrix):
    """
    Поворачивает матрицу на 90 градусов против часовой стрелки.

    :param matrix: Исходная матрица
    :return: Повернутая матрица
    """
    return [list(row) for row in list(zip(*matrix))[::-1]]

def sum_arrays(arr1, arr2):
    """
    Суммирует элементы двух массивов с учетом условий задачи.

    :param arr1: Первый массив
    :param arr2: Второй массив
    :return: Результирующий массив
    """
    arr1.sort(reverse=True)
    arr2.sort()
    result = [a + b if a != b else 0 for a, b in zip(arr1, arr2)]
    result.sort()
    return result

def big_number_operation(arr1, arr2, operation):
    """
    Выполняет операцию суммы или разности больших чисел, представленных массивами цифр.

    :param arr1: Первый массив цифр
    :param arr2: Второй массив цифр
    :param operation: Операция ('sum' или 'diff')
    :return: Результирующий массив цифр
    """
    int_arr1 = int(''.join(map(str, arr1)))
    int_arr2 = int(''.join(map(str, arr2)))
    if operation == 'sum':
        result = int_arr1 + int_arr2
    elif operation == 'diff':
        result = int_arr1 - int_arr2
    return list(map(int, str(result)))

def get_array(length):
    """
    Запрашивает у пользователя ввод массива заданной длины.

    :param length: Длина массива
    :return: Массив, введенный пользователем
    """
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
    """
    Генерирует массив случайных чисел заданной длины.

    :param length: Длина массива
    :return: Сгенерированный массив
    """
    return [random.randint(0, 9) for _ in range(length)]

def get_matrix(rows, cols):
    """
    Запрашивает у пользователя ввод матрицы заданного размера.

    :param rows: Количество строк матрицы
    :param cols: Количество столбцов матрицы
    :return: Матрица, введенная пользователем
    """
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
    """
    Генерирует матрицу случайных чисел заданного размера.

    :param rows: Количество строк матрицы
    :param cols: Количество столбцов матрицы
    :return: Сгенерированная матрица
    """
    return [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]

def choose_input_method(input_type):
    """
    Запрашивает у пользователя выбор метода ввода данных (вручную или случайно).

    :param input_type: Тип ввода ('массив' или 'матрица')
    :return: True, если пользователь выбрал ввод вручную, иначе False
    """
    choice = input(f"Желаете ввести {input_type} вручную? (y/n): ")
    if choice.lower() == 'y':
        return True
    elif choice.lower() == 'n':
        return False
    else:
        print("Неверный выбор. Попробуйте снова.")
        return choose_input_method(input_type)

def menu_task1(length, manual_input):
    """
    Меню для задачи 1: Сумма чисел из двух массивов.

    :param length: Длина массивов
    :param manual_input: True, если пользователь выбрал ввод вручную, иначе False
    """
    if manual_input:
        arr1 = get_array(length)
        arr2 = get_array(length)
    else:
        arr1 = generate_array(length)
        arr2 = generate_array(length)
    result = sum_arrays(arr1, arr2)
    print("Результат:", result)

def menu_task2(manual_input):
    """
    Меню для задачи 2: Поворот матрицы.

    :param manual_input: True, если пользователь выбрал ввод вручную, иначе False
    """
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

def menu_task3(length, manual_input):
    """
    Меню для задачи 3: Сумма или разность больших чисел.

    :param length: Длина массивов
    :param manual_input: True, если пользователь выбрал ввод вручную, иначе False
    """
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
    """
    Главное меню программы.
    """
    while True:
        print("Задачи:\n1. Сумма чисел из двух массивов\n2. Поворот матрицы\n3. Сумма или разность больших чисел\n4. Завершить работу программы")
        choice = input("Выберите пункт меню: ")
        if choice == '1':
            length = int(input("Введите длину массивов: "))
            manual_input = choose_input_method("массивы")
            thread = threading.Thread(target=menu_task1, args=(length, manual_input))
            thread.start()
            thread.join()
        elif choice == '2':
            manual_input = choose_input_method("матрицу")
            thread = threading.Thread(target=menu_task2, args=(manual_input,))
            thread.start()
            thread.join()
        elif choice == '3':
            length = int(input("Введите длину массивов: "))
            manual_input = choose_input_method("массивы")
            thread = threading.Thread(target=menu_task3, args=(length, manual_input))
            thread.start()
            thread.join()
        elif choice == '4':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
