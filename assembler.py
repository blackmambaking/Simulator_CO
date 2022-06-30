import opcode


r0 = "000"
r1 = "001"
r2 = "010"
r3 = "011"
r4 = "100"
r5 = "101"
r6 = "110"
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

def replace_the_word(input1, input2):
    f = open("question1_input.txt", "r")
    content = f.read()
    q=content.split()
    strI=""
    # input1=input("enter the word you want to replace: ")
    # input2=input("enter the word with which you want to replace given word: ")
    for i in range(len(q)):
        if q[i]==input1:
            q[i]=input2
        strI = strI + ' ' + q[i]    

    f2 = open("question1_output.txt", "w+")
    f2.write(strI)

with open("data_file.txt") as f:
    content_list = f.readlines()

