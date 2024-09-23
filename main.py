import time
from colorama import Fore, Style

def welcome_ascii_art_combined():
    welcome_text = f'''
        {Fore.CYAN}W   W  {Fore.YELLOW}EEEEE  {Fore.RED}L      {Fore.GREEN}CCCC  {Fore.BLUE}OOO  {Fore.MAGENTA}M   M  {Fore.CYAN}EEEEE
        {Fore.CYAN}W   W  {Fore.YELLOW}E      {Fore.RED}L     {Fore.GREEN}C     {Fore.BLUE}O   O {Fore.MAGENTA}MM MM  {Fore.CYAN}E
        {Fore.CYAN}W W W  {Fore.YELLOW}EEEE   {Fore.RED}L     {Fore.GREEN}C     {Fore.BLUE}O   O {Fore.MAGENTA}M M M  {Fore.CYAN}EEEE
        {Fore.CYAN}WW WW  {Fore.YELLOW}E      {Fore.RED}L     {Fore.GREEN}C     {Fore.BLUE}O   O {Fore.MAGENTA}M   M  {Fore.CYAN}E
        {Fore.CYAN}W   W  {Fore.YELLOW}EEEEE  {Fore.RED}LLLLL  {Fore.GREEN}CCCC  {Fore.BLUE}OOO  {Fore.MAGENTA}M   M  {Fore.CYAN}EEEEE
    {Style.RESET_ALL}
    '''
    
    border = '*' * 60
    print(border)
    print(border)
    
    for line in welcome_text.split('\n'):
        print(line.center(80))
        time.sleep(0.5)  

    border = '*' * 60
    print(border)
    print(border)


def goodbye_ascii_art_combined():
    goodbye_text = f'''
    {Fore.CYAN} GGGGG     {Fore.YELLOW} OOOOO      {Fore.RED} DDDDD      {Fore.GREEN} BBBBB     {Fore.BLUE} Y     Y    {Fore.MAGENTA} EEEEE
    {Fore.CYAN}G     G    {Fore.YELLOW}O     O     {Fore.RED}D     D     {Fore.GREEN}B     B     {Fore.BLUE} Y   Y     {Fore.MAGENTA} E
    {Fore.CYAN}G          {Fore.YELLOW}O     O     {Fore.RED}D     D     {Fore.GREEN}B     B      {Fore.BLUE} Y Y      {Fore.MAGENTA} E
    {Fore.CYAN}G   GGG    {Fore.YELLOW}O     O     {Fore.RED}D     D     {Fore.GREEN}BBBBBB        {Fore.BLUE} Y       {Fore.MAGENTA} EEE
    {Fore.CYAN}G     G    {Fore.YELLOW}O     O     {Fore.RED}D     D     {Fore.GREEN}B     B        {Fore.BLUE}Y       {Fore.MAGENTA} E
    {Fore.CYAN}G     G    {Fore.YELLOW}O     O     {Fore.RED}D     D     {Fore.GREEN}B     B        {Fore.BLUE}Y       {Fore.MAGENTA} E
    {Fore.CYAN} GGGGG     {Fore.YELLOW} OOOOO      {Fore.RED} DDDDD      {Fore.GREEN} BBBBB         {Fore.BLUE}Y        {Fore.MAGENTA}EEEEE
    {Style.RESET_ALL}
    '''

    border = '*' * 80
    print(border)
    print(border)
    
    for line in goodbye_text.split('\n'):
        print(line.center(100))
        time.sleep(0.5) 

    print(border)
    print(border)


def number_checking(item):
    while not item.isnumeric():
        print("Please enter your data in number.")
        item = input("Please enter again:")
    return item

def character_checking(item):
    while not item.isalpha():
        print("Please enter your data in characters.")
        item = input("Please enter again:")
    return item


def decimal_checking(item):
    while True:
        try:
            float(item)
            break
        except ValueError:
            print("Wrong input! \nPlease enter your data in decimal value.")
            item = input("Please enter again: ")
    return item


def read_inventory_file():
    masterlist = []
    with open("inventory.txt", "r") as f:
        for line in f:
            masterlist.append(line.strip().split(","))
    return masterlist

def write_inventory_file(masterlist):
    z = open("inventory.txt", "w")
    for item in masterlist:
        z.write(",".join(map(str, item)))
        z.write("\n")


def read_userdata_file():
    masterlist = []
    with open("userdata.txt", "r") as x:
        for line in x:
            masterlist.append(line.strip().split(","))
    return masterlist


