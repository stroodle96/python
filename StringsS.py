# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 09:22:59 2018

@author: John Stewart

Strings


"""
s = 'a\nb\tc'

print(s)



#%%

len(s)


#%%
"""
Python also has a triple-quoted string literal format, sometimes called a block string,
that is a syntactic convenience for coding multiline text data.

"""
mantra = """Always look
... on the bright
... side of life."""


print(mantra)
#%%

"""Concatenating Strings """

len('abc1') 
                    # Length: number of items

print('abc' + 'def')
                             # Concatenation: a new string
print('Ni!' * 4)                       # Repetition: like "Ni!" + "Ni!" + ...

#%%

myjob = "hacker"
for c in myjob: print(c, end=' ') # Step through items, print each (3.X form)

#%%

""" Boolean """

"k" in myjob # Found

#%%

"z" in myjob # Not found

#%%

'spam' in 'abcspamdef' # Substring search, no position returned
#%%

"""
Indexing 

"""

#slices out leters of a string
S = 'spam'
S[0], S[-1]

#%%
#
S[1:3], S[1:]      # Slicing: extract a section

#%%

""" X[1:10:2] will fetch every other item in X from offsets 1–9; that is, it will
collect the items at offsets 1, 3, 5, 7, and 9. """

S = 'abcdefghijklmnop'
print(S[1:10:2]) # Skipping items

print(S[::2])
#%%

#reverses a string
S = 'hello'
print(S[::-1]) 
 #%%
 
"""   With a negative stride, the meanings of the first two bounds are essentially reversed.
That is, S[5:1:−1] fetches the items from 2 to 5, in reverse order (the result
contains items from offsets 5, 4, 3, and 2)       """
    


#%%
S = 'abcedfg'
S[5:1:-1] # Bounds roles differ

 

#%%

import nltk

nltk.download()

#%%

"""  String Conversions
"""


"42" + 1
"""TypeError: Can't convert 'int' object to str implicitly"""

#%%

"""This is by design: because + can mean both addition and concatenation, the choice of
conversion would be ambiguous. Instead, Python treats this as an error. In Python,
magic is generally omitted if it will make your life more complex.
What to do, then, if your script obtains a number as a text string from a file or user
interface? The trick is that you need to employ conversion tools before you can treat a
string like a number, or vice versa. For instance:"""


int("42"), str(42) # Convert from/to string


#%%
# This program concatenates strings.

def main():
    name = 'Carmen'
    print('The name is', name)
    name = name + ' Brown'
    print('Now the name is', name)

# Call the main function.
main()


#%%

"""
Changing Strings 

"""

""" immutable  means
that you cannot change a string in place—for instance, by assigning to an index:

"""    

S = 'spam'
S[0] = 'x' # Raises an error!

""" 
TypeError: 'str' object does not support item assignment
"""

#%%

"""How to modify text information in Python, to change a string?   To change a string, you generally
need to build and assign a new string using tools such as concatenation and slicing,
and then, if desired, assign the result back to the string’s original name:  """

S = S + 'SPAM!' # To change a string, make a new one


S = S[:4] + 'Burger' + S[-1]
S


#%%

S = 'splot'
S = S.replace('pl', 'pamal')   # replace pl
S

#%%

"""
it’s also possible to build up new text values with string formatting expressions.
Both of the following substitute objects into a string, in a sense converting the objects
to strings and changing the original string according to a format specification:
    
"""
'That is %d %s bird!' % (1, 'dead')  # Format expression: all Pythons

#%%                        

'That is {0} {1} bird!'.format(1, 'dead') # Format method in 2.6, 2.7, 3.X

         
         
#%%

"""
Slicing strings

"""

S = 'spammy'
S = S[:3] + 'xx' + S[5:] # Slice sections from S
S



#%%
""" to replace a substring, you can also use the string replace method
instead:
    
"""
S = 'spammy'
S = S.replace('mm', 'xx') # Replace all mm with xx in S
S

#%%
"""

The replace method can also takes as arguments an
original substring (of any length) and the string (of any length) to replace it with, and
performs a global search and replace:
    
"""
'aa$bb$cc$dd'.replace('$', 'SPAM')


#%%
"""
If you need to replace one fixed-size string that can occur at any offset, you can do a
replacement again, or search for the substring with the string find method and then
slice:

"""
S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM') # Search for position
where # Occurs at offset 4




