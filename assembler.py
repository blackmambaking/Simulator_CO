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

        
def decimalToBinary(decimal):
    binrep = bin(decimal)[2:]
    return binrep.zfill(8)
# hardcoding codes

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

#returning binary code for each line

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


#reading input line by line

with open("data_file.txt") as f:
    content_list = f.readlines()
g = open("binary.txt", "x")
instructionCounter = 0
varCounter = 0
listOfVar = []
addressOfVar = []

#finding the starting memory address of variables
for line in content_list:
    listA = line.split() 
    if listA [0] == "var":
        listOfVar.append(listA[1])
        varCounter = varCounter + 1
    else:
        instructionCounter = instructionCounter + 1
for i in range(varCounter):
    bi = decimalToBinary(instructionCounter)
    addressOfVar.append(bi)
    instructionCounter = instructionCounter + 1

#dealing each input one by one
for line in content_list:
    listA = line.split() 
    
    #addition
    if listA [0] == "add":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3, 0, 0)
        
    #subtraction
    if listA [0] == "sub":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3, 0, 0)
        

    #moving value
    if listA [0] == "mov":  
        
        if listA[2] == "R0" or listA[2] == "R1" or listA[2] == "R2" or listA[2] == "R3" or listA[2] == "R4" or listA[2] == "R5" or listA[2] == "R6":
            re1 = returnRegister(listA[1])
            re2 = returnRegister(listA[2])
            returnCode(MoveRegister, re1, re2, 0, 0, 0)
        else:
            re1 = returnRegister(listA[1])
            val = listA[2]
            val = val[1:]
            num = int(val)
            bi = decimalToBinary(num)
            returnCode(MoveImmediate, re1, 0, 0, 0, bi)
        
    #load value
    if listA [0] == "ld":  
        re1 = returnRegister(listA[1])
        returnCode(Addition, re1, re2, re3)
        
    
    #store
    if listA [0] == "st":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
        
    
    #multiply
    if listA [0] == "mul":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Multiply, re1, re2, re3)
        

    #divide
    if listA [0] == "div":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        returnCode(Divide, re1, re2)
        

    #rightShift
    if listA [0] == "rs":  
        re1 = returnRegister(listA[1])
        val = listA[2]
        val = val[1:]
        num = int(val)
        bi = decimalToBinary(num)

        returnCode(RightShift, re1, bi)
        

    #leftShift
    if listA [0] == "ls":  
        re1 = returnRegister(listA[1])
        val = listA[2]
        val = val[1:]
        num = int(val)
        bi = decimalToBinary(num)

        returnCode(LeftShift, re1, bi)
        

    #exclusive OR
    if listA [0] == "xor":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(ExclusiveOR, re1, re2, re3)
        


    #OR
    if listA [0] == "or":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Or, re1, re2, re3)
       


    #AND
    if listA [0] == "and":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(And, re1, re2, re3)
        

    #invert
    if listA [0] == "not":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        returnCode(Invert, re1, re2)
        

    #compare
    if listA [0] == "cmp":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        returnCode(Compare, re1, re2)
        

    #unconditional jump
    if listA [0] == "jmp":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
        

    #jump if less than
    if listA [0] == "jlt":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
        
    
    # jump if greater than 
    if listA [0] == "jgt":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
       
    
    #jump if equal
    if listA [0] == "je":  
        re1 = returnRegister(listA[1])
        re2 = returnRegister(listA[2])
        re3 = returnRegister(listA[3])
        returnCode(Addition, re1, re2, re3)
        

    #halt
    if listA [0] == "hlt":  
        returnCode(Halt)
        

