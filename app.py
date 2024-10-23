import random  # Импортируем модуль random для генерации случайных чисел

# Отображение игрового поля
def PrintBoard(board):
    for row in board:
        print(' '.join(str(cell) if cell != 0 else ' ' for cell in row))  # Выводим число или пробел, если оно вычеркнуто

# Проверка доступных чисел в строке
def GetRowNumbers(board, row):
    return [board[row][col] for col in range(3) if board[row][col] != 0]

# Проверка доступных чисел в столбце
def GetColumnNumbers(board, col):
    return [board[row][col] for row in range(3) if board[row][col] != 0]

# Обновление игрового поля (вычеркивание числа)
def UpdateBoard(board, number):
    for i in range(3):
        for j in range(3):
            if board[i][j] == number:  # Если нашли выбранное число
                board[i][j] = 0  # Заменяем его на 0, то есть вычеркиваем
                return (i, j)  # Возвращаем координаты вычеркнутого числа

# Основная функция игры
def main():
    # Создаём поле 3x3 со случайными числами от 1 до 9
    board = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
    # Счёт игроков
    score1 = 0
    score2 = 0

    # Вывод начального игрового поля
    print("Начальное игровое поле:")
    PrintBoard(board)

    # Переменные для хранения последних координат
    LastRow, LastCol = None, None
    CurrentPlayer = 1  # Начинает первый игрок

    # Основной цикл игры
    while True:
        # Определяем доступные ходы для текущего игрока
        if CurrentPlayer == 1:  # Первый игрок выбирает из строки последнего хода второго игрока
            AvailableNumbers = GetRowNumbers(board, LastRow) if LastRow is not None else [cell for row in board for cell in row if cell != 0]
        else:  # Второй игрок выбирает из столбца последнего хода первого игрока
            AvailableNumbers = GetColumnNumbers(board, LastCol) if LastCol is not None else [cell for row in board for cell in row if cell != 0]

        # Проверяем, есть ли доступные ходы
        if not AvailableNumbers:
            print(f"Игрок {CurrentPlayer} не может сделать ход.")
            break  # Завершаем игру, если нет доступных ходов

        # Получаем выбор игрока
        print(f"Игрок {CurrentPlayer}, доступные числа: {AvailableNumbers}")
        choice = int(input("Введите число: "))

        # Проверяем, корректный ли выбор
        if choice not in AvailableNumbers:
            print("Некорректный выбор, попробуйте снова.")
            continue

        # Обновляем игровое поле
        position = UpdateBoard(board, choice)

        # Обновляем счёт
        if CurrentPlayer == 1:
            score1 += choice
        else:
            score2 += choice

        # Переключаем текущего игрока
        CurrentPlayer = 2 if CurrentPlayer == 1 else 1

        # Обновляем последние координаты
        LastRow, LastCol = position

        # Печатаем текущее состояние игрового поля
        PrintBoard(board)
        print(f"Счет: Игрок 1 - {score1}, Игрок 2 - {score2}")

    # Определяем победителя
    if score1 > score2:
        print("Игрок 1 победил!")
    elif score2 > score1:
        print("Игрок 2 победил!")
    else:
        print("Ничья!")

# Запускаем игру
main()
