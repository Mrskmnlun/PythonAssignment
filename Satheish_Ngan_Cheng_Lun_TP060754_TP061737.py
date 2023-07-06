# Satheish
# TP060754
# Ngan Cheng Lun
# TP061737

import time
import datetime


def main():
    now = datetime.datetime.now()
    print(now)
    print("-------------------------------------")
    print("-ONLINE FOOD ORDER MANAGEMENT SYSTEM-")
    print("---SPIDERMAN ONLINE FOOD SERVICES----")
    print("-------------------------------------")
    time.sleep(1)
    print("Choose your option: ")
    print("(1)Access to Admin System\n(2)Access to Customer System")
    print("(3)Access to Guest System\n(4)Exit")
    while True:
        num = str(input("Choose your Option: "))
        if num == "1":
            print("------------------------------------- \n"
                  "Directing to Admin Page"
                  "\n-------------------------------------")
            admin_login_signup()
            break
        elif num == "2":
            print("------------------------------------- \n"
                  "Directing to Customer Page"
                  "\n-------------------------------------")
            customerpage()
            break
        elif num == "3":
            print("------------------------------------- \n"
                  "Directing to Guest Page"
                  "\n-------------------------------------")
            guestpage()
            break
        elif num == "4":
            print("------------------------------------- \n"
                  "Exiting................\n"
                  "-------------------------------------")
            exit()
            break
        else:
            print("Invalid Option")


# done
def admin_login_signup():
    print("\n" * 1)
    print("-------------------------------------\n"
          "Welcome to the Admin Page\n"
          "-------------------------------------")
    print("Choose your Option")
    print("(1) Login\n"
          "(2) Sign Up\n"
          "(3) Back to Welcome Page")
    while True:
        num1 = str(input("Choose your Option: "))
        if num1 == "1":
            print("-------------------------------------\n"
                  "Directing to Login Page\n"
                  "-------------------------------------")
            admin_login()
            break
        elif num1 == "2":
            print("-------------------------------------\n"
                  "Directing to Sign Up Page\n"
                  "-------------------------------------")
            admin_signup()
            break
        elif num1 == "3":
            print("-------------------------------------\n"
                  "Directing to Welcome Page\n"
                  "-------------------------------------")
            main()
            break
        else:
            print("Invalid Option")


# Done
def admin_signup():
    detail = True
    while detail:
        print("\n" * 1)
        print("-------------------------------------\n"
              "Would you like to register an admin account?\n"
              "-------------------------------------")
        print("(1) Yes\n(2) NO")
        reg = str(input("Choose your option:"))
        if reg == "1":
            print("Enter a username. (atleat 4 character long)")
            fourchar = False
            while not fourchar:
                username = str(input("Username:")).upper()
                if len(username) >= 4:
                    if len(username) <= 12:
                        fourchar = True
                    else:
                        fourchar = False
                        print("Username Can't Exceed 12 Characters long.")
                else:
                    fourchar = False
                    print("Username must be in between 4 to 12 Character")

                print("-------------------------------------\n"
                      "Password atleast 5 characters\n"
                      "-------------------------------------")
                pass1 = True
                while pass1:
                    password = str(input("Enter a Password:"))
                    if len(password) >= 5:
                        pass1 = False
                    else:
                        print("Password is too short!")
                        pass1 = True

                with open("admin.txt", "a") as AF:
                    AF.write(username + ";" + password + "\n")
                    print("-------------------------------------\n"
                          "Account is registered!!\n"
                          "Pls Login Again\n"
                          "-------------------------------------")
                    AF.close()
                    admin_login()
        elif reg == "2":
            print("User Will be Direct back to Welcome Page")
            print("-------------------------------------")
            main()
            break
        else:
            print("Invalid Input")


# done
def admin_login():
    while True:
        print("-------------------------------------\n"
              "Welcome to Login Page\n"
              "-------------------------------------")
        print("Would You Like too continue?")
        print("(1)Yes\n(2)No")
        ans = str(input("Choose Your Option:"))
        if ans == "1":
            permission = False
            while not permission:
                with open('admin.txt', 'r') as AR:
                    print("Enter admin username and password")
                    adname = str(input("Username:")).upper()
                    adpass = str(input("Password:"))
                    for line in AR:
                        if adname + ";" + adpass == line.strip():
                            permission = True
                            break
                    if permission == True:
                        print("Access Granted!!")
                        print("-------------------------------------")
                        print("Welcome", adname)
                        print("-------------------------------------")
                        admin_page()
                        break
                    else:
                        print("Access Denied!!!")
        elif ans == "2":
            print("User will return to Welcome Page")
            main()
        else:
            print("Invalid Option")


