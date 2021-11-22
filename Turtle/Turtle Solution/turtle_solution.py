"""
TODO: Read information here
https://www.geeksforgeeks.org/turtle-programming-python/
"""

"""
STEP 1
TODO: Import the relevant library and initialize it
"""
import turtle
robot = turtle.Turtle()

"""
STEP 2
TODO: set the turtle properties to not leave a line behind
        and change the color to not be black
"""
def set_properties():
   robot.penup()
   robot.color("red")

def get_command():
    command = input("What must I do next?:")
    return command

"""
STEP 3
TODO: implement the code to know which function to call
        and pass the number of steps to the reLevant function
"""
def handle_command(command):

    steps = 0
    if " " in command: action, steps = command.split()
    else: action = command
    if (str(steps).isdigit()): steps = int(steps)
    action = str(action).lower()

    if action == "exit": return False
    elif action == "forward": robot.forward(steps)
    elif action == "back": robot.back(steps)
    elif action == "right": robot.right(90)
    elif action == "left": robot.left(90)

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
