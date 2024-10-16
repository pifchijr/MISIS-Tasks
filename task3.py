Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> symbol = input()
... letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
... number = "0123456789"
... for i in symbol:
...   if i in letters:
...     print("Это буква!")
...   elif i in number and i <=9:
...     print("Это цифра!")
...   else:
