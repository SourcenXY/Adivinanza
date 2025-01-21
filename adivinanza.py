import random

intervale = range(1, 11)
solution = random.choice(intervale)


print('Hi Chocho, Im going to think in a number from 1 to 10')
number = int(input('Write the number: \n'))

while(number != solution):
    if(number > solution):
        print('The number entered is greater, choose a smaller number')
        number = int(input('Write the number: \n'))
    else:
        print('The number entered is less, choose a bigger number')
        number = int(input('Write the number: \n'))
if(number == solution):
    print('You find the number, congratulations!')

