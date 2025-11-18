print("Welcome to the School Portal Login System!")
email = input("enter your email: ")
password = input("emter your password: ")


def signup(email,password):
    if "@" not in email:
        print("Error. Invalid email.")
        return "invalid email"
    print("yay u!👍 good email")
signup(email,password)