# done
def admin_page():
    while True:
        print("-------------------------------------")
        print("Welcome to Admin Page")
        print("-------------------------------------")
        print("Would you like to continue?")
        print("(1) Yes\n(2) No")
        pick = str(input("Enter a number:"))
        if pick == "1":
            print("-------------------------------------")
            print("(1) Add Food")
            print("(2) Modify Menu")
            print("(3) Display All Record")
            print("(4) Search Specific Record")
            print("(5) Exit")
            while True:
                option = str(input("Choose a Option:"))
                if option == "1":
                    print("-------------------------------------")
                    print("Heading to Add Item Menu")
                    add_menu()
                    break
                elif option == "2":
                    print("-------------------------------------")
                    print("Heading to Modify Menu")
                    admin_modify_menu()
                    break
                elif option == "3":
                    print("-------------------------------------")
                    print("Heading to Display Page")
                    display_record()
                    break
                elif option == "4":
                    print("-------------------------------------")
                    print("Search Specific Record")
                    search_specific_page()
                    break
                elif option == "5":
                    print("-------------------------------------")
                    print("Exiting...")
                    print("-------------------------------------")
                    exit()
                else:
                    print("Invalid Option, Try Again")
        elif pick == "2":
            print("-------------------------------------")
            print("You will be log out!")
            print("-------------------------------------")
            print("Returning to Menu...")
            print("-------------------------------------")
            admin_login()
            break
        else:
            print("Invalid Option, Try Again")


# Done
def display_record():
    while True:
        print("-------------------------------------")
        print("Welcome to Display Record Page")
        print("-------------------------------------")
        print("Would you like to continue?")
        print("(1) Yes\n(2) No")
        pick = str(input("Enter a number:"))
        if pick == "1":
            print("-------------------------------------")
            print("(1) Food Category")
            print("(2) Customer Orders")
            print("(3) Customer Payment")
            print("(4) Exit")
            while True:
                option = str(input("Choose a Option:"))
                if option == "1":
                    print("-------------------------------------")
                    print("Heading to Food Category")
                    foodcategory()
                elif option == "2":
                    print("-------------------------------------")
                    print("Heading to Customer Order")
                    customer_order()
                elif option == "3":
                    print("-------------------------------------")
                    print("Heading to Customer Payment")
                    customer_payment()
                else:
                    print("Invalid Option, Try Again")
        elif pick == "2":
            print("-------------------------------------")
            print("You will be log out!")
            print("-------------------------------------")
            print("Returning to Menu...")
            print("-------------------------------------")
            admin_page()
        else:
            print("Invalid Option, Try Again")


# done
def add_menu():
    while True:
        print("-------------------------------------")
        print("Welcome to Add Item Menu Page")
        print("-------------------------------------")
        print("Would you like to continue?")
        print("(1) Yes\n(2) No")
        pick = str(input("Enter a number:"))
        while True:
            if pick == "1":
                print("-------------------------------------")
                print("(1) Add Food")
                print("(2) Add Drink")
                print("(3) Add Snack")
                print("(4) Exit")
                option = str(input("Choose a Option:"))
                if option == "1":
                    print("-------------------------------------")
                    print("Heading to Add Food")
                    add_food()
                    break
                elif option == "2":
                    print("-------------------------------------")
                    print("Heading to Add Drinks")
                    add_drink()
                    break
                elif option == "3":
                    print("-------------------------------------")
                    print("Heading to Add Snacks")
                    add_snack()
                    break
                elif option == "4":
                    print("-------------------------------------")
                    print("Exiting...")
                    print("-------------------------------------")
                    exit()
                else:
                    print("Invalid Option, Try Again")
            elif pick == "2":
                print("-------------------------------------")
                print("You will be log out!")
                print("-------------------------------------")
                print("Returning to Menu...")
                print("-------------------------------------")
                admin_login()
                break
            else:
                print("Invalid Option, Try Again")


# done
def add_food():
    print("Code\t\tFoods\t\t\t\tPrice")
    with open('FoodMenu.txt', 'r') as read_file:
        x = read_file.readlines()
        for i in x:
            var = i.split(";")
            spaces = 20 - len(var[1])
            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
        foodid = str(input("Enter foodid: ")).upper()
        foodname = str(input("Enter food name: ")).upper()
        foodprice = float(input("RM:"))
        foodprice = format(foodprice, ".2f")
    with open("FoodMenu.txt", "a") as menu:
        menu.write(foodid + ";" + foodname + ";" + foodprice + ";" + '\n')
    print("\n")
    with open("FoodMenu.txt", "r"):
        print("Food ID   :", foodid)
        print("Food Name :", foodname)
        print("Food Price:", foodprice)
        add_menu()


# done
def add_drink():
    print("Code\t\tDrinks\t\t\t\tPrice")
    with open('DrinkMenu.txt', 'r') as read_file:
        x = read_file.readlines()
        for i in x:
            var = i.split(";")
            spaces = 20 - len(var[1])
            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
        drinkid = str(input("Enter drinkid: ")).upper()
        drinkname = str(input("Enter drink name: ")).upper()
        drinkprice = float(input("RM:"))
        drinkprice = format(drinkprice, ".2f")
        with open("DrinkMenu.txt", "a") as menu:
            menu.write(drinkid + ";" + drinkname + ";" + drinkprice + ";" + '\n')
        print("\n")
        with open("DrinkMenu.txt", "r"):
            print("Drink ID   :", drinkid)
            print("Drink Name :", drinkname)
            print("Drink Price:", drinkprice)
            add_menu()


