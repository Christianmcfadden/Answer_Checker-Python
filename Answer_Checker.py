"""
Version 10 (Adding Additional features)



**There is a problem with the form of the variable solution 
needs to be a int and not a double**
"""

def askProblem():
    guess = input("Please enter your equation (Separate it by spaces): ")
    return guess

"""
if number3 == solution:
        print("You got it correct! ")
        print(number3 , solution)
        correct + 1
        return correct
    elif number3 != solution:
        print("Sorry that is incorrect Try again.")
        while tries > 2:
            number3 = int(input("What is your answer? "))
"""
    
def askResponse(number1, opperation, number2, solution):
    print("---------Quiz----------")
    print(" " + str(number1) + " " + str(opperation) + " " + str(number2) + " = ?")
    number3 = input("What is your answer? ")
    tries = 1
    correct = 0
    if str(number3) == solution:
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            correct += 1
            return correct, tries

    while str(number3) != solution:
        print("You Got it wrong, Try again") 
        number3 = askAnswer() 
        if number3 != solution:
            print("You ran out of tries")
            print("Your incorrect answer was: ", number3)
            print("The Correct answer is: ", solution)
            number3 = solution
            tries += 1
            return correct, tries
        if str(number3) == solution.round():
            print("Correct Answer: ", solution)
            print("You got it Correct! ")
            correct += 1
            tries += 1
            return correct, tries

def displayBank(displayMem):
    option = input("Display?")
    if option == "1":
        print()
        displayMem.remove(displayMem[0])
        counter = 1
        for i in displayMem:
            print(str(counter) + ". " + i + " = ?")
            counter += 1
    elif option == "2":
            print("Problems Display Skipped.")
    
def askAnswer():
    number3 = int(input("What your answer: "))
    return number3

"""
def displayBank(displayMem):
    displayMem.remove(displayMem[0])
    counter = 1
    for i in displayMem:
        print(str(counter) + ". " + i + " = ?")
        counter += 1
"""

def getSolutionAdd(number1, number2):
    solution = int(number1) + int(number2)
    return solution

def storeAdd(number1, number2, memory, op, displayMem):
    print()
    solution = getSolutionAdd(number1, number2)
    store = str(number1) +  " " + op + " " + str(number2) + " " + str(solution)
    print(store)
    memory.append(store)
    displayStore = str(number1) +  " " + op + " " + str(number2)
    print(displayStore)
    displayMem.append(displayStore)
    return memory, displayMem

def getSolutionSubtract(number1, number2):
    solution = int(number1) - int(number2)
    return solution

def storeSubtract(number1, number2, memory, op, displayMem):
    print()
    solution = getSolutionSubtract(number1, number2)
    store = str(number1) +  " " + op + " " + str(number2) + " " + str(solution)
    print(store)
    memory.append(store)
    displayStore = str(number1) +  " " + op + " " + str(number2)
    print(displayStore)
    displayMem.append(displayStore)
    return memory, displayMem

def getSolutionMulti(number1, number2):
    solution = int(number1) * int(number2)
    return solution

def storeMulti(number1, number2, memory, op, displayMem):
    print()
    solution = getSolutionMulti(number1, number2)
    store = str(number1) +  " " + op + " " + str(number2) + " " + str(solution)
    print(store)
    memory.append(store)
    displayStore = str(number1) +  " " + op + " " + str(number2)
    print(displayStore)
    displayMem.append(displayStore)
    return memory, displayMem

def getSolutionDivide(number1, number2):
    solution = int(number1) / int(number2)
    return solution

def storeDivide(number1, number2, memory, op, displayMem):
    print()
    solution = getSolutionDivide(number1, number2)
    store = str(number1) +  " " + op + " " + str(number2) + " " + str(solution)
    print(store)
    memory.append(store)
    displayStore = str(number1) +  " " + op + " " + str(number2)
    print(displayStore)
    displayMem.append(displayStore)
    return memory, displayMem

def checkOperation(number1, number2, opperation, memory, displayMem):
    print()
    if opperation == "+":
        op = opperation
        memory, displayMem = storeAdd(number1, number2, memory, op, displayMem)
        return memory, displayMem, op

    if opperation == "-":
        op = opperation
        memory, tries = storeSubtract(number1, number2, memory, op, displayMem)
        return memory, tries, op

    if opperation == "*":
        op = opperation
        memory, tries = storeMulti(number1, number2, memory, op, displayMem)
        return memory, tries, op

    if opperation == "/":
        op = opperation
        memory, tries = storeDivide(number1, number2, memory, op, displayMem)
        return memory, tries, op

def main(memory, displayMem):
    print()
    memory = [""]
    displayMem = [""]
    howMany = int(input("how many problems would you like to check: "))
    for i in range(0, howMany):
        equation = askProblem()
        equation = equation.split(" ")
        number1 = equation[0]
        opperation = equation[1]
        number2 = equation[2]
        memory, displayMem, op = checkOperation(number1, number2, opperation, memory, displayMem)
        ## Add if user wants to see the memory of problems entered
    displayBank(displayMem)
    print("what oh its been done before")
    print(memory)
    
"""
pass back variables mem ans displaymem
"""
def display(memory):
    for i in memory:
        if i == "":
            continue
        equation = i
        equation = equation.split(" ")
        print(equation)
        number1 = equation[0]
        opperation = equation[1]
        number2 = equation[2]
        solution = equation[3]
        correct, tries = askResponse(number1, opperation, number2, solution)
        print(correct, tries)

def bankMenu():
    print("")
    print("------------MENU------------")
    print("Welcome to answer checker")
    print("1. Enter problems")
    print("2. display problems")
    option = int(input("Choose an option(1 or 2): "))
    if option == 1:
        memory = main(memory)
        
    elif option == 2:
        display(memory)
        print()
    else:
        print("invalid input")
        new()

def new():
    memory = [""]
    memory = bankMenu()
main()