def check_password(password):
  if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
    return True
  else:
    return False
print(check_password(input()))