# done
def add_snack():
    print("Code\t\tSnacks\t\t\t\tPrice")
    with open('SnacksMenu.txt', 'r') as read_file:
        x = read_file.readlines()
        for i in x:
            var = i.split(";")
            spaces = 20 - len(var[1])
            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
        snackid = str(input("Enter snackid: ")).upper()
        snackname = str(input("Enter snack name: ")).upper()
        snackprice = float(input("RM:"))
        snackprice = format(snackprice, ".2f")
        with open("SnacksMenu.txt", "a") as menu:
            menu.write(snackid + ";" + snackname + ";" + snackprice + ";" + '\n')
        print("\n")
        with open("SnacksMenu.txt", "r"):
            print("snack ID   :", snackid)
            print("snack Name :", snackname)
            print("snack Price:", snackprice)
            add_menu()


# done
def admin_modify_menu():
    while True:
        print(
            "Which Menu Would you like to Modify?\n1) Food menu\n2) Drink Menu\n3) Snacks Menu\n4) Delete Menu\n5) Exit")
        ans = str(input("Enter A Number: "))
        if ans == "1":
            print("-" * 50)
            print("You will be directed to Food Menu Modification Page....")
            print("-" * 50)
            modify_food()
            break
        elif ans == "2":
            print("-" * 50)
            print("You will be directed to Drink Menu Modification Page....")
            print("-" * 50)
            modify_drink()
            break
        elif ans == "3":
            print("-" * 50)
            print("You will be directed to Snacks Menu Modification Page....")
            print("-" * 50)
            modify_snacks_menu()
            break
        elif ans == "4":
            print("-" * 50)
            print("You will be directed to Delete Menu Page....")
            delete_menu_page()
            break
        elif ans == "5":
            print("-" * 50)
            print("You will be redirected to Admin Page....")
            admin_page()
        else:
            print("<<<Invalid Input. Enter Correct Value>>>")


def modify_food():
    while True:
        code = []
        name = []
        price = []
        print("Code\t\tFoods\t\t\t\tPrice")
        with open('FoodMenu.txt', 'r') as mod_file:
            x = mod_file.readlines()
            for i in x:
                var = i.split(";")
                code.append(var[0])
                name.append(var[1])
                price.append(var[2])
                spaces = 20 - len(var[1])
                print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
        print("Which item do you want to modify?")
        m_code = str(input("Code:")).upper()
        if m_code in code:
            index = code.index(m_code)
            new_name = str(input("Enter new name:")).upper()
            new_price = str(input("Enter new price:"))
            with open('FoodMenu.txt', 'r') as modfile:
                text_rep = modfile.read()
            text_rep = text_rep.replace(code[index] + ";" + name[index] + ";" + price[index] + ";" + "\n", m_code + ";"
                                        + new_name + ";" + new_price + ";" + '\n')
            with open('FoodMenu.txt', 'w') as modfile:
                modfile.write(text_rep)
            print("Item modified!")
            break
        else:
            print("Try again!")


# done

def modify_drink():
    while True:
        code = []
        name = []
        price = []
        print("Code\t\tDrinks\t\t\t\tPrice")
        with open('DrinkMenu.txt', 'r') as mod_file:
            x = mod_file.readlines()
            for i in x:
                var = i.split(";")
                code.append(var[0])
                name.append(var[1])
                price.append(var[2])
                spaces = 20 - len(var[1])
                print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
        print("Which item do you want to modify?")
        m_code = str(input("Code:")).upper()
        if m_code in code:
            index = code.index(m_code)
            new_name = str(input("Enter new name:")).upper()
            new_price = str(input("Enter new price:"))
            with open('DrinkMenu.txt', 'r') as modfile:
                text_rep = modfile.read()
            text_rep = text_rep.replace(code[index] + ";" + name[index] + ";" + price[index] + ";" + "\n", m_code + ";"
                                        + new_name + ";" + new_price + ";" + '\n')
            with open('DrinkMenu.txt', 'w') as modfile:
                modfile.write(text_rep)
            print("Item modified!")
            break
        else:
            print("Try again!")


# done
def modify_snacks_menu():
    while True:
        code = []
        name = []
        price = []
        print("Code\t\tSnacks\t\t\t\tPrice")
        with open('SnacksMenu.txt', 'r') as mod_file:
            x = mod_file.readlines()
            for i in x:
                var = i.split(";")
                code.append(var[0])
                name.append(var[1])
                price.append(var[2])
                spaces = 20 - len(var[1])
                print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
        print("Which item do you want to modify?")
        m_code = str(input("Code:")).upper()
        if m_code in code:
            index = code.index(m_code)
            new_name = str(input("Enter new name:")).upper()
            new_price = str(input("Enter new price:"))
            with open('SnacksMenu.txt', 'r') as modfile:
                text_rep = modfile.read()
            text_rep = text_rep.replace(code[index] + ";" + name[index] + ";" + price[index] + ";" + "\n", m_code + ";"
                                        + new_name + ";" + new_price + ";" + '\n')
            with open('SnacksMenu.txt', 'w') as modfile:
                modfile.write(text_rep)
            print("Item modified!")
            break
        else:
            print("Try again!")


