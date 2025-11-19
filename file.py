print("Welcome to the School Portal Login System!")
email = input("enter your email: ")



def signup(email):
    if "@" not in email:
        print("Error. Email must contain @ symbol.")
        return "invalid email"
    print("yay u!👍 good email")

    password = input("Enter your password: ")
    upper = False
    if password.__len__() < 8:
        print("Error. Password Needs to be at least 8 characters long.")
        return "invalid password"
    for char in password:
        if char == char.upper():
            upper = True
        
            


    
signup(email)