#%%

"""
The find method returns the offset where the substring appears (by default, 
searching from the front), or −1 if it is not found. 

it’s a substring search operation
find returns the position of a located substring.

Another option is to use replace with a third argument to limit it to a single substitution:
"""
S = 'xxxxSPAMxxxxSPAMxxxx'
S.replace('SPAM', 'EGGS') # Replace all
#%%

S.replace('SPAM', 'EGGS', 1) # Replace one

#%%

"""
Parsing Text
"""

line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]

print(col1)

print(col3)
#%%

"""

Here, the columns of data appear at fixed offsets and so may be sliced out of the original
string. This technique passes for parsing, as long as the components of your data have
fixed positions. If instead some sort of delimiter separates the data, you can pull out its
components by splitting. 
    
"""
    
line = 'aaa bbb ccc'
cols = line.split()
cols


#%%

line = 'bob,hacker,40'
line.split(',')

#%%
"""

Delimiters can be longer than a single character, too:
"""    
    
line = "i'mSPAMaSPAMlumberjack"
line.split("SPAM")




#%%
""""
EXAMPLE CODE

"""



#%%

# This program counts the number of times
# the letter T (uppercase or lowercase)
# appears in a string.

def main():
    # Create a variable to use to hold the count.
    # The variable must start with 0.
    count = 0
    
    # Get a string from the user.
    my_string = input('Enter a sentence: ')

    # Count the Ts.
    for ch in my_string:
        if ch == 'T' or ch  == 't':
            count += 1

    # Print the result.
    print('The letter T appears', count, 'times.')

# Call the main function.
main()





#%%

"""
Save this as login.py in your root folder 

"""

# The get_login_name function accepts a first name,
# last name, and ID number as arguments. It returns
# a system login name.

def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name.
    # If the name is less than 3 characters, the
    # slice will return the entire first name.
    set1 = first[0 : 3]

    # Get the first three letters of the last name.
    # If the name is less than 3 characters, the
    # slice will return the entire last name.
    set2 = last[0 : 3]

    # Get the last three characters of the student ID.
    # If the ID number is less than 3 characters, the
    # slice will return the entire ID number.
    set3 = idnumber[-3 :]

    # Put the sets of characters together.
    login_name = set1 + set2 + set3

    # Return the login name.
    return login_name

# The valid_password function accepts a password as
# an argument and returns either true or false to
# indicate whether the password is valid. A valid
# password must be at least 7 characters in length,
# have at least one uppercase letter, one lowercase
# letter, and one digit.

def valid_password(password):
    # Set the Boolean variables to false.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Begin the validation. Start by testing the
    # password's length.
    if len(password) >= 7:
        correct_length = True

        # Test each character and set the
        # appropriate flag when a required
        # character is found.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    # Determine whether all of the requirements
    # are met. If they are, set is_valid to true.
    # Otherwise, set is_valid to false.
    if correct_length and has_uppercase and \
       has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    # Return the is_valid variable.
    return is_valid


#%%

#%%

"""
Can store the previous file as a module in your root directory and
import it. 

"""

# This program gets the user's first name, last name, and
# student ID number. Using this data it generates a
# system login name.

import login

def main():
    # Get the user's first name, last name, and ID number.
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')

    # Get the login name.
    print('Your system login name is:')
    print(login.get_login_name(first, last, idnumber))
    
# Call the main function.
main()





#%%

# This program demonstrates the repetition operator.

def main():
    # Print nine rows increasing in length.
    for count in range(1, 10):
        print('Z' * count)

    # Print nine rows decreasing in length.
    for count in range(8, 0, -1):
        print('Z' * count)

# Call the main function.
main()



#%%

# This program calls the split method, using the
# '/' character as a separator.

def main():
    # Create a string with a date.
    date_string = '11/26/2012'

    # Split the date.
    date_list = date_string.split('/')

    # Display each piece of the date.
    print('Month:', date_list[0])
    print('Day:', date_list[1])
    print('Year:', date_list[2])

# Call the main function.
main()

#%%

# This program demonstrates the split method.

def main():
   # Create a string with multiple words.
   my_string = 'One two three four'

   # Split the string.
   word_list = my_string.split()

   # Print the list of words.
   print(word_list)

# Call the main function.
main()

#%%
"""
String Methods

"""

