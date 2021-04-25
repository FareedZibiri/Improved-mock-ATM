#register
# - username, password, email
# - generate Account number

#login
# - (username or account number to login) and password

#bank operations

#Initializing the system

import random
database = {}

def init():

    isValidOptionSelected = False
    print("Welcome to BankPHP")

    while isValidOptionSelected == False:
        have_account  = int(input("Do you have an account?: 1 (yes) 2 (no) \n"))

        if(have_account == 1):
            isValidOptionSelected = True
            login()
        elif(have_account == 2):
            isValidOptionSelected = True
            register()
        else:
            print('Invalid Option Selected')

def login():
    print("***** Login *****")




    accountNumFromUser = int(input("Enter your Account Number \n"))
    password_given = input("Enter your password \n")

    for account_number, userDetails in database.items():
        if(account_number == accountNumFromUser):
            if(userDetails[3] == password_given):
                bankOperations(userDetails)
            else:
                print("Invalid account or password")
                login()




def register():
    print("***** Register *****")

    email = input("Enter you email address \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create your password \n")

    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password]

    print("Your account has been created successfully. Please keep it safe")
    print("-----------------------")
    print("Your account number is: %d " %account_number)
    print("-----------------------")
    login()

def bankOperations(user):
    print("Welcome %s %s " % (user[0], user[1]))
    selectedOption = int(input('Please select an option: (1) Deposit (2) Withdrawal (3) Complaint (4) Logout (5) Exit '))

    if (selectedOption == 1):
        depositOperation()

    elif (selectedOption == 2):
        withdrawalOperation()

    elif (selectedOption == 3):
        customerComplaint()

    elif(selectedOption == 4):
        logout()

    elif(selectedOption == 5):
        exit()

    else:
        print('Invalid Option selected, Please try again ')
        bankOperations(user)

def depositOperation():
    print("*** Deposit ***")
    amountDeposited = input('How much would you like to deposit? \n')
    print('This is your current balance')
    print("Thank you for banking with us")

def withdrawalOperation():
    print("*** Withdrawal ***")
    amountWithdrawed = input('How much would you like to withdraw? \n')
    print('Take your cash')
    print("Thank you for banking with us")

def customerComplaint():
    print("*** Customer Complaint ***")
    customerComplaint = input('What issue 1would you like to report? \n')
    print('Thank you for contacting us, we would work on your complaint shortly')
    print("Thank you for banking with us")

def logout():
    login()

def generate_account_number():
    return random.randrange(1111111111,9999999999)


init()


