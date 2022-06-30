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

def returnCode(opCode, reg1, reg2, reg3, mem ):
    final = ""
    if(opCode == Addition):
        pass
    elif(opCode == Subtraction):
        pass
    elif(opCode == MoveImmediate):
        pass
    elif(opCode == MoveRegister):
        pass
    elif(opCode == Load):
        pass
    elif(opCode == Store):
        pass
    elif(opCode == Multiply):
        pass
    elif(opCode == Divide):
        pass
    elif(opCode == RightShift):
        pass
    elif(opCode == LeftShift):
        pass
    elif(opCode == ExclusiveOR):
        pass
    elif(opCode == Or):
        pass
    elif(opCode == And):
        pass
    elif(opCode == Invert):
        pass
    elif(opCode == Compare):
        pass
    elif(opCode == UnconditionalJump):
        pass
    elif(opCode == JumpIfLessThan):
        pass
    elif(opCode == JumpIfGreaterThan):
        pass
    elif(opCode == JumpIfEqual):
        pass
    elif(opCode == Halt):
        pass
    
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

