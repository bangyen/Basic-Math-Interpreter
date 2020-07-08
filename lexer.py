from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.currPos = -1
        self.currChar = None
        self.getNextChar()

    def getNextChar(self):
        if self.currPos + 1 < len(self.text):
            self.currPos += 1
            self.currChar = self.text[self.currPos]
        else:
            self.currChar = None

    #generates the tokens so uses yield instead of return
    def generateTokens(self):
        char_dict = {
            '+': Token(TokenType.PLUS),
            '-': Token(TokenType.MINUS),
            '/': Token(TokenType.DIVIDE),
            '*': Token(TokenType.MULTIPLY),
            '(': Token(TokenType.LPAREN),
            ')': Token(TokenType.RPAREN)
        }
        while self.currChar:
            if self.currChar in WHITESPACE:
                self.getNextChar()
            elif self.currChar in DIGITS or self.currChar == ".":
                num = self.generateNumber()
                if num:
                    yield num
            elif self.currChar in char_dict:
                self.getNextChar()
                yield char_dict[self.currChar]
            else:
                raise Exception(f"Illegal character '{self.currChar}'")


    def generateNumber(self):
        numberString = ""
        numDecimalPoints = 0
        while self.currChar and self.currChar in DIGITS or (self.currChar == "." and numDecimalPoints == 0):
            if self.currChar == ".":
                numDecimalPoints += 1
                numberString += "."
            else:
                numberString += self.currChar
            self.getNextChar()
        if numberString == ".":
            return None
        if numberString.startswith('.'):
            numberString = "." + numberString
        if numberString.endswith('.'):
            numberString += '0'

        return Token(TokenType.NUMBER, float(numberString))
