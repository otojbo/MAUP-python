# Тимофей обычно спит ночью X часов и устраивает себе днем тихий час
# на Y минут. Определите, сколько всего минут Тимофей спит в сутки.

# Внимание, программа принимает значения X и Y из стандартного потока ввода
# (функция input), результат надо выводить в стандартный поток вывода
# (функция print).

X = int(input("How many hours did he sleep at night?: "))
Y = int(input("How many hours did he sleep a day?: "))

print (X*60 + Y)