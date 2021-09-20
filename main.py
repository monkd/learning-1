import sys
import re
from array import array

KeyCnt = 0
Switch_Num = 0
CaseTotal = 0
IfTotal = 0
Flag = 0
Case_Num = array('i')
IfArray = array('i')
IF_EL = 0
IF_ELIF_IF = 0


KeyWord = (
    "auto", "break", "case", "char",
    "const", "continue", "default", "do",
    "double", "else", "enum", "extern",
    "float", "for", "goto", "if",
    "int", "long", "register", "return",
    "short", "signed", "sizeof", "static",
    "struct", "switch", "typeof", "union",
    "unsigned", "void", "volatile", "while"
)


def simplity(path):
    Text = open(path, mode='r').read()
    Textre = re.sub(r"\/\*([^\*^\/]*|[\**\/*]*|[^\**\/]*)*\*\/", "", Text)
    Textre = re.sub(r"\/\/[^\n]*", "", Textre)
    Textre = re.sub(r"\"(.*)\"", "", Textre)                #以上三行代码用于删除不应该被统计但是会影响结果的部分
    Textre = re.sub(r"[0123456789]+"," ", Textre)           #将代码中数字都变成空格
    Textre = re.sub(r"[\n]+", "  ", Textre)                 #将代码中的换行都变成空格
    Textre = re.sub(r"['+*/=<>():']+", "  ", Textre)        #将代码中的运算符都变成空格
    Textre = re.sub(r"[ \f\r\t\v]+", " ", Textre)           #将代码中的多余空格删除
    Textre = re.split(r"\W", Textre)                        #转化为列表
    return Textre



def Slove(Textre,GRADE):
    global KeyCnt,Switch_Num,CaseTotal
    global IfTotal,Flag
    global IF_EL,IF_ELIF_IF
    global Case_Num,IF_EL
    text_iter = iter(range(len(Textre)))
    for i in text_iter:
        Temp = Textre[i]
        if Temp != ' 'and Temp in KeyWord:
            KeyCnt +=1

            if Temp == 'switch':            # 用于GRADE 2 中统计 switch 出现的次数
                Switch_Num+=1

            if Temp == 'if' and Textre[i-1] != 'else':
                IfArray.append(1)
                IfTotal += 1

            if Temp == 'else' and Textre[i+1] == 'if':
                if IfArray[IfTotal-1] == 1:
                    IfArray.pop()
                    IfArray.append(3)

            if Temp == 'else' and Textre[i + 1] != 'if':           #用一个类似栈的实现来完成 GRADE3 和 GRADE4
                if IfArray[IfTotal-1] == 1:
                    IF_EL+=1
                    IfTotal -= 1
                    IfArray.pop()
                else:
                    IF_ELIF_IF += 1
                    IfTotal -= 1
                    IfArray.pop()

    text_iter = iter(range(len(Textre)))
    for j in text_iter:                                            #用于统计各个switch循环中 case 出现的次数
        temp = Textre[j]
        if temp =='case':
            CaseTotal += 1

        elif temp == 'switch' :
            if Flag == 0:
                Flag +=1
                continue                                            #第一个switch前不统计
            Case_Num.append(CaseTotal)
            CaseTotal = 0;

    Case_Num.append(CaseTotal)                                      #将最后一个switch的case个数存入数组

    if GRADE >= 1:
        print("total num: ", KeyCnt)

    if GRADE >= 2:
        print("switch num: ", Switch_Num)
        if Switch_Num > 0:
            print("case num:" , *Case_Num)
        else:
            print("case num: 0")

    if GRADE >= 3:
        print("if-else num:", IF_EL)

    if GRADE >= 4:
        print("if-elseif-else num:", IF_ELIF_IF)                    #分 4 个 GRADE 来输出


if __name__ == "__main__":
    PATH = sys.argv[1]
    GRADE = sys.argv[2]
    FILE = simplity(PATH)
    Grade = int(GRADE)
    while Grade > 4 or Grade < 1:
        print("您输入地等级有误，请重新输入")
        GRADE = input()
        Grade = int(GRADE)
    Slove(FILE,Grade)