def delete_menu_page():
    while True:
        print("Which Menu Would you like to Delete?\n1) Food menu\n2) Drink Menu\n3) Snacks Menu\n4) Exit")
        ans = str(input("Enter A Number: "))
        if ans == "1":
            print("-" * 50)
            print("You will be directed to Food Menu Delete Page....")
            print("-" * 50)
            delete_foods_menu()
            break
        elif ans == "2":
            print("-" * 50)
            print("You will be directed to Drink Menu Delete Page....")
            print("-" * 50)
            delete_drinks_menu()
            break
        elif ans == "3":
            print("-" * 50)
            print("You will be directed to Snacks Menu Delete Page....")
            print("-" * 50)
            delete_snacks_menu()
            break
        elif ans == "4":
            print("-" * 50)
            print("You will be redirected to Admin Page....")
            admin_page()
        else:
            print("<<<Invalid Input. Enter Correct Value>>>")


def delete_foods_menu():
    while True:
        code = []
        name = []
        price = []
        print("Code\t\tFoods\t\t\t\tPrice")
        with open('FoodMenu.txt', 'r') as delete_file:
            x = delete_file.readlines()
            for i in x:
                var = i.split(";")
                code.append(var[0])
                name.append(var[1])
                price.append(var[2])
                spaces = 20 - len(var[1])
                print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
        print("Which item do you want to delete?")
        d_code = str(input("Code:")).upper()
        if d_code in code:
            index = code.index(d_code)
            with open('FoodMenu.txt', 'r') as deletefile:
                text_rep = deletefile.read()
            text_rep = text_rep.replace(code[index] + ";" + name[index] + ";" + price[index] + ";" + "\n", '')
            with open('FoodMenu.txt', 'w') as deletefile:
                deletefile.write(text_rep)
            print("Item deleted!")
            print("-" * 50)
            print("Code\t\tFoods\t\t\t\tPrice")
            with open('FoodMenu.txt', 'r') as read_file:
                x = read_file.readlines()
                for i in x:
                    var = i.split(";")
                    spaces = 20 - len(var[1])
                    print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
            break
        else:
            print("Try again!")


def delete_drinks_menu():
    while True:
        code = []
        name = []
        price = []
        print("Code\t\tDrinks\t\t\t\tPrice")
        with open('DrinkMenu.txt', 'r') as delete_file:
            x = delete_file.readlines()
            for i in x:
                var = i.split(";")
                code.append(var[0])
                name.append(var[1])
                price.append(var[2])
                spaces = 20 - len(var[1])
                print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
        print("Which item do you want to delete?")
        d_code = str(input("Code:")).upper()
        if d_code in code:
            index = code.index(d_code)
            with open('DrinkMenu.txt', 'r') as deletefile:
                text_rep = deletefile.read()
            text_rep = text_rep.replace(code[index] + ";" + name[index] + ";" + price[index] + ";" + "\n", '')
            with open('DrinkMenu.txt', 'w') as deletefile:
                deletefile.write(text_rep)
            print("Item deleted!")
            print("-" * 50)
            print("Code\t\tDrinks\t\t\t\tPrice")
            with open('FoodMenu.txt', 'r') as read_file:
                x = read_file.readlines()
                for i in x:
                    var = i.split(";")
                    spaces = 20 - len(var[1])
                    print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
            break
        else:
            print("Try again!")


def delete_snacks_menu():
    while True:
        code = []
        name = []
        price = []
        print("Code\t\tSnacks\t\t\t\tPrice")
        with open('SnacksMenu.txt', 'r') as delete_file:
            x = delete_file.readlines()
            for i in x:
                var = i.split(";")
                code.append(var[0])
                name.append(var[1])
                price.append(var[2])
                spaces = 20 - len(var[1])
                print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
        print("Which item do you want to delete?")
        d_code = str(input("Code:")).upper()
        if d_code in code:
            index = code.index(d_code)
            with open('SnacksMenu.txt', 'r') as deletefile:
                text_rep = deletefile.read()
            text_rep = text_rep.replace(code[index] + ";" + name[index] + ";" + price[index] + ";" + "\n", '')
            with open('SnacksMenu.txt', 'w') as deletefile:
                deletefile.write(text_rep)
            print("Item deleted!")
            print("-" * 50)
            print("Code\t\tSnacks\t\t\t\tPrice")
            with open('FoodMenu.txt', 'r') as read_file:
                x = read_file.readlines()
                for i in x:
                    var = i.split(";")
                    spaces = 20 - len(var[1])
                    print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
            break
        else:
            print("Try again!")


