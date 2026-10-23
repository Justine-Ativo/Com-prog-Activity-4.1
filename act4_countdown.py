# Name: Justine M Ativo
# Section: BAET 2102

# activity4_countdown

n = int(input("Enter n: "))
while n <= 0:
    n = int(input("Enter n: "))

current = n
while current >= 1:
    print(current, end=" ")
    current -= 1
print("Liftoff!")

