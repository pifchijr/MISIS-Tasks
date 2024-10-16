price = int(input())
if price > 1000:
  price*=0.9
if price > 500 and price <= 1000:
  price*=0.95
print(price)
