def returnRegister(reg):
    if reg == "R0":
        return "000"
    if reg == "R1":
        return "001"
    if reg == "R2":
        return "010"
    if reg == "R3":
        return "011"
    if reg == "R4":
        return "100"
    if reg == "R5":
        return "101"
    if reg == "R6":
        return "110"
R0 = "000"
R1 = "001"
R2 = "010"
R3 = "011"
R4 = "100"
R5 = "101"
R6 = "110"
FLAGS = "111"
Addition = "10000"
Subtraction = "10001"
MoveImmediate = "10010"
MoveRegister = "10011"
Load = "10100"
Store = "10101"
Multiply = "10110"
Divide = "10111"
RightShift = "11000"
LeftShift = "11001"
ExclusiveOR = "11010"
Or = "11011"
And = "11100"
Invert = "11101"
Compare = "11110"
UnconditionalJump = "11111"
JumpIfLessThan = "01100"
JumpIfGreaterThan = "01101"
JumpIfEqual = "01111"
Halt = "01010"

def returnCode(opCode, reg1, reg2, reg3, mem, imm ):
    final = ""
    if(opCode == Addition):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == Subtraction):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == MoveImmediate):
        pass
    elif(opCode == MoveRegister):
        pass
    elif(opCode == Load):
        final = opCode + reg1+ mem
    elif(opCode == Store):
        final = opCode + reg1+ mem
    elif(opCode == Multiply):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == Divide):
        final = opCode + "00000" + reg1+ reg2
    elif(opCode == RightShift):
        final = opCode + reg1 + imm
    elif(opCode == LeftShift):
        final = opCode + reg1 + imm
    elif(opCode == ExclusiveOR):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == Or):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == And):
        final = opCode +"00"+ reg1+ reg2+ reg3
    elif(opCode == Invert):
        final = opCode + "00000" + reg1+ reg2
    elif(opCode == Compare):
        final = opCode + "00000" + reg1+ reg2
    elif(opCode == UnconditionalJump):
        final = opCode + "000" + mem
    elif(opCode == JumpIfLessThan):
        final = opCode + "000" + mem
    elif(opCode == JumpIfGreaterThan):
        final = opCode + "000" + mem
    elif(opCode == JumpIfEqual):
        final = opCode + "000" + mem
    elif(opCode == Halt):
        final = opCode + "00000000000"
    
    return final



with open("data_file.txt") as f:
    content_list = f.readlines()
g = open("binary.txt", "x")

for line in content_list:
    listA = line.split() 
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "sub":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "mov":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "ld":  
        re1 = returnRegister(listA[1])
        
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)

