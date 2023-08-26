
from calculate import calcOperation

def getNumbers():
    print(f"I can Add(+) Subtract(-) Divide(/) or Multiply(*) any two numbers.")
    firstNumber = input("What is the first number: ")
    while valNumbers(firstNumber) != True:
        firstNumber = input("Please input first number again: ")

    secondNumber = input("What is the second number: ")
    while valNumbers(secondNumber) != True:
        secondNumber = input("Please input second number again: ")

    numOperation = input("What operation do you want [+-/*]: ")
    while valOperation(numOperation) != True:
        numOperation = input("Please enter valid operation [+-/*]: ")
    
    calcOperation(firstNumber, secondNumber, numOperation)


def valNumbers(numInput):
    if numInput.isnumeric():
        return(True)
    else:
        print("This is not a numeric value!")
        return(False)


def valOperation(OpInput):
    numOp = ['+', '-', '/', '*']
    if OpInput in numOp:
        return(True)
    else:
        print("This is not a valid operater!")
        return(False)





