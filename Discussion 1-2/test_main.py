#!/usr/bin/env python3
# Discussion 01.2: Using GitHub Classrooms

# Import Modules
import main as app, random

# Global Variable for input() of Values
value_input = []

# Global Variable for Student Actual Result of the Program
value_actual = []

def mock_input(prompt):
    "Mock the Input Process"
    global value_input, value_actual
    value_actual.append(prompt)
    return str(value_input.pop(0))

def run_main_program():
    "Run the main() program and capture the results"
    global value_input, value_actual

    # Overwrite the input() function
    app.input = mock_input

    # Overwrite the print() function with 1 argument in the print()
    app.print = lambda arg1 : value_actual.extend([arg1])

    # Execute the main() function from the code
    app.main()

    return value_actual

def test_case1():
    "Test for IO Case 1"

    # Setup IO Variables
    global value_input, value_actual
    value_input = ["1", "1"]
    value_actual = []
    value_expected = [
        "> ", "> ", # Output from input() prompt text
        "1 + 1 = 2" # Output from print()
    ]

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected

def test_case2():
    "Test for IO Case 2"

    # Setup IO Variables
    global value_input, value_actual
    value_input = ["4", "7"]
    value_actual = []
    value_expected = ["> ", "> ", "4 + 7 = 11"]

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected

def test_case3():
    "Test for IO Case 3"

    # Setup IO Variables
    global value_input, value_actual
    value_input = ["22", "20"]
    value_actual = []
    value_expected = ["> ", "> ", "22 + 20 = 42"]

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected

def test_numbers():
    "Test for Random Numerical Input"

    # Random Numerical Value for Testing
    x = random.randint(1,1000)
    y = random.randint(1,1000)
    a = x + y
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = [str(x), str(y)]
    value_actual = []
    value_expected = ["> ", "> ", " + ".join(value_input)+" = "+str(a)]

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected
