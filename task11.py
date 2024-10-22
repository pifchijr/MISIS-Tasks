def calculate_average(lst):
  l = len(lst)
  sum = 0
  for i in lst:
    sum += i
  return sum / l
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])
avrg = calculate_average(a)
print(round(avrg, 2))
