import datetime, time, random

userDatabase = {} # transient database for users


accountBalance = 5000.50    # demo initial account balance
messageDecorator = '***'    # message decorator for messages

def init():
    """
    Function for actual banking system
    """
    print("Welcome to LBA")
 
    try:
        haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
        
        if(haveAccount == 1):
            login()

        elif(haveAccount == 2):
            register()
        else:
            print(f"You have selected invalid option, {messageDecorator}please try again{messageDecorator}"); print()
            init()
    except ValueError as e:
        print(f'You entered something wrong, {messageDecorator}please try again{messageDecorator}'); print()
        return init()

def login():
    """
    Login function
    """
    print("********* Login ***********")
    print()

    try:
        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("What is your password \n")

        for accountNumber, userDetails in userDatabase.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    bankOperation(userDetails)
                else:
                    print(f'Invalid account or password {messageDecorator}Please try again{messageDecorator}')
                    login(); print()
            else:
                print(f'Invalid account or password {messageDecorator}Please try again{messageDecorator}')
                login(); print()
    except ValueError as e:
        print(f'You entered something wrong, {messageDecorator}please try again{messageDecorator}'); print()
        return login()
    
    print()

    
def generationAccountNumber():
    """
    Function to automatically generate account number for new users
    """
    return random.randrange(1111111111, 9999999999)      

def register():
    """
    Function to register users
    """
    print("****** Register *******")

    email = str(input("What is your email address? \n"))
    first_name = str(input("What is your first name? \n"))
    last_name = str(input("What is your last name? \n"))
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()
    if accountNumber not in userDatabase:
        userDatabase[accountNumber] = [ first_name, last_name, email, password ]
    else:
        while accountNumber in userDatabase:
            accountNumber = generationAccountNumber

    print("Your Account Has been created")
    print(" === ====== ====== ====== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" === ====== ====== ====== ===")

    # print(userDatabase)     #check how the database looks like

    login()

def withdrawal():
    """
    Function for withdrawal
    """
    try:
        withdrawalAmount = round(float(input('How much would you like to withdraw: ')), 2)
        print(); print('processing...')
        time.sleep(1.5)
        withdrawalOutput = '\nPlease take your cash \n{}Your current balance is now ${}{}'.format(
                messageDecorator, (accountBalance - withdrawalAmount), messageDecorator)

        if (withdrawalAmount <= accountBalance):
                print(withdrawalOutput)
        else:
            withdrawalOutput = '{}Sorry, you can\'t withdraw more than you currently have. Please try again or quit{}'.format(
                messageDecorator, messageDecorator
            )
            print(withdrawalOutput); print()
            withdrawal()
    except ValueError as e:
        print(f'you have to enter a number'); print(f'{messageDecorator}please try again{messageDecorator}')
        withdrawal()

def deposit():
    """
    Function for deposit
    """
    try:

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
            print(depositOutput); print()
            deposit()

    except ValueError as e:
        print(f'you have to enter a number'); print(f'{messageDecorator}please try again{messageDecorator}')
        deposit()

def complaint():
    """
    Function to accomodate customer complaints
    """
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
    """
    Banking Operation Logic
    """
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

    try:
        
        selectedOption = int(input('What would you like to do?  '))
        optionSelectionMessage = 'you selected ' + str(selectedOption)

        #Withdrawal block            
        if(selectedOption == 1):
            print(optionSelectionMessage)
            withdrawal()
            
        #Cash deposit block            
        elif(selectedOption == 2):
            print(optionSelectionMessage)
            deposit()
            
        #Complaint block            
        elif(selectedOption == 3):
            print(optionSelectionMessage)
            complaint()

        elif(selectedOption == 4):
            exit()   
        else:
            print(f'Invalid Option "{selectedOption}" selected, {messageDecorator}please try again{messageDecorator}')
            bankOperation(user)
    except ValueError as e:
        print(f'You have to input an integer'); print('You can try again or enter "4" to quit')
        bankOperation(user)



#### ACTUAL BANKING SYSTEM #####

init()
