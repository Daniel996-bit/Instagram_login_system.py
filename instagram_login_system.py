attempts = 0
access_granted = False
account_blocked = False
while attempts <3:
    attempts += 1
    print("¶•¶•¶•¶•¶•¶•¶•¶•¶•¶ INSTAGRAM LOGIN SYSTEM ¶•¶•¶•¶•¶•¶•¶•¶•¶•¶")
    print(f"Attempt number {attempts}")
    email = input("Enter your email ")
    username = input("Enter your username ")
    phone_number = int(input("Enter your phone number "))
    password = input("Enter your password ")
    if email != "danielt@gmail.com" or (username != "t.d.06" or phone_number != 996703334353):
        print("Entered incorrect data!")
    else:
        print("Entered correct data!")
        if password != "Dan.996":
            print("Incorrect password!")
        else:
            print("Correct password!")
            access_granted = True
            break
if not access_granted:
    account_blocked = True
    print("The limit for attempts has been reached. Access denied!!")
else:
    print("Access granted!")
if account_blocked:
    print("Your account is blocked!")
else:
    print("Your account is not blocked!")
print("¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶•¶")