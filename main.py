# Ввод и проверка ввода
try:
    num = int(input("Введите число строк от 12 до 62: "))
    if num < 12 or num > 62:
        raise ValueError
except ValueError:
    input("Вы ввели неправильное значение")
    exit()


#Получаем высоту
lenght = num * 2

#Получаем кол-во пробелов в верхней и нижней части
tube = lenght // 6
if tube % 2 == 1:
    lenght += 1

# Получаем кол-ва двоеточий и пробелов (для внутреннего квадрата)
filler = (lenght - 2 - tube) // 2
num_two_dots = tube - 1
num_spaces = lenght - num_two_dots * 2 - 4

#Получаем высоту "трубы" - кол-во строк с пробелами на внутренним квадратом
tube_h = num // 9
#Получаем высоту внутрннего квадрата
height_sq = num - 2 * tube_h - 4

#Вывод на экран

print('[' * ((lenght - tube) // 2) + " " * tube + ']' * ((lenght - tube) // 2))

[print('[' + ':' * filler + ' ' * tube + ':' * filler + ']') for i in range(tube_h)]

lid = '[' + ':' * num_two_dots + ':' + '[' * (filler - 2 - num_two_dots) + ':'
lid += ' ' * tube + ':' + ']' * (filler - 2 - num_two_dots) + ':' * num_two_dots + ':' + ']'

print(lid)

main_string = "[" + ":" * num_two_dots + "[" + " " * num_spaces + "]" + ":" * num_two_dots + "]"


for i in range(height_sq):
    string = main_string
    text = ''
    # Вывод текста по середине квадрата
    if i + 1 == height_sq // 2 and num_spaces >= 22:
        text = "CODE THE WORLD"
    elif i + 1 == height_sq // 2 + 1 and num_spaces >= 22:
        text = "www.itmathrepetitor.ru"
    spaces = (num_spaces - len(text)) // 2
    add = (num_spaces - len(text)) % 2
    text = text.ljust(num_spaces - spaces - add, " ")
    text = text.rjust(num_spaces, " ")

    string = string.split(" ")[0] + text + string.split(" ")[-1]
    print(string)

print(lid)

[print('[' + ':' * filler + ' ' * tube + ':' * filler + ']') for i in range(tube_h)]

print('[' * ((lenght - tube) // 2) + " " * tube + ']' * ((lenght - tube) // 2))

input()