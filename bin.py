import sys
import random

errorMessages = ["Ya like jazz?","According to all known laws of aviation, there is no way a bee should be able to fly.","Yellow, black. Yellow, black.", "The bee, of course, flies anyway.", "Barry! Breakfast is ready!", "Use the stairs. Your father paid good money for those.","You got lint on your fuzz.","Wave to us! We'll be in row 118,000.","Everybody knows, you sting someone, you die.", "Don't waste it on a squirrel. Such a hothead.", "You going to the funeral?", "Keep your hands and antennas inside the tram at all times.", "That girl was hot.\n<!> She's my cousin!\n<!> She is?\n<!> Yes, we're all cousins!", "That bee is stress-testing a new helmet technology.", "Please clear the gate. Royal Nectar Force on approach.", "They know what it's like outside the hive.", "It's just a status symbol. Bees make too much of it.", "Oh no! You're dating a human florist!", "Thinking bee. Thinking bee. Thinking bee! Thinking bee! Thinking bee! Thinking bee!", "You have got to start thinking bee, my friend. Thinking bee!", "I just hope she's bee-ish.", "Anger, jealousy, lust.", "What is wrong with you? It's a bug.", "Get out of here, you creep!", "You, sir, have crossed the wrong sword!", "You, sir, will be lunch for my iguana, Ignacio!", "All right. Take ten, everybody. Wrap it up, guys.", "I had virtually no rehearsal for that."]

def throwError():
    errorIndex = random.randint(0,len(errorMessages)-1)
    print("<!> " + errorMessages[errorIndex])
    exit()

def openFile(FIQ):# File In Question
    file = open(FIQ,"r")
    lines = []
    for x in file:# initializes lines as a list of all lines
        lines.append(x)
    for i in range(len(lines)):# gets rid of \n at the end of all lines
        if i != len(lines)-1:
            lines[i] = lines[i][:-1]
    emptyCount = 0
    for i in range(len(lines)):# gets rid of empty lines
        if lines[i] == "":
            emptyCount+=1
    for i in range(emptyCount):
        lines.remove("")
    return lines

labels = []

def extractLabels(LsIQ):# Lines in Question
    output = []
    index = 0
    for line in LsIQ:# for each line
        if line[0] != ":":
            output += [line]
            index+=1
        else:
            if line[1] != "b":
                throwError()# if label doesnt start with a b
            labels.append([line[1:],index])
    # print(labels)
    return output

operationList = ["bet", "bif", "boto", "brint", "binput", "blus", "binus", "bimes", "bivide", "bar", "batch", "betch"]# list of all operations
oneArgOpList = ["boto", "brint"]
twoArgOpList = ["bet", "bif", "binput", "blus", "binus", "bimes", "bivide", "bar", "batch", "betch"]# TODO debug command that prints all vars
expressionOpList = ["blus", "binus", "bimes", "bivide", "bar", "batch", "betch"]

def countOperations(input):# count operations in sequence of words (for parsing)
    count=0
    for word in input:# ADD if word is actually a list, ignore/continue to avoid errors
        for operation in operationList:
            if word == operation:
                count+=1
    return count

allowedFirstChars = ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "b", "\""]

def parseLine(LIQ):# Line In Question
    lastSpace=-1# scuffed but shhhhhh
    insideQuotes=-1# -1 is false, 1 is true
    words=[]
    for i in range(len(LIQ)):# for every letter in the string given
        if LIQ[i] == "\"":
            insideQuotes*=-1# flip inside quotes status
        if LIQ[i] == " " and insideQuotes == -1:# if the letter is a space and not inside quotes
            words += [LIQ[lastSpace+1:i]]# add last word to list
            lastSpace=i
    words += [LIQ[lastSpace+1:len(LIQ)]]
    for word in words: # first char check - TODO: make 0-9 only valid starts for numbers instead of all words
        allowed=False
        for char in allowedFirstChars:
            if word[0] == char:
                allowed=True
        if allowed == False:
            throwError()
    while countOperations(words) > 1:# while there are more than one ungrouped ops (the base op at the start is ok, to avoid an unnecessary layer of list nesting)
        i = 0
        while i < len(words):# while operation is above zero, group operations and their args into sublists starting from the back
            # print(words[-(i+1)])
            isOp=False
            for operation in twoArgOpList:
                if words[-(i+1)] == operation:
                    words[-(i+1)] = [words[-(i+1)],words[-i],words[-(i-1)]]
                    words.pop(-i)
                    words.pop(-(i-1))
                    isOp=True
                    break
            if isOp == True:
                break
            i+=1
    # print(words)# debug, remove later
    return words

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
numbersWithDecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "-"]

def getChar(string, index):
    return string[index]

