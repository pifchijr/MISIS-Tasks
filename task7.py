n  = int(input())
simple = "простое"
for i in range(2, n + 1):
    if n % i == 0 and n != i:
        simple = "составное"
        break
print(simple)
