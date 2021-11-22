"""
TODO: Read information here
https://www.geeksforgeeks.org/turtle-programming-python/
"""

"""
STEP 1
TODO: Import the relevant library and initialize it
"""


"""
STEP 2
TODO: set the turtle properties to not leave a line behind
        and change the color to not be black
"""
def set_properties():
   pass

def get_command():
    command = input("What must I do next?:")
    return command

"""
STEP 3
TODO: implement the code to know which function to call
        and pass the number of steps to the reLevant function
"""
def handle_command(command):

    ### Changing the code between here ###
    steps = 0
    if " " in command: action, steps = command.split()
    else: action = command
    if (str(steps).isdigit()): steps = int(steps)
    action = str(action).lower()
    ### And here, is not recommended :-) ###

    if action == "exit": return False
    

    return True

'''TODO: Do not touch anything below here'''
def main():
    set_properties()
    run = True
    while(run):
        command = get_command()
        run = handle_command(command)

if __name__ == "__main__":
    main()
