# Name: Justine M Ativo
#Section: BAET 2102

#actvity4_pin


correct_pin = "1234"
tries = 0
max_tries = 3
access_granted = False

while tries < max_tries:
    pin = input("PIN: ")
    if pin == correct_pin:
        access_granted = True
        break
    else:
        print("Access denied")
    tries += 1

if access_granted:
    print("Access granted")
else:
    print("Card blocked")

