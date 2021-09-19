import sys
import re
from array import array

keycnt = 0
Switch_num = 0
Casetotal = 0
Flag=0
Case_num = array('i')


KEYword = (
    "unsigned", "void", "volatile", "while", "struct", "switch", "typedef", "union",
    "short", "signed", "sizeof", "static", "const", "continue", "default", "do",
    "int", "long", "register", "return", "double", "else", "enum", "extern",
    "auto", "break", "case", "char", "float", "for", "goto", "if"
)


def simplity(path):
    text = open(path, mode='r').read()
    textre = re.sub(r"[0123456789]+"," ", text)
    textre = re.sub(r"[\n]+", "  ", textre)         #将代码中的换行都变成空格
    textre = re.sub(r"['+*/=<>():']+", "  ", textre)         #将代码中的运算符都变成空格
    textre = re.sub(r"[ \f\r\t\v]+", " ", textre)   #将代码中的多余空格删除
    textre = re.split(r"\W", textre)                #转化为列表
    return textre

def cntfuc(textre):
    global keycnt,Switch_num,Casetotal,Flag
    global Case_num
    text_iter = iter(range(len(textre)))
    for i in text_iter:
        temp = textre[i]
        if temp != ' 'and temp in KEYword:
            keycnt +=1

            if temp == 'switch':            # 用于GRADE 2
                Switch_num+=1

    text_iter = iter(range(len(textre)))
    for j in text_iter:
        temp = textre[j]
        if temp =='case':
            Casetotal += 1
        elif temp == 'switch' :
            if Flag == 0:
                Flag +=1
                continue        #第一个switch前不统计
            Case_num.append(Casetotal)
            Casetotal = 0;
    Case_num.append(Casetotal)   #将最后一个switch的case个数存入数组

    print("total num: ",keycnt)
    print("switch num: ",Switch_num)
    print("case num:" ,*Case_num)

if __name__ == "__main__":
    PATH = sys.argv[1]
    FILE = simplity(PATH)
    cntfuc(FILE)
