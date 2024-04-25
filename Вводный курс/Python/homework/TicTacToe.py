print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
board = list(range(1, 10))

#Функция, которая выводит игровое поле
def draw_board(board):
    print(13 * "-")
    for _ in range(3):
        print("|", board[0 + _ * 3], "|", board[1 + _ * 3], "|", board[2 + _ * 3], "|")
        print(13 * "-")

#Функция, которая принимает и проверят корректность ввода значения для определения позиции
def take_input(player_token, position):
    while True:
        value = input(f"Игрок {position}, выберите позицию для {player_token}:")
        if not (value in "123456789"): #Проверяем, входит ли введеное число пользователем в диапазон от 1 до 9
            print("Некорректный ввод. Введите число от 1 до 9.")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO": #Проверяем, занята ли клетка
            print("Эта клетка уже занята.")
            continue
        board[value - 1] = player_token #Записываем символ в список на указанную позицию по индексу
        break

#Функция, которая проверяет игровое поле на наличие выигрышной комбинации
def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

#Главная функция, определяющая логику игры
def main(board):
    counter = 0
    while True:
        draw_board(board)
        if counter % 2 == 0: #Чётный ход - "Х"
           take_input("X", 1)
        else:
           take_input("O", 2) #Нечётный ход - "О"
        if counter > 3: #Проверяем после 3 хода наличие выигрышной комбинации
           tmp = check_win(board)
           if tmp:
              draw_board(board)
              print(tmp, "выиграл!")
              break
        counter += 1
        if counter > 8: #Выигрышной комбинации нет после 9 хода нет
            draw_board(board)
            print("Ничья!")
            break

main(board)

input("Нажмите Enter для выхода!")