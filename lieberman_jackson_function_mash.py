import random

def chorus(index):
    artist= ['Jay-Z', "Britney"]
    '''
    Reduces the number of print statements needed to sing a songs chorus 
    Args:
        i(int): Each chorus the artist mentioned changes so this will help change the artist in each chorus by acessing the index of the list
    Returns:
        prints the chorus of party in the USA
    '''
    artist = artist[index]
    print(f''' My tummy's turnin' and I'm feelin' kinda homesick
Too much pressure and I'm nervous
That's when the DJ dropped my favorite tune
And a {artist} song was on
And a {artist} song was on
And a {artist} song was on
So I put my hands up
They're playin' my song, the butterflies fly away
I'm noddin' my head like, yeah
Movin' my hips like, yeah
I got my hands up, they're playin' my song
They know I'm gonna be okay
Yeah, it's a party in the U.S.A.
Yeah, it's a party in the U.S.A.''')
    
def SingSong(time):
    '''
    Reduces the number of print statements needed to sing Party in the USA's bridge 
    Args:
        time(int): the bridge is different the first time so it uses this to vary what its printint
    Returns:
        prints the bridge of party in the USA
    '''
    if time == 1:
        print(f'''I hopped off the plane at LAX
With a dream and my cardigan
Welcome to the land of fame excess (whoa)
Am I gonna fit in?
Jumped in the cab, here I am for the first time
Look to my right, and I see the Hollywood sign
This is all so crazy
Everybody seems so famous''')
    else:
        print(f'''Get to the club in my taxi cab
Everybody's looking at me now
Like, "Who's that chick that's rockin' kicks?
She gotta be from out of town"
So hard with my girls not around me
It's definitely not a Nashville party
'Cause all I see are stilettos
I guess I never got the memo''')
          





def add(n1, n2):
    '''
    Takes two numbers and prints their sum

    Args:
        n1(int): first number added
        n2(int): second number being added
    Returns:
        prints the 2 numbers added
    '''
    print(n1+n2)


def print_list(list1):
    '''
    prints a list
    Args:
        list1(lst): list of numbers
    Returns:
        the list printed, each element on its own line
    '''
    for i in list1:
        print(i)

def in_list(list1, article):
    '''
    checks if an element is in a list
    Args:
        list1(lst): list that we are checking
        article(str): the item we check to see if in the list
    Returns:
        bool: if the article is in the list
    '''
    for element in list1:
        if str(element) == str(article):
            return True
    return False

def get_integer(order):
    '''
    checks if a value is an integer
    Args:
        order(str): order of integers
    Returns:
        int: the integer entered by the user
    '''
    while True:
        v = input(f'Enter your{order}integer: ')
        try:
            v = int(v)
            return v
        except ValueError:
            print('Not an integer!')
def get_integers():
    '''
    checks if 2 numbers are integers, if they are it prints them
    Args:
        none
    Returns:
        prints either not integers or the 2 integers
    '''
    v1 = get_integer(' first ')
    v2 = get_integer('second')
    return v1, v2

def get_random():

    '''
    gets a random number between 2 integers
    Args:
        none
    Returns:
        int: a random number between the 2 integers
    '''
    r1 = get_integer(' first ')
    r2 = get_integer(' second ')

    if r1 > r2:
        return random.randint(r2, r1)
    else:
        return random.randint(r1, r2)
    

def count_vowels(s):
    '''
    counts the amount of vowels in a word
    Args:
        s(str): the string we are checking for vowels
    Returns:
        int: the amt of vowels in the word
    '''
    total_vowels = 0

    for char in s:
        if char in ['a', 'e', 'i', 'o', 'u']:
            total_vowels += 1
    return total_vowels

def reverse_string(string):
    '''
    reverses a string 
    Args:
        string(str): the string being reversed
    Returns:
        str: the string reversed
    '''
    return string [:: -1]

def is_palindrome(string):
    '''
    checks if a string is a palendrome
    Args:
        str(str): the string being checked if its a palindrome
    Returns:
        bool: if the string is a palendrome
    '''
    return reverse_string(string) == string

def get_initials(fullname): 
    '''
    Takes a name and returns the initials
    Args:
        fullname(str): persons name for the initals
    Returns:
        str: the persons initals
    '''
    names = fullname.split(' ')
    initials = ''

    for name in names:
        initials += name[0]
    return initials.upper()

def replace_character(replace, old, new):
    '''
    replaces a character in a word with a new character
    Args:
        replace(str): the string that the letters are going to be replaced in
        old(str): the letter being replaced
        new(str): the new letter that will replace old
    Returns:
        str:the new string with letters replaced
    '''
    new_string = ''
    for char in replace:
        if char == old:
            new_string += new
        else:
            new_string += char
    return new_string


 
def main():
    '''
    Runs all funtions
    Args:
        none
    '''
    while True:
        option = input('''
                       What would you like to do? 
                       1.Sing a song
                       2.add 2 integers, 
                       3.print a list, 
                       4.check if an item is in a list, 
                       5. Check if a value is an integer, 
                       6.Generate a random number between 2 integers, 
                       7.Count the vowels in a word, 
                       8.Reverse a string, 
                       9.Check if a string is a palindrome, 
                       10.Create intials for a name, 
                       11. Replace characters in a word
                       ''')
   
        if option == '1':
            
            SingSong(1)
            chorus(0)
            SingSong(1)
            chorus(1)
        elif option == '2':
            print('Lets check if 2 values are integers')
            n1, n2 = get_integers()
            add(n1, n2)
        elif option == '3':
            list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            print_list(list1)
        elif option == '4':
            list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            article = input("Enter an element to check if it is in the list: ")
    
            print(in_list(list1, article))
        elif option == '5':
            print(get_integer(" "))
        elif option == '6':
            print('Lets generate a random number between 2 integers')
            print(get_random())
        elif option == '7':
            s=input('enter a word for vowels to be counted')
            print(count_vowels(s))
        elif option == '8':
            string = input('Enter a sting to reverse:')
            print(reverse_string(string))
        elif option =='9':
            str = input('Enter a string to check if its a palindrome:')
            print(is_palindrome(str))
        elif option == '10':
            name = input('Whats your full name?')
            print(get_initials(name))
        elif option == '11':
            replace = input('What word would you like to replace characters for?')
            old = input('what character in the word would you like to replace?')
            new = input('what character would like to replace this with?')
            print(replace_character(replace, old, new))
    
main()