def getValue(input):# if a number, returns that number. if a list, evaluates the function in the list via recursion
    if type(input) == str:
        if input[0] == "\"" and input[-1] == "\"":# if the input is a string literal, send it back up the chain
            return input[1:-1]# return input without quotes
        else:
            for i in range(len(variables)):# check if var, if so, return var value
                if variables[i][0] == input:
                    return variables[i][1]
            for i in range(len(input)):
                isNum = False
                for char in numbers:
                    if input[i] == char:
                        isNum = True
                if isNum == False:
                    for i in range(len(input)):
                        isFloat = False
                        for char in numbersWithDecimal:
                            if input[i] == char:
                                isFloat = True
                        if isFloat == False:
                            return 0 # because its probably a non-initialized variable
                    return float(input)
            return int(input)# return the float of the input
    elif type(input) == list: # if the input is a list, *recursion*
        match(input[0]):
            case "blus":# TODO make string - int concatenation possible
                if type(getValue(input[1])) == str:
                    return getValue(input[1]) + str(getValue(input[2])) 
                return getValue(input[1]) + getValue(input[2])
            case "binus":
                return getValue(input[1]) - getValue(input[2])
            case "bimes":
                return getValue(input[1]) * getValue(input[2])
            case "bivide":
                return getValue(input[1]) / getValue(input[2])
            case "bar":
                return getChar(getValue(input[1]),getValue(input[2]))
            case "batch":
                if getValue(input[1]) == getValue(input[2]):
                    return 1
                return 0
            case "betch":# TODO make this only take 1 arg
                for i in range(len(variables)):# checks if variable exists
                    if variables[i][0] == getValue(input[1]):# if ith variable's name is the value of arg1
                        return variables[i][1] # return variable value
                return 0 # fetching value of unassigned var returns 0
                
        throwError()# if you get to this point, the command must be invalid
    else:# if the input is a number or something, send it back up the chain.
        return input
# "a" is placeholder for a special funky character
asciiSet = "aaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaa !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~a"

variables = []# variable is stored as a list of ["name", value] e.g. [["bree", 3], ["bour", 4]]

def executeLine(LIQ):# Line In Question (parsed list)
    match(LIQ[0]):# TODO bebug command that prints all variables, labels, etc
        case "brint":
            print(getValue(LIQ[1]))
            return
        case "bet": # TODO make assigning a value to a non-b starting variable impossible
            for i in range(len(variables)):# checks if variable exists
                if variables[i][0] == getValue(LIQ[1]):# if ith variable's name is the value of arg1
                    variables[i][1] = getValue(LIQ[2]) # set variable's value to new expression
                    return
            variables.append([getValue(LIQ[1]),getValue(LIQ[2])])
            return
        case "binput": # identical to set, just with input() substituted with arg2
            if LIQ[1] == "bumb":
                for i in range(len(variables)):# checks if variable exists
                    if variables[i][0] == getValue(LIQ[2]):# if ith variable's name is the value of arg1
                        variables[i][1] = int(input(getValue(LIQ[3]))) # set variable's value to user input
                        return
                variables.append([getValue(LIQ[2]),int(input(getValue(LIQ[3])))])
            else:
                for i in range(len(variables)):# checks if variable exists
                    if variables[i][0] == getValue(LIQ[1]):# if ith variable's name is the value of arg1
                        variables[i][1] = input(getValue(LIQ[2])) # set variable's value to user input
                        return
                variables.append([getValue(LIQ[1]),input(getValue(LIQ[2]))])
            return
        case "boto":
            for label in labels: # if arg1 is in labels list
                if LIQ[1] == label[0]:
                    return label[1]-1 # SO SCUFFED i know but itll work trust - TODO make this not so fucking scuffed
            # throwError()# getting to this point indicates the label does not exist
        case "bif": # goto with a conditional
            if LIQ[1] == "bot":
                if getValue(LIQ[2]) <= 0:# if arg1 is above zero (zero is false, not zero is true)
                    for label in labels: # if arg2 is in labels list
                        if LIQ[3] == label[0]:
                            return label[1]-1
            elif getValue(LIQ[1]) > 0:# if arg1 is above zero (zero is false, not zero is true)
                for label in labels: # if arg2 is in labels list
                    if LIQ[2] == label[0]:
                        return label[1]-1
            # throwError()
        case other:
            throwError()

lines = extractLabels(openFile(sys.argv[1]))
pointerIndex = 0
while pointerIndex < len(lines):
    # print(pointerIndex)
    outputLabel = executeLine(parseLine(lines[pointerIndex]))
    if type(outputLabel) == int:
        pointerIndex = outputLabel
    pointerIndex+=1
    # print(variables) # debug