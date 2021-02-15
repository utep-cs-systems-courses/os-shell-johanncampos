import os

input = None

def myReadChar():
    input = os.read(0, 100)
    return input

def myReadLine():
    input = myReadChar()
    inputString = ""
    i = 0

    while i < len(input):
        if chr(input[i]) != '\n':
            inputString += chr(input[i])
        i += 1

    return tokenize(inputString)

def tokenize(input):
    args = []
    curWord = ""
    i = 0

    while i < len(input):
        if input[i] != ' ':
            curWord += input[i]
        else:
            args.append(curWord)
            curWord = ""
        if i == len(input) - 1:
            args.append(curWord)
        i += 1

    return args

def main():
    return 0

if __name__ == '__main__':
    main()
