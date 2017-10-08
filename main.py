import lexer, const

if __name__ == '__main__':
    lexer_obj = lexer.Lexer("test.txt")
    while lexer_obj.get_sym() != const.EOF:
        print("----------")
        print("token:"+str(lexer_obj.token))
        print("symbol:"+str(lexer_obj.symbol))
        print("num:"+str(lexer_obj.num))