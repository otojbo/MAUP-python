# Напишите программу, которая получает на вход три целых числа, по одному
# числу в строке, и выводит на консоль в три строки сначала максимальное,
# потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.

a = int(input("Write first number: "))
b = int(input("Write first second: "))
c = int(input("Write first third: "))

if a>b and a>c:
  max = a
  if b>c:
    mid=b
    min=c
  else:
    mid=c
    min=b
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")
elif b>a and b>c:
  max=b
  if a>c:
    mid=a
    min=c
  else:
    mid=c
    min=a
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")
elif c>a and c>b:
  max=c
  if a>b:
    mid=a
    min=b
  else:
    mid=b
    min=a
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")
elif c==a and b==c:
  max=a
  min=b
  mid=c
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")
elif c==a and (b>a or b>c):
  max=b
  min=c
  mid=a
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")
elif c==a and (b<a or b<c):
  max=a
  min=b
  mid=c
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")
elif a==b and (c<b or c<a):
  max=a
  min=c
  mid=b
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")
elif a==b and (c>b or c>a):
  max=a
  min=b
  mid=c
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")
elif c==b and (a>c or a>b):
  max=a
  min=c
  mid=b
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")
elif c==b and (a<c or a<b):
  max=c
  min=a
  mid=b
  print(f"Max number: {max}")
  print(f"Min number: {min}")
  print(f"Remaining number: {mid}")