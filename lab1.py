'''
This is a lab on list comprehensions
1.    Generate a list of all of the numbers from 1-1000 that are divisible by 7
2.    Generate a list of all of the numbers from 1-1000 that have the digit 3 in them
3.    Remove all of the vowels in a string (can assume y is not a vowel)
4.    Find all of the words in a string that are less than 4 letters
5.    Use a dictionary comprehension that maps each each word in a sentence to its length.

Additional Challenges:

    Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

'''

# generate a list of all the numbers from 1-1000 that are divisible by 7

'''
new_list = []
def divide_7():
    for i in range(1, 1001):
        if i % 7 == 0:
            new_list.append(i)
    
    return new_list

# print(divide_7())
'''

new_list = []
def divide_7():
    new_list = [i for i in range(1, 1001) if i % 7 == 0]
    
    return new_list

# generate a list of all the numbers from 1-1000 that have the digit 3 in them

'''
list2 = []
def digit3():
    for i in range(1,1001):
        if '3' in str(i):
            list2.append(i)
    
    return list2

# print(digit3())
'''

list2 = []
def digit3():
    list2 = [i for i in range(1, 1001) if '3' in str(i)]
    
    return list2

# remove all of the vowels in a string (assume y is not a vowel)

'''
vowels = ['a', 'e', 'i', 'o', 'u']
def remove_vowel(string):
    new_string = ''
    for i in string:
        if i not in vowels:
            new_string += i
    
    return new_string

# print(remove_vowel('hello'))
'''

vowels = []
def remove_vowel(string):
    vowels = [i for i in string if i not in 'aeiou']
    return ''.join(vowels)



# find all of the words in a string that are less than 4 letters

'''
small_words = []

def small_word(string):
    for i in string.split():
        if len(i) < 4:
            small_words.append(i)
    
    return small_words


# print(small_word('hello my name is valiant and i am a student'))
'''

small_words = []
def small_word(string):
    small_words = [i for i in string.split() if len(i) < 4]
    return small_words

# use a dictionary comprehension that maps each word in a sentence to its length

'''
empty_dict = {}

def length_word(string):
    for i in string.split():
        empty_dict[i] = len(i)
        empty_dict.update(empty_dict)

    return empty_dict

# print(length_word('hello my name is valiant and i am a student'))
'''

empty_dict = {}
def length_word(string):
    empty_dict = {i: len(i) for i in string.split()}
    return empty_dict
