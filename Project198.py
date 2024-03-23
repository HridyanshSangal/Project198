items = []
prices = []
quantities = []
total_cost = 0

while True:
  item = input("Enter item name (or 'done' to finish): ")
  if item == 'done':
    break
  items.append(item)
  price = float(input("Enter price of {}: ".format(item)))
  prices.append(price)
  quantity = int(input("Enter quantity of {}: ".format(item)))
  quantities.append(quantity)
total_cost += price * quantity

# Print the bill
print("Bill:")
for i in range(len(items)):
  print(f'Price of your items is: {price}')
print(f"Total cost: {total_cost}")