# This program demonstrates several string testing methods.

def main():
    # Get a string from the user.
    user_string = input('Enter a string: ')

    print('This is what I found about that string:')
    
    # Test the string.
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits.')
    if user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only whitespace characters.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')

# Call the main function.
main();

    
    #%%
    
    
# This program gets a password from the user and
# validates it.

import login

def main():
    # Get a password from the user.
    password = input('Enter your password: ')

    # Validate the password.
    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print('That is a valid password.')

# Call the main function.
main()
#%%
# Programming Exercise 8-1

def main():
    # Receive user input
    full_name = input ('Enter your full name: ')

    # Split according to spaces
    name = full_name.split()

    # The first character of each name is an initial
    for string in name:
        print(string[0].upper(), sep='', end='')
        print('.', sep=' ', end='')

# Call the main function.
main()
#%%

# This program sums the digits in a string

def main():
    # Get a string of numbers as input from the user.
    number_string = input('Enter a sequence of digits ' \
                          'with nothing separating them: ')

    # Call string_total method, and store the total.
    total = string_total(number_string)

    # Display the total.
    print('The total of the digits in the ' \
          'string you entered is', total)


# The string_total method receives a string and returns
# the total of all the digits contained in the string.
# The method assumes that the string does not contain
# non-digit characters
def string_total(string):
    # Local variables
    total = 0
    number = 0

    # Step through each character in the string.
    for i in range(len(string)):
        # Convert the character to an integer.
        number = int(string[i])
        # Add the value to the running total.
        total += number

    # Return the total
    return total

# Call the main function.
main()



#%%

"""
ACTIVITY 1
Write a program that accepts a string as an argument and returns the number of 
vowels and consonants that the string contains.  The user should be prompted for the 
string and the output should display the number of vowels and consonants the string
contains. 

"""
def main():
    # Create a variable and initialize it and imports the library re.
    import re
    count_c = 0
    count_v = 0
    good_string = 1
    
    # Get the string from the user and assign it to the variable my_string
    my_string = input('Enter ONE word to count its consonants and vowels:\n >> ')
    
    #Check my_string for vowels and adds 1 to the count if found.
    for v in my_string:
        if v == 'A' or v  == 'a':
            count_v += 1
    for v in my_string:
        if v == 'E' or v  == 'e':
            count_v += 1
    for v in my_string:
        if v == 'I' or v  == 'i':
            count_v += 1
    for v in my_string:
        if v == 'O' or v  == 'o':
            count_v += 1
    for v in my_string:
        if v == 'U' or v  == 'u':
            count_v += 1
     
    #Subtract the amount of vowels to find the amount of consonants in the string.
    count_c = len(my_string) - count_v
   
    # Print the results.
    print('There is ', count_v, ' Vowel(s) and ', count_c, ' Consonants in that string.!!')

# returns to the main function.
main()
"""
OUTPUT

Enter ONE word to count its consonants and vowels:
 >> Mailman
There is  3  Vowel(s) and  4  Consonants in that string.!!



Enter ONE word to count its consonants and vowels:
 >> Example
There is  3  Vowel(s) and  4  Consonants in that string.!!



"""
#%%
"""
ACTIVITY 2

Create a program that tests whether a word is a Palindrome.  That is a word
that is the same forward and backward in spelling.

EXAMPLES: 

rotor

rats live on no evil star

A man a plan a canal Panama


"""


#%%
def PalindromeChk(WordInput):
    Flag = True
    Letters = list(WordInput)
    
    "Checks the first position letter against last position.  Then 2nd postiion against 2nd to last... ect"
    for l in Letters:
        if l == Letters[-1]:
            Letters.pop(-1)
        else:
            Flag = False
            break
    "Prints results of test"
    if Flag == True:
        print("Your word is a Palindrome!")
    elif Flag == False:
        print("That word is not a Palindrome!")

    "Main Function"
def main():
    
    WordInput = input("Enter a word to check to see if it is a Palindrome\n>>")    
    PalindromeChk(WordInput=WordInput)

main()

"""OUTPUT
Enter a word to check to see if it is a Palindrome
>>racecar
Your word is a Palindrome!

Enter a word to check to see if it is a Palindrome
>>wow
Your word is a Palindrome!

Enter a word to check to see if it is a Palindrome
>>Test
That word is not a Palindrome!

"""

#%%
"""


