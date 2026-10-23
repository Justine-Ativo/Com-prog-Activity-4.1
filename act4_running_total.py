# Name: Justine M Ativo
# Section: BAET 2102

#act4_running_total

items = 0
total = 0.0

price = float(input("Price (0 to stop): "))
while price != 0:
    items += 1
    total += price
    price = float(input("Price (0 to stop): "))

if items > 0:
    average = total / items
    print(f"Items: {items} Total: {total:.2f}")
    print(f"Average: {average:.2f}")
else:
    print("Items: 0 Total: 0.00")
    print("Average: 0.00")