##########################
def foodcategory():
    print("-" * 45)
    print("Welcome to Food Category Page")
    print("-" * 45)
    print("Choose your option: ")
    print("(1) Yes\n(2) No")
    while True:
        num = str(input("Enter Number: "))
        if num == "1":
            while True:
                print("Food Category")
                print("(1) Foods")
                print("(2) Drinks")
                print("(3) Snacks")
                print("(4) Back to Food Category Page")
                pick = str(input("Choose Your option:"))
                if pick == "1":
                    print("Code\t\tFoods\t\t\t\tPrice")
                    with open('FoodMenu.txt', 'r') as read_file:
                        x = read_file.readlines()
                        for i in x:
                            var = i.split(";")
                            spaces = 20 - len(var[1])
                            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
                elif pick == "2":
                    print("Code\t\tDrinks\t\t\t\tPrice")
                    with open('DrinkMenu.txt', 'r') as read_file:
                        x = read_file.readlines()
                        for i in x:
                            var = i.split(";")
                            spaces = 20 - len(var[1])
                            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
                elif pick == "3":
                    print("Code\t\tSnacks\t\t\t\tPrice")
                    with open('SnacksMenu.txt', 'r') as read_file:
                        x = read_file.readlines()
                        for i in x:
                            var = i.split(";")
                            spaces = 20 - len(var[1])
                            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
                elif pick == "4":
                    print("Directing to Food Category Page")
                    foodcategory()
                    break
                else:
                    print("Invalid Input, Please Try Again")
        elif num == "2":
            print("Directing to Display Record Page")
            display_record()
            break
        else:
            print("Invalid Input, Please Try Again")


def customer_order():
    while True:
        print("-" * 50)
        print("1)View all orders\n2)Exit")
        ans = str(input("Enter a number: ")).upper()
        if ans == "1":
            print("=" * 50)
            print("\t\t\t\t  All Orders")
            print("-" * 50)
            with open("Orders.txt", "r") as File:
                lines = File.readlines()
                for i in lines:
                    line = i.split(";")
                    print("=" * 50)
                    print(f"ID:", line[0])
                    print("-" * 50)
                    line.pop(0)
                    print(f"Ordered at:", line[-1])
                    line.pop(-1)
                    for j in line:
                        if j == line[-1]:
                            print("-" * 50)
                            print("Total Price: " + j)
                            print("=" * 50)
                            print("\n")
                            break
                        print(j)
        elif ans == "2":
            print("You are directed to Admin Main page.")
            admin_page()
            break
        else:
            print("Invalid input. Try again.")


def customer_payment():
    while True:
        print("-" * 50)
        print("1)View all customers' payment records\n2)Exit")
        ans = str(input("Enter a number: ")).upper()
        if ans == "1":
            print("=" * 50)
            print("\t\t\t\tAll Payments")
            print("-" * 50)
            with open("Payments.txt", "r") as File:
                lines = File.readlines()
                for i in lines:
                    line = i.split(';')
                    print("=" * 50)
                    print(f"ID:", line[0])
                    print("-" * 50)
                    line.pop(0)
                    print(f"Paid at: ", line[-1])
                    line.pop(-1)
                    print("Customer Name:", line[1])
                    print("Card Number:", line[2])
                    print("Card Type:", line[3])
                    print("Expiry Date(MM/YYYY):", line[4])
                    print("CVC:", line[5])
                    print("Delivery Address:", line[6])
                    print("Payment Amount: RM", line[0])
                    print("=" * 50)
        elif ans == "2":
            print("You are directed to Admin Main page.")
            admin_page()
            break
        else:
            print("Invalid input. Try again.")


def search_specific_page():
    while True:
        print("-------------------------------------")
        print("Welcome to Searching Record Page")
        print("-------------------------------------")
        print("Would you like to continue?")
        print("(1) Yes\n(2) No")
        pick = str(input("Enter a number:"))
        if pick == "1":
            print("-------------------------------------")
            print(" What record would you like to search for?")
            print("(1) Customer Order")
            print("(2) Customer Payment")
            print("(3) Exit")
            while True:
                option = str(input("Choose a Option:"))
                if option == "1":
                    print("-------------------------------------")
                    print("Heading to Customer Order")
                    print("-------------------------------------")
                    query_customerorder_admin()
                if option == "2":
                    print("-------------------------------------")
                    print("Heading to Customer Payment")
                    print("-------------------------------------")
                    query_CustomerPayment_admin()
                elif option == "3":
                    print("-------------------------------------")
                    print("Returning to Admin Page")
                    print("-------------------------------------")
                    admin_page()
        elif pick == "2":
            print("-------------------------------------")
            print("You will be log out!")
            print("-------------------------------------")
            print("Returning to Menu...")
            print("-------------------------------------")
            admin_login()
        else:
            print("Invalid Option, Try Again")


# done
def query_customerorder_admin():
    while True:
        print("-" * 50)
        print("1)Search order record\n2)Exit")
        ans = str(input("Enter a number: ")).upper()
        if ans == "1":
            print("=" * 50)
            print("\t\t\t\tOrder Search")
            print("-" * 50)
            ic = str(input("Please Enter IC Number to search: "))
            with open("Orders.txt", "r") as orderfile:
                lines = orderfile.readlines()
                for i in lines:
                    x = i.split(";")
                    if ic == x[0]:
                        print("-" * 50)
                        print("IC Number :" + x[0])
                        print("-" * 50)
                        x.remove(x[0])
                        for y in x:
                            if y == x[-1]:
                                print("-" * 50)
                                print("Subtotal : " + y)
                                print("-" * 50)
                                break
                            print(y)
        elif ans == "2":
            print("Back to Admin Main page.")
            admin_page()
            break
        else:
            print("Invalid input. Try again.")


