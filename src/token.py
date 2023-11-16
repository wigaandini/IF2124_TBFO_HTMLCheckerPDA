import os
import sys
import re

def lex(text, token_rules):
    pos = 0
    line = 1
    tokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1

        flag = None
        for current_token in token_rules:
            pattern, tag = current_token

            regex = re.compile(pattern)
            flag = regex.match(text,pos)

            if flag:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not flag:
            print("SYNTAX ERROR !!!")
            print(f'Error Expression at line {line}: {text[pos:].splitlines()[0]}')
            sys.exit(1)
        else:
            pos = flag.end(0)

    return tokens

def createToken(text):
    # Read file
    file = open(text, encoding="utf8")
    characters = file.read()
    file.close()

    tokens = lex(characters, token_rules)
    tokenResult = []

    for token in tokens:
        tokenResult.append(token)

    # Write file
    # path = os.getcwd()
    # fileWrite = open(path + "./tokenResult.txt", 'w')
    # for token in tokenResult:
    #     fileWrite.write(str(token)+" ")
        # print(token)
    # fileWrite.close()

    return tokenResult