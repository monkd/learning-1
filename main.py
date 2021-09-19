
import sys
import re

KEYword = (
    "unsigned", "void", "volatile", "while", "struct", "switch", "typedef", "union",
    "short", "signed", "sizeof", "static", "const", "continue", "default", "do",
    "int", "long", "register", "return", "double", "else", "enum", "extern",
    "auto", "break", "case", "char", "float", "for", "goto", "if"
)


def simplity(path):
    text = open(path, mode='r').read()
    textre = re.sub(r"[0123456789]+", "  ", text)
    textre = re.sub(r"[\n]+", "  ", textre)
    textre = re.sub(r"['+*/=<>()''-']+", "  ", textre)
    textre = re.sub(r"[ \f\r\t\v]+", " ", textre)
    print(textre)
    return textre


if __name__ == "__main__":
    PATH = sys.argv[1]
    FILE = simplity(PATH)