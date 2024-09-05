#!/usr/bin/env python3
# Discussion 01.1: Using GitHub Classrooms

# Import Modules
import main as app, random, string

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

    # Overwrite the print() function with 2 arguments in the print()
    app.print = lambda arg1, arg2 : value_actual.extend([arg1, arg2])

    # Execute the main() function from the code
    app.main()

    return value_actual

def test_case1():
    "Test for IO Case 1"

    # Setup IO Variables
    global value_input, value_actual
    value_input = ["Student"]
    value_actual = []
    value_expected = [
        "> ",              # Output from input() prompt text
        "Hello", "Student" # Output from print()
    ]

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected

def test_case2():
    "Test for IO Case 2"

    # Setup IO Variables
    global value_input, value_actual
    value_input = ["42"]
    value_actual = []
    value_expected = [
        "> ",         # Output from input() prompt text
        "Hello", "42" # Output from print() statement
    ]

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected

def test_numbers():
    "Test for Random Numerical Input"

    # Random Numerical Value for Testing
    x = random.randint(1,1000)
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = [str(x)]
    value_actual = []
    value_expected = [
        "> ",           # Output from input() prompt text
        "Hello", str(x) # Output from print()
    ]

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected


def test_strings():
    "Test for Random String Input"

    # Random String Value for Testing
    x = random.choice(string.ascii_letters)
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = [str(x)]
    value_actual = []
    value_expected = [
        "> ",           # Output from input() prompt text
        "Hello", str(x) # Output from print()
    ]

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected
