import datetime, time, random

Database = {'Goodness': 'goody', 'Doris': 'passDoris',
                    'Mike': 'passMike', 'Seyi': 'passSeyi', '':''}

userDatabase = {} #transient database


accountBalance = 5000.50
messageDecorator = '***'

def init():
   
    print("Welcome to bankPHP")
 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()

def login():
    print("********* Login ***********")
    print()

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in userDatabase.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
    

    print()

    
def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)      

def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()
    if accountNumber not in userDatabase:
        userDatabase[accountNumber] = [ first_name, last_name, email, password ]
    else:
        while accountNumber in userDatabase:
            accountNumber = generationAccountNumber

    print(accountNumber)
    print(type(accountNumber))

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    print(userDatabase)

    login()

def withdrawal():
    withdrawalAmount = round(float(input('How much would you like to withdraw: ')), 2)
    print(); print('processing...')
    time.sleep(1.5)
    withdrawalOutput = '\nPlease take your cash \n{}Your current balance is now ${}{}'.format(
            messageDecorator, (accountBalance - withdrawalAmount), messageDecorator)

    if (withdrawalAmount <= accountBalance):
            print(withdrawalOutput)
    else:
        withdrawalOutput = '{}Sorry, you can\'t withdraw more than you have currently. Please try again{}'.format(
            messageDecorator, messageDecorator
        )
        print(withdrawalOutput)    

def deposit():
    depositAmount = round(float(input('Enter your deposit amount: ')), 2)
    print()
    depositOutput = '{}Thank you! Your current balance is now {}{}'.format(
        messageDecorator, (accountBalance + depositAmount), messageDecorator
    )

    if (depositAmount >= 5):
            print(depositOutput)
    else:
        depositOutput = '{}Sorry, you can\'t deposit less than $5. Please try again{}'.format(
            messageDecorator, messageDecorator
        )
        print(depositOutput)

def complaint():
    complaintMessage = input('What issue will you like to report?\n')
    outputMessage = '{}Thank you for contacting us{}'.format(
        messageDecorator, messageDecorator
    )
    if (complaintMessage != ''):
        print(outputMessage)
    else:
        print('{}You didn\'t report anything. Thank you{}'.format(
            messageDecorator, messageDecorator
        ))


def bankOperation(user):
    print()
    print("Welcome %s %s " % ( user[0], user[1] ) )

    now = datetime.datetime.now()
    print('You logged in at: {}'.format(
            now.strftime('%Y-%m-%d %H:%M:%S')
        ))
    print()
    print("***Please note that all transactions are to 2 decimal places, amounts are rounded to that effect***")

    print('\nThese are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('What would you like to do?  '))
    optionSelectionMessage = print('you selected {}'.format(selectedOption))

    #Withdrawal block            
    if(selectedOption == 1):
        optionSelectionMessage
        withdrawal()
        
    #Cash deposit block            
    elif(selectedOption == 2):
        optionSelectionMessage
        deposit()
        
    #Complaint block            
    elif(selectedOption == 3):
        optionSelectionMessage
        complaint()

    elif(selectedOption == 4):
        exit()   
    else:
        print('Invalid Option selected, please try again')


#### ACTUAL BANKING SYSTEM #####

init()

# TODO
# try and except clause for each block