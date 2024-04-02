#Lab Exam 1
game_lib = {"Donkey kong" : {"Quantity" : 3 , "Cost" : 2},
            "Super Mario" : {"Quantity" : 5, "Cost" : 3},
            "Tetris" : {"Quantity" : 2, "Cost" : 1}}


user_account = {}

admin_username = "admin"
admin_pass = "adminpass"


def available_games():
    print(f"Available Games{game_lib}")

def sign_up():
    while True:
        try:
            username = input("Enter username: ")
            balance = 0
            points = 0
            if not username:
                main_menu()
            if username in user_account:
                print("Username already exist")
                continue
            while True:
                try:        
                    password = input("Enter password: ")
                    if len(password) < 8:
                        print("Password mustr at least 8 characters")
                    if len(password) >= 8:
                        user_account[username] = {"password" : password, "balance" : balance, "points" : points}
                        print("Register successful")
                        main_menu()
                    else:
                        print("Invalid password")                 
                        continue          
                except ValueError as e:
                    print(e)
                    sign_up()
        except ValueError as e:
            print(e)
            sign_up()
            
def log_in():
    print("Sign in")
    while True:
        try:
            username = input("Enter username: ")
            if not username:
                main_menu()
            password = input("Enter password: ")
            if user_account.get(username) and user_account[username]['password'] == password:
                print("Log in Successful")
                rental_main(username)
                

            else:
                print("Invalid Username or Password")
        except ValueError as e:
            print(e)
            main_menu()

def admin_login():
    print("Admin Login")
    username = input("Enter admin username: ")
    if not username:
        main_menu()
    if username == admin_username:
        password = input("Enter admin password: ")
        if password == "adminpass":
           print("Log in successfull")
    else:
        print("Invalid admin username or password")


def exit():
    print("Exiting")







def main_menu():
    print("Main menu")
    print("1. Display available games")
    print("2. Register")
    print("3. Log in")
    print("4. Admin Login")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
       available_games()
       main_menu()
    elif choice == 2:
        sign_up()
    elif choice == 3:  
        log_in()
    elif choice == 4:
        admin_login()
    elif choice == 5:
        exit()
    else:
        print("Invalid input")



def rental_main(username):
    print(f"You are {username}")
    print("1. Rent a game")
    print("2. Return a game")
    print("3. Top up")
    print("4. Display Inventory")
    print("5. Redeem Free Game Rental")
    print("6. Check Points")
    print("7. Log out")

    choice = int(input("Enter your choice: "))

    while True:               
        if choice == 1:
           rent_game(username)
        elif choice == 2:
           return_game(username)
        elif choice == 3:
           top_up(username)
        elif choice == 4:
           display_inventory(username)
        elif choice == 5:
           redeem(username)
        elif choice == 6:
           check_points(username)
        elif choice == 7:
           log_out(username)
        break 

def rent_game(username):
    print("Rent a game")
    print(game_lib)

    gamename = input("Select Game: ")
    if not gamename:
        rental_main(username)
    if game_lib[gamename]['Quantity'] <= 0:
        print ("Not available")
    if game_lib[gamename]['Quantity'] >= 0:
        print("1. Pay using Balance")
        print("2. Pay using Points")
        pay = int(input("Choose how to pay: "))

        if pay == 1:
            if user_account[username]['balance'] <= 0:
                print("Not enough balance to rent.")
            else:
                user_account[username]['balance'] -= game_lib[gamename]['Cost']
                if game_lib[gamename]['Cost'] >= 2:
                    user_account[username]['points'] +=1
                    print(f"Rented Succesfully. User Balance: {user_account[username]['balance']}), Points: {user_account[username]['points']} ")
        if pay == 2:
            if user_account[username]['points'] <= 0:
                print("Not enough balance to rent.")
                rental_main(username)
            else:
                user_account[username]['points'] -= game_lib[username]['Cost']
        else:
            print("Invalid Input")

def return_game(username):
    print("Return Game")
    game_to_return = input ("Enter name of the game you want to return: ")
    quantity_of_game = input("Enter quantity of game to return")
    game_lib[game_to_return]['Quantity'] += quantity_of_game


def top_up(username):
    print("Top Up")
    print(f"Username: {username}, Current Balance: {user_account [username]['balance']}")

    topup_amt = float(input("Enter amount to top up: "))
    user_account[username]['balance'] += topup_amt
    print("Top Up succesfully")
    print(f"Username: {username}, New Balance: {user_account[username]['balance']}")
    rental_main(username)


def display_inventory(username):
    pass

def redeem(username):
    pass

def check_points(username):
    pass

def log_out(username):
    pass




main_menu()







