# Name: Nabulay, Gabriel Seth B.
# Grade and Section: 8-Adelfa

while True:
    pin = input("Create a six-digit PIN: ") # Inputs the PIN's value

    if pin.isdigit() and len(pin) == 6: # Checks if user's PIN is a digit and the length of the pin is six digits
        print("Valid PIN.") # Outputs this message if PIN is valid
        break
    else:
        print("Invalid PIN. Enter exactly 6 digits.") # Outputs this message if PIN is invalid and makes user re-input