def query_CustomerPayment_admin():
    while True:
        print("-" * 50)
        print("1)Search payment record\n2)Exit")
        ans = str(input("Enter a number: ")).upper()
        if ans == "1":
            print("=" * 50)
            print("\t\t\t\tPayment Query")
            print("-" * 50)
            search = str(input("Please Enter IC Number to search: "))
            with open("Payments.txt", "r") as PaymentFile:
                lines = PaymentFile.readlines()
                for i in lines:
                    x = i.split(';')
                    if search == x[0]:
                        print("-" * 50)
                        print("IC Number:" + x[0])
                        print("-" * 50)
                        x.remove(x[0])
                        print(f"Paid at: ", x[-1])
                        x.remove(x[-1])
                        print("Customer Name:", x[1])
                        print("Card Number:", x[2])
                        print("Card Type:", x[3])
                        print("Expiry Date:", x[4])
                        print("CVC:", x[5])
                        print("Delivery Address:", x[6])
                        print("Paid: RM", x[0])
                        print("-" * 50)
        elif ans == "2":
            print("Back to main page.")
            admin_page()
            break
        else:
            print("Invalid input. Try again.")


# done
####################customer
def customerpage():
    print("\n" * 1)
    print("-------------------------------------\n"
          "Welcome to the Customer Page\n"
          "-------------------------------------")
    print("Choose your Option")
    print("(1) Login\n"
          "(2) Sign Up\n"
          "(3) View Menu\n"
          "(4) Back to Welcome Page")
    while True:
        num1 = str(input("Choose your Option: "))
        if num1 == "1":
            print("-------------------------------------\n"
                  "Directing to Login Page\n"
                  "-------------------------------------")
            customer_login()
            break
        elif num1 == "2":
            print("-------------------------------------\n"
                  "Directing to Sign Up Page\n"
                  "-------------------------------------")
            customer_signup()
            break
        elif num1 == "3":
            print("-------------------------------------\n"
                  "Directing to Food Menu Page\n"
                  "-------------------------------------")
            menu()
            break
        elif num1 == "4":
            print("-------------------------------------\n"
                  "Directing to Menu Page\n"
                  "-------------------------------------")
            main()
            break
        else:
            print("Invalid Option")
    # done


def customer_login():
    while True:
        print("-------------------------------------\n"
              "Welcome to Customer Login Page\n"
              "-------------------------------------")
        print("Would You Like too continue?")
        print("(1)Yes\n(2)No")
        ans = str(input("Choose Your Option:"))
        if ans == "1":
            permission = False
            while not permission:
                with open('customer.txt', 'r') as AR:
                    print("Enter Customer username and password")
                    cusname = str(input("Username:")).upper()
                    cuspass = str(input("Password:"))
                    for line in AR:
                        if cusname + ";" + cuspass + ";" == line.strip():
                            permission = True
                            break
                    if permission == True:
                        print("Access Granted!!")
                        print("-------------------------------------")
                        print("Welcome", cusname)
                        print("-------------------------------------")
                        custmenu()
                        break
                    else:
                        print("Access Denied!!!")
        elif ans == "2":
            print("User will return to Customer Page")
            customerpage()
        else:
            print("Invalid Option")


# done
def customer_signup():
    detail = True
    while detail:

        print("\n" * 1)
        print("-------------------------------------\n"
              "Would you like to register an Customer account?\n"
              "-------------------------------------")
        print("(1) Yes\n(2) NO")
        reg = str(input("Choose your option:"))
        if reg == "1":
            print("-------------------------------------")
            print("Enter your Username to sign up.")
            print("-------------------------------------")
            while True:
                fourchar = False
                while not fourchar:
                    username = str(input("Username:")).upper()
                    if len(username) >= 4:
                        if len(username) <= 12:
                            fourchar = True
                        else:
                            fourchar = False
                            print("Username Can't Exceed 12 Characters long.")
                    else:
                        fourchar = False
                        print("Username must be in between 4 to 12 Character")

                    print("-------------------------------------\n"
                          "Password at least 5 characters\n"
                          "-------------------------------------")
                    pass1 = True
                    while pass1:
                        password = str(input("Enter a Password:"))
                        if len(password) >= 5:
                            pass1 = False
                        else:
                            print("Password is too short!")
                            pass1 = True

                    with open("customer.txt", "a") as CA:
                        CA.write(username + ";" + password + ";" + "\n")
                        print("-------------------------------------\n"
                              "Account is registered!!\n"
                              "Pls Login Again\n"
                              "-------------------------------------")
                        CA.close()
                        customer_login()
        elif reg == "2":
            print("User Will be Direct back to Customer Page")
            print("-------------------------------------")
            customerpage()
        else:
            print("Invalid Input")


def menu():
    while True:
        print("\n")
        print("-------------------------------------\n"
              "Welcome to the Menu Page\n"
              "-------------------------------------")
        option = input("Which Menu Would You Like to See?\n"
                       "(1) Food Menu\n"
                       "(2) Drinks Menu\n"
                       "(3) Snacks Manu\n"
                       "(4) Exit\n"
                       "Enter Your Option: ")
        if option == "1":
            print("-------------------------------------\n"
                  "Directing to Food Menu\n"
                  "-------------------------------------")
            cust_food_menu()
        elif option == "2":
            print("-------------------------------------\n"
                  "Directing to Drinks Menu\n"
                  "-------------------------------------")
            cust_drink_menu()
        elif option == "3":
            print("-------------------------------------\n"
                  "Directing to Snacks Manu\n"
                  "-------------------------------------")
            cust_snacks_menu()
        elif option == "4":
            print("-------------------------------------\n"
                  "Directing to Customer Page\n"
                  "-------------------------------------")
            customerpage()
        else:
            print("Invalid Option")


def cust_food_menu():
    print("Code\t\tFoods\t\t\t\tPrice")
    with open('FoodMenu.txt', 'r') as read_file:
        x = read_file.readlines()
        for i in x:
            var = i.split(";")
            spaces = 20 - len(var[1])
            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])


def cust_drink_menu():
    print("Code\t\tDrinks\t\t\t\tPrice")
    with open('DrinkMenu.txt', 'r') as read_file:
        x = read_file.readlines()
        for i in x:
            var = i.split(";")
            spaces = 20 - len(var[1])
            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])


def cust_snacks_menu():
    print("Code\t\tSnacks\t\t\t\tPrice")
    with open('SnacksMenu.txt', 'r') as read_file:
        x = read_file.readlines()
        for i in x:
            var = i.split(";")
            spaces = 20 - len(var[1])
            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])


def custmenu():
    print("\n" * 1)
    print("-------------------------------------\n"
          "Welcome to the Customer Menu\n"
          "-------------------------------------")
    print("Choose your Option")
    print("(1) View Menu\n"
          "(2) Select Item and add in cart\n"
          "(3) Exit")
    while True:
        pick = str(input("Enter a Option: "))
        if pick == "1":
            print("-------------------------------------\n"
                  "Directing to Menu\n"
                  "-------------------------------------")
            menu()
        if pick == "2":
            print("-------------------------------------\n"
                  "Directing to Select Item Page\n"
                  "-------------------------------------")
            cust_select_item()
        if pick == "3":
            print("-------------------------------------\n"
                  "Returning to Customer Page\n"
                  "-------------------------------------")

            customerpage()
        else:
            print("Invalid Option, Please Try Again")


# done
def cust_payment(total_price, icnumber):
    print("---------------Payment Page---------------")
    print("Please input the following details.")
    print("-" * 50)
    while True:
        print("Please enter Cardholder Name, IC Number, Card Number, Card Type, Expiry Date, CVC and Delivery Address.")
        cardholder = str(input("Cardholder Name: ")).upper()
        cardnumber = str(input("Card Number: ")).upper()
        cardtype = str(input("Card Type (MASTERCARD/VISA): ")).upper()
        expiry = str(input("Expiry Date(MM/YYYY): "))
        cvc = str(input("CVC: "))
        d_address = str(input("Delivery Address:")).upper()

        if len(cardholder) < 1:
            print("Invalid Cardholder Name.")
        elif len(cvc) != 3:
            print("Invalid CVC. Try again!")
        else:
            break
    clock = str(datetime.datetime.now())

    payment_details = str(
        icnumber + ';' + total_price + ';' + cardholder + ';' + cardnumber + ';' + cardtype + ';' + expiry + ';' + cvc + ';' + d_address + ';' + clock + '\n')

    with open("Payments.txt", "a") as File:
        File.write(payment_details)

    print("=" * 50)
    print(clock)
    print("Payment Done Successfully!")
    print("Thank you for your purchase")
    print("=" * 50)
    print("Going back to main page....")
    time.sleep(1)
    custmenu()


