import sys
import re

keycnt = 0
Switch_num = 0


KEYword = (
    "unsigned", "void", "volatile", "while", "struct", "switch", "typedef", "union",
    "short", "signed", "sizeof", "static", "const", "continue", "default", "do",
    "int", "long", "register", "return", "double", "else", "enum", "extern",
    "auto", "break", "case", "char", "float", "for", "goto", "if"
)


def simplity(path):
    text = open(path, mode='r').read()
    textre = re.sub(r"[0123456789]+", "  ", text)   #将代码中的数字都变成空格，因为数字对我们的统计没影响
    textre = re.sub(r"[\n]+", "  ", textre)         #将代码中的换行都变成空格
    textre = re.sub(r"['+*/=<>()']+", "  ", textre)         #将代码中的运算符都变成空格
    textre = re.sub(r"[ \f\r\t\v]+", " ", textre)   #将代码中的多余空格删除
    #print(textre)
    textre = re.split(r"\W", textre)                #转化为列表
    return textre

def cntfuc(textre):
    global keycnt,Switch_num
    global Case_num
    text_iter = iter(range(len(textre)))
    for i in text_iter:
        temp = textre[i]
        if temp != ' 'and temp in KEYword:
            keycnt +=1

            if temp == 'switch':            # 用于GRADE 2
                Switch_num+=1


    print("total num: ",keycnt);
    print("switch num: ",Switch_num);

if __name__ == "__main__":
    PATH = sys.argv[1]
    FILE = simplity(PATH)
    cntfuc(FILE)
