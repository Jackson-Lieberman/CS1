import csv


Websites = []
Usernames = []
Passwords = []

def setup(Websites, Usernames, Passwords):
    '''
    Adds a password username and website to each of their lists
    Args:
        websites(lst): the list of websites
        Usernames(lst): list of user name
        Passwords(str): list of passwords        
    '''
    web = input('What Webite would you like to make a password for: ').lower()
    Websites.append(web)
    user = input("What's your username for this website: ")
    Usernames.append(user)
    passw = input("What's your password for this website: ")
    Passwords.append(passw)
def show(Websites, Usernames, Passwords):
    '''
    shows the user a requested set of websites usernames and passwords
    Args:
        websites(lst): the list of websites
        Usernames(lst): list of user name
        Passwords(str): list of passwords        
    '''
    a = str(input('Which user names and passwords would you like to see? (Say all to see the whole list)')).lower()
    
    if a == 'all':
        print(f'Websites: {Websites}')
        print(f'Usernames: {Usernames}')
        print(f'Passwords: {Passwords}')
    elif a in Websites:
        index = Websites.index(a)
        print(f'Website: {a}')
        print(f'User: {Usernames[index]}')
        print(f'Pass: {Passwords[index]}')
    elif a in Usernames:
        index = Usernames.index(a)
        print(f'Website: {Websites[index]}')
        print(f'User: {a}')
        print(f'Pass: {Passwords[index]}')
    else:
        print('not a value')
def export(filename,Headers,*arrays):
    '''
    exports the passwords, usernames and websites into a csv file
    Args:
        filename(str): name of the file
        Header(lst): Headers of each column in the csv file
        *arrays(): the contents of each column     
    '''
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(Headers) 
        for row in zip(*arrays):
            writer.writerow(row)

def leave():
    '''
    lets the user leave the code 
    '''
    leave=input('Would you like to leave?(y/n): ').lower()
    if leave == 'y':
        print('Okay bye!')
        quit()

print("Welcome to Jackson's password keeper")
setup(Websites, Usernames, Passwords)   

while True:
    cont = input('Would you like to continue adding websites?(y/n): ').lower()
    
    if cont == 'y':
        setup(Websites, Usernames, Passwords)
    elif cont == 'n':
        showpass= input('Would you like to veiw your passwords?(y/n): ').lower()
        
        if showpass == 'y':
            show(Websites, Usernames, Passwords)
        elif showpass == 'n':
            exportCSV= input('Would you like to export your passwords to a csv file?(y/n):').lower()
            if exportCSV == 'y':
                export("passwords.csv", ['Websites', 'Usernames', 'Passwords'], Websites, Usernames, Passwords)
                print('They have been added to the file passwords.csv!')
            elif exportCSV== 'n':
                leave()
    else:
        print('Invalid')
    