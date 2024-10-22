def convert_temperature(temp, from_scale, to_scale):
  if from_scale == "Цельсий" and to_scale == "Фаренгейт":
    return temp * 1.8 + 32
  if from_scale == "Фаренгейт" and to_scale == "Цельсий":
    return (temp - 32) / 1.8
  else:
    return "Error!"
print(convert_temperature(int(input()), input(), input()))
