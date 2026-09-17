# Name: Nabulay, Gabriel Seth B.
# Grade and Section: 8-Adelfa

payment_methods = ["gcash", "paypal", "card"] # List of payment methods

while True:
    entered_payment_method = input("Enter payment method: ").lower() # Inputs user's payment method

    if entered_payment_method in payment_methods: # Checks if inputted payment method in the pre-listed payment methods
        print("Valid payment method.")
        break # Ends program if payment method is valid.
    else:
        print("Invalid payment method.") # Outputs this line and maked user enter payment method again.