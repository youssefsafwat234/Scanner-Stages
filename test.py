import re
from enum import Enum, auto

class LexemeType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()
    NUMBER = auto()
    STRING_LITERAL = auto()
    COMMENT = auto()
    OPERATOR = auto()
    SYMBOL = auto()
    UNRECOGNIZED = auto()

class Lexeme:
    def __init__(self, category, value):
        self.category = category
        self.value = value

    def __str__(self):
        return f"Lexeme: {self.value:<15} Type: {self.category.name}"

# Keywords recognized by the scanner
RESERVED_WORDS = {"int", "float", "return", "if", "else", "while", "for", "char"}

# Patterns for token matching
TOKEN_PATTERNS = {
    LexemeType.IDENTIFIER: r'^[a-zA-Z_][a-zA-Z0-9_]*',
    LexemeType.NUMBER: r'^\d+',
    LexemeType.STRING_LITERAL: r'^"(.*?)"',
    LexemeType.COMMENT: r'^//.*',
    LexemeType.OPERATOR: r'^[+\-*/=<>!&|]+',
    LexemeType.SYMBOL: r'^[;,(){}]',
}

def extract_next_lexeme(text):
    # Remove leading spaces
    text = text.lstrip()

    for lexeme_type, regex in TOKEN_PATTERNS.items():
        match = re.match(regex, text)
        if match:
            fragment = match.group(0)
            if lexeme_type == LexemeType.IDENTIFIER and fragment in RESERVED_WORDS:
                return Lexeme(LexemeType.KEYWORD, fragment), text[len(fragment):]
            return Lexeme(lexeme_type, fragment), text[len(fragment):]

    if text:
        return Lexeme(LexemeType.UNRECOGNIZED, text[0]), text[1:]
    return None, ''  # No more input

def analyze_text(source_text):
    lexemes = []
    remaining_text = source_text
    while remaining_text:
        lexeme, remaining_text = extract_next_lexeme(remaining_text)
        if lexeme:
            lexemes.append(lexeme)
    return lexemes

def start_scanner():
    print("Type expressions to analyze. Type 'exit' to quit.")
    while True:
        source_text = input("Input: ")
        if source_text.strip().lower() == "exit":
            print("Exiting scanner.")
            break
        lexemes = analyze_text(source_text)
        for lexeme in lexemes:
            print(lexeme)
        print()

if __name__ == "__main__":
    start_scanner()