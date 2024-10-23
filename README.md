# Отчёт об игре 
1. Название игры - Maxit
2. Студент - Антонов Артём Андреевич, ТРПО24-2
3. Задание: 
Реализовать программу , при помощи которой 2 игрока могут играть в игру «Максит». Правила игры следующие. В клетках квадрата 3 на 3 пишутся случайные числа из диапазона от 1 до 9. Начинающий выбирает любое понравившееся ему число и вычеркивает его, прибавляя к своей сумме. Второй игрок может выбрать любое из оставшихся чисел того столбца, в котором первый игрок делал свой предыдущий ход. Он тоже вычеркивает выбранное число, прибавляя его к своей сумме. Первый игрок далее поступает аналогично, выбирая число-кандидата из той строки, в которой второй игрок ходил перед этим. Может так случиться, что у какого-то игрока не будет хода. Тогда его соперник продолжает игру, делая ход в той же строке (для первого игрока) или в том же столбце (для второго игрока), что и до этого. Игра заканчивается, когда оба играющих не имеют ходов. Результат определяется по набранным суммам, у кого она больше, тот и выиграл. При равенстве сумм фиксируется ничья. (описание правил игры: https://www.iqfun.ru/articles/maxit.shtml ).
Взаимодействие с программой производится через консоль. Игровое поле изображается в виде 3 текстовых строк и перерисовывается при каждом изменении состояния поля. При запросе данных от пользователя программа сообщает, что ожидает от пользователя (например, координаты очередного хода) и проверяет корректность ввода. Программа должна уметь автоматически определять сумму очков каждого из игроков и окончание партии и ее победителя.
Сама программа НЕ ходит, т.е. не пытается вычеркивать числа с целью выиграть игру

5. Работа программы

   
![image](https://github.com/user-attachments/assets/248f4a6c-dec5-4807-a91f-7b527ed206ba)



![image](https://github.com/user-attachments/assets/21d241ec-f55d-430d-a6e1-4dbe15bf257e)
![image](https://github.com/user-attachments/assets/8a83d187-fdf0-4694-bfeb-49c42537aa5d)