def insert_new_item():
    item_number = (input("Please enter the amount of item: "))
    item_number = int(number_checking(item_number))

    for i in range(item_number):
        item_code = (input("Please enter the code of the item: "))
        item_code = number_checking(item_code)
        description = (input("Please enter the description of the item (Product name): "))
        description = character_checking(description)
        category = (input("Please enter the category of the item(fruits,drinks,seafood,meat,beef,lamb or any): "))
        category = character_checking(category)
        unit = (input("Please enter the unit of the item (boxes, cans, kg(kilogram), packets or any): "))
        unit = character_checking(unit)
        price = (input("Please enter the price of the item (in RM): "))
        price = decimal_checking(price)
        quantity = (input("Please enter the quantity of the item: "))
        quantity = number_checking(quantity)
        minimum = (input("Please enter the minimum amount of the item: "))
        minimum = number_checking(minimum)
        temporary_list = [item_code, description, category, unit, price, quantity, minimum]
        f = open("inventory.txt", "a")
        f.write(",".join(map(str, temporary_list)))
        f.write("\n")

def update_item():
    update_item_code = (input("Please enter the code you need to update: "))
    update_item_code = number_checking(update_item_code)
    masterlist = read_inventory_file()
    for item in masterlist:
        if update_item_code == item[0]:
            item_need_change = (input("Please enter the total number of item you want to change: "))
            item_need_change = number_checking(item_need_change)
            for i in range(int(item_need_change)):
                print("Change ITEM CODE press 0")
                print("Change ITEM DESCRIPTION press 1")
                print("Change ITEM CATEGORY press 2")
                print("Change ITEM UNIT press 3")
                print("Change ITEM PRICE press 4")
                print("Change ITEM QUANTITY press 5")
                print("Change ITEM MINUMUM press 6")
                change = (input("Please enter the item you want to change: "))
                change = int(number_checking(change))
                if change == 0:
                    item[0] = str(input("Please enter the new item code: "))
                    item[0] = number_checking(item[0])
                elif change == 1:
                    item[1] = str(input("Please enter the new item description: "))
                    item[1] = character_checking(item[1])
                elif change == 2:
                    item[2] = str(input("Please enter the new item category: "))
                    item[2] = character_checking(item[2])
                elif change == 3:
                    item[3] = str(input("Please enter the new item unit: "))
                    item[3] = character_checking(item[3])
                elif change == 4:
                    item[4] = str(input("Please enter the new item price: "))
                    item[4] = decimal_checking(item[4])
                elif change == 5:
                    item[5] = str(input("Please enter the new item quantity: "))
                    item[5] = number_checking(item[5])
                elif change == 6:
                    item[6] = str(input("Please enter the new item minimum: "))
                    item[6] = number_checking(item[6])
    write_inventory_file(masterlist)

def delete_item():
    delete_item = str(input("Please enter the item code that you want to remove: "))
    delete_item = number_checking(delete_item)
    masterlist = read_inventory_file()
    for item in masterlist:
        if delete_item == item[0]:
            masterlist.remove(item)
    write_inventory_file(masterlist)

def stock_taking ():
    masterlist = read_inventory_file()
    stock_taking = (input("Please enter the item code that you want to check: "))
    stock_taking = number_checking(stock_taking)
    for item in masterlist:
        if stock_taking == item[0]:
            print(item[5])
            question = str(input("Do you want to change the quantity of the item(yes/no): "))
            question = character_checking(question)
            if question == "yes" :
                user = (input("Please enter the amount of the quantity of the item: "))
                user = number_checking(user)
                item[5] = user
    write_inventory_file(masterlist)

def view_replenish_list ():
    masterlist = read_inventory_file()
    temp=0
    for item in masterlist:
        if int(item[5])<int(item[6]):
            print(item)
            temp=temp+1
    if temp==0:
        print("NO ITEMS IS BELOW THE MINIMUM THRESHOLD")

def stock_replenishment ():
    item_code = (input("Please enter the item code to show you the quantity of the item: "))
    item_code = number_checking(item_code)
    masterlist = read_inventory_file()
    for item in masterlist:
        if int(item_code) == int(item[0]):
            print(item[5])
            item[5] = (input("Please enter the new purchased item's quantity: "))
            item[5] = number_checking(item[5])
    write_inventory_file(masterlist)


def search ():
    item_types=str(input("Search for description = 0. Search for code range = 1. Search for category = 2. Search for price range = 3: "))
    item_types = number_checking(item_types)
    masterlist = read_inventory_file()
    if item_types == "0":
        item_description = str(input("Please enter the description of the item: "))
        item_description = character_checking(item_description)
        for item in masterlist:
            if item_description == item[1]:
                print(item)
    elif item_types == "1":
        min_item_code = (input("Please enter the minimum item code: "))
        min_item_code = number_checking(min_item_code)
        max_item_code = (input("Please enter the maximum item code: "))
        max_item_code = number_checking(max_item_code)
        for item in masterlist:
            if int(min_item_code)<int(item[0]) and int(max_item_code)>int(item[0]):
                print(item)
    elif item_types == "2":
        item_category = str(input("Please enter the category of the item: "))
        item_category = character_checking(item_category)
        for item in masterlist:
            if item_category == item[2]:
                print(item)
    elif item_types == "3":
        min_price_range = (input("Please enter the minimum price of the item: "))
        min_price_range = decimal_checking(min_price_range)
        max_price_range = (input("Please enter the maximum price of the item: "))
        max_price_range = decimal_checking(max_price_range)
        for item in masterlist:
            if float(min_price_range)<float(item[4]) and float(max_price_range)>float(item[4]):
                print(item)

