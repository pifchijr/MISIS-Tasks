symbol = input()
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
for i in symbol:
  if i in letters:
    print("Это буква!")
  elif i in number and i <=9:
    print("Это цифра!")
  else:
    print("Это не цифра и не буква!")
