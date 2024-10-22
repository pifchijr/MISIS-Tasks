text = input()
vowels = "аеёиоуыэюя"
count = 0
for letter in text.lower():
    if letter in vowels:
        count += 1
print(count)
