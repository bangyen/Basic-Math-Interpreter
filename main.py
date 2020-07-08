from lexer import Lexer

while True:
    text = input('Expression: ')
    lexer = Lexer(text)
    tokens = lexer.generateTokens()
    print(list(tokens))
