'''
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

Sources used:
https://www.w3resource.com/python-exercises/math/python-math-exercise-6.php
https://www.geeksforgeeks.org/python-program-to-find-volume-surface-area-and-space-diagonal-of-a-cuboid/
https://www.geeksforgeeks.org/self-in-python-class/
https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
'''
import math 

#Creates a class for the calculator
class Calculator:
    def __init__(self):
        self.view_mode = 'D'

    #Displays the options
    def menu_select(self):
        print("A/V calculator Menu")
        print("(Level 0)")
        print("Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.")
        print("Enter V/v to change the calculated view or D/d for default view.")
        print("(Level 1)")
        print("1. First Area/Volume calculation")
        print("2. Second Area/Volume calculation")
        print("3. Third Area/Volume calculation")
        print("4. Fourth Area/Volume calculation")
        print("5. Fifth Area/Volume calculation")

    #Change the view mode to verbose or default (the default is well... default if the input is invalid)
    def view_mode_select(self):
        user_input = input("Enter V/v for verbose view or D/d for default view: ").strip().upper()
        if user_input == 'V':
            self.view_mode = 'V'
        elif user_input == 'D':
            self.view_mode = 'D'
        else:
            print("Default view mode selected.")

    #Runs the main program loop
    def run(self):
        while True:
            self.menu_select()
            user_input = input("Input your choice: ").strip().lower()

            if user_input == 'q':
                break
            elif user_input == 'v':
                self.view_mode_select()
            elif user_input == 'd':
                self.view_mode = 'D'
            elif user_input in ['1', '2', '3', '4', '5']:
                calculation_choice = int(user_input)
                self.calculate(calculation_choice)
            else:
                print("ERORR: Please select an option.")
    
    #Performs the selected calculation based on what the user selects
    def calculate(self, choice):
        if choice == 1:
            a = float(input("Input value for 'a': "))
            b = float(input("Input value for 'b': "))
            result = calculate_area_volume_1(a, b)
            self.calculated_result(1, a, b, result)
        elif choice == 2:
            a = float(input("Input value for 'a': "))
            b = float(input("Input value for 'b': "))
            result = calculate_area_volume_2(a, b)
            self.calculated_result(2, a, b, result)
        elif choice == 3:
            a = float(input("Input value for 'a': "))
            b = float(input("Input value for 'b': "))
            result = calculate_area_volume_3(a, b)
            self.calculated_result(3, a, b, result)
        elif choice == 4:
            a = float(input("Input value for 'a': "))
            b = float(input("Input value for 'b': "))
            result = calculate_area_volume_4(a, b)
            self.calculated_result(4, a, b, result)
        elif choice == 5:
            a = float(input("Input value for 'a': "))
            b = float(input("Input value for 'b': "))
            result = calculate_area_volume_5(a, b)
            self.calculated_result(5, a, b, result)
    
    #Displays the calculated result based on the selected view mode (verbose or default)
    def calculated_result(self, choice, a, b, result):
        if self.view_mode == 'V':
            equation = ""
            if choice == 1:
                equation = f"Area = {a} * {b}"
            elif choice == 2:
                equation = f"Volume = {a} * {a} * {a}"
            elif choice == 3:
                equation = f"Area = π * {a}^2"
            elif choice == 4:
                equation = f"Volume = (4/3) * π * {a}^3"
            elif choice == 5:
                equation = f"Area = 0.5 * {a} * {b}"
            print(f"Calculation: {equation} = {result}")
        elif self.view_mode == 'D':
            print(f"Calculation: {result}")


#The calculations are defined here
def calculate_area_volume_1(a, b):
    #Equation for the first calculation: Area of a rectangle
    return a * b

def calculate_area_volume_2(a, b):
    #Equation for the second calculation: Volume of a cube
    return a * a * a

def calculate_area_volume_3(a, b):
    #Equation for the third calculation: Area of a circle
    return math.pi * a * a

def calculate_area_volume_4(a, b):
    #Equation for the fourth calculation: Volume of a sphere
    return (4 / 3) * math.pi * a * a * a

def calculate_area_volume_5(a, b):
    #Equation for the fifth calculation: Area of a triangle
    return 0.5 * a * b

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
