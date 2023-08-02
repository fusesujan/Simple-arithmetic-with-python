# Q.Write Python functions for basic mathematical operations such as addition, subtraction, and multiplication.
# These functions should take two numeric inputs and return the result of the corresponding operation.

# defining a function that can do all the operations
def SimpleArithmetic(params1, params2):
    print("Given numbers are", params1, 'and', params2)

    print("Tell me which operation you wanna perform ? (-),(+),(*), (/)")
    opr = input()
    if (opr == "-"):
        # user may want to minus the earlier number
        print("Want to alter the numbers ? y/n")
        alt1 = input()
        if alt1 == 'y' or alt1 == "Y":
            output = params2 - params1
        else:
            output = params1 - params2
    elif (opr == "+"):
        output = params1 + params2
    elif (opr == "*"):
        output = params1 * params2
    elif (opr == "/"):
        # user may want to divide the earlier number
        print("Want to alter the numbers ? y/n")
        alt2 = input()
        if alt2 == 'y' or alt2 == "Y":
            output = params2 / params1
        else:
            output = params1 / params2
    else:
        return None

    return output


print("Please enter any two numbers")
x = int(input())
y = int(input())

FinalResult = SimpleArithmetic(x, y)

if (FinalResult != 0):
    print("Your Final output is", FinalResult)
else:
    print("Be sure you enter one of the available operations")