def sign_up():
    masterlist = read_userdata_file()
    username = str(input("Please enter your user ID: "))
    username = character_checking(username)
    password = str(input("Please enter your password: "))
    password = character_checking(password)
    reconfirm_password = str(input("Please enter your password to reconfirm: "))
    reconfirm_password = character_checking(reconfirm_password)
    for user in masterlist:
        while username == user[0]:
            print("Your user ID is used.")
            username = str(input("Please try another user ID: "))
            username = character_checking(username)
            continue

    while password != reconfirm_password:
        print("Please type your password again.")
        password = str(input("Please re-enter your password: "))
        password = character_checking(password)
        reconfirm_password = str(input("Please reconfirm your password: "))
        reconfirm_password = character_checking(reconfirm_password)
    print("Please choose your role.")
    print("Admin-1, Inventory-checker-2, Purchaser-3")
    roles = str(input("Please enter your roles: "))
    roles=int(number_checking(roles))
    while roles != 1 and roles != 2 and roles != 3:
        print("Your choice is invalid. Please try again.")
        roles = str(input("Please enter your roles: "))
        roles = int(number_checking(roles))

    user_list = [username, password, str(roles)]
    f = open("userdata.txt", "a")
    f.write(",".join(map(str, user_list)))
    f.write("\n")


masterlist = read_userdata_file()
login=False
while login==False:
    welcome_ascii_art_combined()
    username = str(input("Please enter your user ID: "))
    username = character_checking(username)
    password = str(input("Please enter your password: "))
    password = character_checking(password)

    for user in masterlist:
        if username == user[0] and password == user[1]:
            login=True
            print("log in successful")
            resume = 1
            #User role:
            #Admin-1, Inventory-checker-2, Purchaser-3
            while resume == 1: 
                if user[2] == "1":
                    print("insert Item - 1")
                    print("update Item - 2")
                    print("delete Item - 3")
                    print("stock taking - 4")
                    print("view replenish list - 5")
                    print("stock replenishment - 6")
                    print("search Item - 7")
                    print("sign up - 8")
                    ask_function=(input("Please enter which number of the functions you want to access."))
                    ask_function =int(number_checking(ask_function))
                    while ask_function<1 or ask_function>8:
                        print("Your data is invalid. Please enter again.")
                        ask_function=(input("Please enter function you want to access."))
                        ask_function=int(number_checking(ask_function))
                    if ask_function == 1:
                        insert_new_item()
                    elif ask_function == 2:
                        update_item()
                    elif ask_function == 3:
                        delete_item()
                    elif ask_function == 4:
                        stock_taking()
                    elif ask_function == 5:
                        view_replenish_list()
                    elif ask_function == 6:
                        stock_replenishment()
                    elif ask_function == 7:
                        search()
                    elif ask_function == 8:
                        sign_up()
                elif user[2] == "2":
                    print("stock taking - 1")
                    print("search Item - 2")
                    ask_function = (input("Please enter which number of the functions you want to access."))
                    ask_function = int(number_checking(ask_function))
                    while ask_function !=1 and ask_function !=2:
                        print("Your data is invalid. Please enter again.")
                        ask_function = (input("Please enter function you want to access."))
                        ask_function = int(number_checking(ask_function))
                    if ask_function == 1:
                        stock_taking()
                    elif ask_function == 2:
                        search()
                elif user[2] == "3":
                    print("view replenish list - 1")
                    print("stock replenishment - 2")
                    print("search Item - 3")
                    ask_function = (input("Please enter which number of the functions you want to access."))
                    ask_function = int(number_checking(ask_function))
                    while ask_function !=1 and ask_function !=2 and ask_function !=3:
                        print("Your data is invalid. Please enter again.")
                        ask_function = (input("Please enter function you want to access."))
                        ask_function = int(number_checking(ask_function))
                    if ask_function == 1:
                        view_replenish_list()
                    elif ask_function == 2:
                        stock_replenishment()
                    elif ask_function == 3:
                        search()
                print("-------------------------------------------------")
                print("Do you want to continue with the other functions?")
                print("1. Yes 2. No")
                resume = (input("Please enter your choice."))
                resume = int(number_checking(resume))
                if resume == 2:
                    print("Logout successfully.")
                    goodbye_ascii_art_combined()

    if login==False:
        print("Login is Failed")
