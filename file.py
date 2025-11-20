print("Welcome to the School Portal Login System!")
email = input("enter your email: ")
users = [{"email": ,"password":}]
def signup(email):
    if "@" not in email:
        print("Error. Email must contain @ symbol.")
        return "invalid email"
    print("yay u!👍 good email")
    password = input("Enter your password: ")
    upper = 0
    num = 0
    if password.__len__() < 8:
        print("Error. Password Needs to be at least 8 characters long.")
        return "invalid password"
    for char in password:
        if char.isupper():
            upper =+ 1
    for char in password:
        if char.isdigit():
            num =+ 1
    if upper <1 :
        print("Password needs to have at least 1 uppercase letter")
        return "invalid password"
    if num <1:
        print("Password needs to have at least 1 number")
        return "invalid password"
    print("yay u! Good password :D")
    users.append(email)
signup(email)
print(users)