def cust_select_item():
    print("=" * 50)
    print("Add Items To Cart")
    print("=" * 50)
    display_menu()
    print("=" * 50)
    print("Enter the Item Code to add to cart\nEnter C to Confirm Orders in Cart\nEnter E to Exit")
    cart = []
    total_price = 0
    order = True
    while order:
        print("-" * 50)
        ans = str(input("Input: ")).upper()
        if ans == "E":
            print("-" * 50)
            print("You are being directed to the main page. Please Wait. . . .")
            time.sleep(2)
            custmenu()
            break
        elif ans[0] == "F":
            FoodMenu_code = []
            FoodMenu_price = []
            FoodMenu_name = []
            with open('FoodMenu.txt', 'r') as File:
                lines = File.readlines()
                for line in lines:
                    i = line.split(";")
                    FoodMenu_code.append(i[0])
                    FoodMenu_price.append(i[2])
                    FoodMenu_name.append(i[1])
            if ans in FoodMenu_code:
                c_index = FoodMenu_code.index(ans)
                spaces = 20 - len(FoodMenu_name[c_index])
                menu = str(
                    FoodMenu_code[c_index] + '\t\t' + FoodMenu_name[c_index] + " " * spaces + FoodMenu_price[c_index])
                text = str(FoodMenu_code[c_index] + ';' + FoodMenu_name[c_index] + ';' + FoodMenu_price[c_index])
                print("Code\t\tItem\t\t\t\tPrice")
                print(menu)
                cart.append(text)
                print("Item added to cart.")
                total_price = total_price + float(FoodMenu_price[c_index])
            else:
                print("Invalid input. Try again.")

        elif ans[0] == "D":
            DrinksMenu_code = []
            DrinksMenu_price = []
            DrinksMenu_name = []
            with open('DrinkMenu.txt', 'r') as File:
                lines = File.readlines()
                for line in lines:
                    i = line.split(";")
                    DrinksMenu_code.append(i[0])
                    DrinksMenu_price.append(i[2])
                    DrinksMenu_name.append(i[1])
            if ans in DrinksMenu_code:
                c_index = DrinksMenu_code.index(ans)
                spaces = 20 - len(DrinksMenu_name[c_index])
                menu = str(
                    DrinksMenu_code[c_index] + '\t\t' + DrinksMenu_name[c_index] + " " * spaces + DrinksMenu_price[
                        c_index])
                text = str(DrinksMenu_code[c_index] + ';' + DrinksMenu_name[c_index] + ';' + DrinksMenu_price[c_index])
                print("Code\t\tItem\t\t\t\tPrice")
                print(menu)
                cart.append(text)
                print("Item added to cart.")
                total_price = total_price + float(DrinksMenu_price[c_index])
            else:
                print("Invalid item code. Try again.")
        elif ans[0] == "S":
            SnacksMenu_code = []
            SnacksMenu_name = []
            SnacksMenu_price = []
            with open('SnacksMenu.txt', 'r') as File:
                lines = File.readlines()
                for line in lines:
                    i = line.split(";")
                    SnacksMenu_code.append(i[0])
                    SnacksMenu_name.append(i[1])
                    SnacksMenu_price.append(i[2])

            if ans in SnacksMenu_code:
                c_index = SnacksMenu_code.index(ans)
                spaces = 20 - len(SnacksMenu_name[c_index])
                menu = str(
                    SnacksMenu_code[c_index] + '\t\t' + SnacksMenu_name[c_index] + " " * spaces + SnacksMenu_price[
                        c_index])
                text = str(SnacksMenu_code[c_index] + ';' + SnacksMenu_name[c_index] + ';' + SnacksMenu_price[c_index])
                print("Code\t\tSnacks\t\t\t\tPrice")
                print(menu)
                cart.append(text)
                print("Item added to cart.")
                total_price = total_price + float(SnacksMenu_price[c_index])
            else:
                print("Invalid item code. Try again.")
        elif ans == "C":
            total_price = format(total_price, ".2f")
            print("\n")
            print("=" * 50)
            for i in cart:
                print(i)
            print("-" * 50)
            print(f"Subtotal = RM", total_price)
            print("=" * 50)
            while True:
                icnumber = str(input("Enter IC Number: "))
                if len(icnumber) != 12:
                    print("Invalid IC Number. Please try again!")
                else:
                    break

            with open('Orders.txt', 'a') as orderfile:
                orderfile.write(icnumber + ";" + ";".join(
                    cart) + ";" + "RM" + total_price + "\n")
                orderfile.flush()
            print("-" * 50)
            print("You are being directed to the Payment Page. Please Hold On. . . . ")
            time.sleep(1)
            cust_payment(total_price, icnumber)
            break
        else:
            print("Invalid input. Try again!")

def display_menu():
    print("Code\t\tFoods\t\t\t\tPrice")
    with open('FoodMenu.txt', 'r') as read_file:
        x = read_file.readlines()
        for i in x:
            var = i.split(";")
            spaces = 20 - len(var[1])
            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
    print("-" * 50)
    print("Code\t\tDrinks\t\t\t\tPrice")
    with open('DrinkMenu.txt', 'r') as read_file:
        x = read_file.readlines()
        for i in x:
            var = i.split(";")
            spaces = 20 - len(var[1])
            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])
    print("-" * 50)
    print("Code\t\tSnacks\t\t\t\tPrice")
    with open('SnacksMenu.txt', 'r') as read_file:
        x = read_file.readlines()
        for i in x:
            var = i.split(";")
            spaces = 20 - len(var[1])
            print(var[0] + "\t\t" + var[1] + " " * spaces + var[2])


##############################################Guest
def guestpage():
    while True:
        print("\n")
        print("-------------------------------------\n"
              "Welcome to the Guest Page\n"
              "-------------------------------------")
        option = input("Which Menu Would You Like to See?\n"
                       "(1) Food Menu\n"
                       "(2) Drinks Menu\n"
                       "(3) Snacks Manu\n"
                       "(4) Exit\n"
                       "Enter Your Option: ")
        if option == "1":
            print("-------------------------------------\n"
                  "Directing to Food Menu\n"
                  "-------------------------------------")
            cust_food_menu()
        elif option == "2":
            print("-------------------------------------\n"
                  "Directing to Drinks Menu\n"
                  "-------------------------------------")
            cust_drink_menu()
        elif option == "3":
            print("-------------------------------------\n"
                  "Directing to Snacks Manu\n"
                  "-------------------------------------")
            cust_snacks_menu()
        elif option == "4":
            print("-------------------------------------\n"
                  "Directing to Customer Page\n"
                  "-------------------------------------")
            customerpage()
        else:
            print("Invalid Option")




main()
