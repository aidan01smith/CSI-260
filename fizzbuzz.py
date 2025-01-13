# for loop that goes from 1-100
# define a function that gives us the remainder (using modulo)
# if statement to check if divisible by 3 or 5
# nest together the if statements to account for fizzbuzz

# what I made
'''
for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print('fizzbuzz')
        continue
    elif fizzbuzz % 3 == 0:
        print('fizz')
        continue
    elif fizzbuzz % 5 == 0:
        print('buzz')
    else:
        print(fizzbuzz)
'''

# in-class example

def remainder(n, divisor):
    return n % divisor

for i in range(1, 101):
    if remainder(i, 15) == 0:
        print(i, 'fizzbuzz')
    elif remainder(i, 3) == 0:
        print(i, 'fizz')
    elif remainder(i, 5) == 0:
        print(i, 'buzz')
