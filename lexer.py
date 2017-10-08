from const import *


class Lexer:
    char = ' '
    token = ""
    num = 0x33333334
    symbol = EXCSY
    src = None

    srcpos = 0

    def __init__(self, file):
        self.src = open(file, "r+")

    def getchar(self):
        self.char = self.src.read(1)
        #print("getchar:" + self.char)
        if self.char == "":
            #print ("EOF")
            self.char = "\0"
        self.srcpos += 1

    def clear_token(self):
        self.token = ""

    def is_space(self):
        return self.char==' '

    def is_newline(self):
        return self.char=='\n'

    def is_tab(self):
        return self.char=='\t'

    def is_letter(self):
        return self.char.isalpha()

    def is_digit(self):
        return self.char.isdigit()

    def is_colon(self):
        return self.char==':'

    def is_comma(self):
        return self.char==','

    def is_semi(self):
        return self.char==';'

    def is_equ(self):
        return self.char=='='

    def is_plus(self):
        return self.char=='+'

    def is_minus(self):
        return self.char=='-'

    def is_divi(self):
        return self.char=='/'

    def is_star(self):
        return self.char=='*'

    def is_lpar(self):
        return self.char=='('

    def is_rpar(self):
        return self.char==')'

    def cat_token(self):
        self.token += self.char

    def retract(self):
        #print("backchar:" + self.char)
        self.srcpos -= 1
        self.src.seek(self.srcpos, 0)

    def reserver(self):
        if self.token == "BEGIN":
            return BEGINSY
        elif self.token == "END":
            return ENDSY
        elif self.token == "IF":
            return IF
        elif self.token == "THEN":
            return THENSY
        elif self.token == "ELSE":
            return ELSESY
        else:
            return 0

    def trans_num(self):
        return eval(self.token)

    def error_handler(self):
        print("Lexical error.")

    def get_sym(self):
        self.clear_token()
        self.num = 0
        while True:
            self.getchar()
            if not (self.is_space() or self.is_newline() or self.is_tab()):
                if self.char == '\0':
                    return -1
                break

        if self.char == '\0':
            return -1

        if self.is_letter():
            while self.is_letter() or self.is_digit():
                self.cat_token()
                self.getchar()
            #self.retract()

            result_value = self.reserver()

            if result_value == 0:
                self.symbol = IDSY
            else:
                self.symbol = result_value
        elif self.is_digit():
            while self.is_digit():
                self.cat_token()
                self.getchar()
            self.retract()
            self.num = self.trans_num()
            self.symbol = INTSY
        elif self.is_colon():
            self.getchar()
            if self.is_equ():
                self.symbol = ASSIGNSY
            else:
                self.retract()
                self.symbol = COLONSY
        elif self.is_plus():
            self.symbol = PLUSSY
        elif self.is_minus():
            self.symbol = MINUSSY
        elif self.is_star():
            self.symbol = STARSY
        elif self.is_lpar():
            self.symbol = LPARSY
        elif self.is_comma():
            self.symbol = COMMASY
        elif self.is_semi():
            self.symbol = SEMISY
        elif self.is_equ():
            self.symbol = EQUSY
        elif self.is_divi():
            self.getchar()
            if self.is_star():
                while True:
                    while True:
                        self.getchar()
                        if not not self.is_star():
                            break

                    while True:
                        self.getchar()
                        if self.is_divi():
                            return 0
                        if not self.is_star():
                            break
                    if not not self.is_star():
                        break
            self.retract()
            self.symbol = DIVISY
        else:
            self.error_handler()
        return 0


