
def is_valid(numbers):
    """goes through a string, converts it into a list and checks for non-numeric values
    using a lambda function named is_numeric"""

    is_numeric = lambda x : str.isnumeric(x)

    numbers = numbers.split(",")
    for number in numbers:
        
        if  is_numeric(number) == False:
            return False 
    
    return True

def only_two_numbers(input):
    """makes sure we get only two numbers , not just a list with any two elements"""

    if is_valid(input):
        if len(input.split(',')) == 2:
            return True
    return False

def get_input() :
    """ get user input ,check that we receive only  numbers or an off command, uses a lambda function in a 
    map function to convert a valid list into integers and store in user_input_as_numbers"""

    user_input = ""

    while (only_two_numbers(user_input) == False ):
        user_input = input(" Please enter 2 numbers seperated by a comma :\n")
        if user_input == 'off':
            return 'game over'

    user_input_as_numbers = list(map(lambda x :int(x),user_input.split(',')))

    return user_input_as_numbers

def get_operator() :
    """ receives input from user, checks that we got a valid operator
    
    """
    operator = ""
    while operator not in ['+','-','/','*']:
        operator = input("Please choose and operator : + ,- ,/ ,* :\n")

    return operator

def calculate(numbers, operator):
    """
Function tells program which lambda function to use

Args:
    :numbers: numbers is a list of two integers.
    :operator: operator is the operator to be exercised.

:Return:
    @result , the final value after numbers go through the lambda function.
    """

    if operator == '+':
        compute = lambda x, y: x + y
    elif operator == '-':
        compute = lambda x, y: x - y
    elif operator == '/':
        compute = lambda x, y: x / y
    elif operator == '*':
        compute = lambda x, y: x * y

    result = compute(numbers[0],numbers[1])

    return result


def calculator():
    """responsible mainly for checking for our off button, and calling all other functions"""


    numbers = get_input()
    if numbers =='game over':
        return False
    operator = get_operator()
    result = calculate(numbers,operator)
    print('The result is : {r}'.format(r = result))

    return True

def run():
    """ main game loop
    """

    print("Welcome friend ! lets go !")

    run = True
    while (run):
        if calculator() == True:
            continue
        else:
            run = False
            break

if __name__ == "__main__":
    run()
        
