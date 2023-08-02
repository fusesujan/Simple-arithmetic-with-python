# Q.Write Python functions for basic mathematical operations such as addition, subtraction, and multiplication.
# These functions should take two numeric inputs and return the result of the corresponding operation.

def SimpleArithmetic(params1, params2):
    print("Given numbers are", params1, 'and', params2)

    print("Tell me which operation you wanna perform ? (-),(+),(*)")
    opr = input()
    result = 0
    if (opr == "-"):
        output = params1 - params2
    elif (opr == "+"):
        output = params1 + params2
    elif (opr == "*"):
        output = params1 * params2
    else:
        return None

    return output


print("Please enter any two numbers")
x = int(input())
y = int(input())

FinalResult = SimpleArithmetic(x, y)

if FinalResult:
    print("Your Final output is", FinalResult)
