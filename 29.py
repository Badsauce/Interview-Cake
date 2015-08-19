def validateContainerCharacterPairs(inputString):
    if len(inputString) < 1:
        return True;

    openerStack = []

    for character in inputString:
        if character in '()[]{}':
            if isOpener(character):
                openerStack.append(character)
            if isCloser(character):
                if len(openerStack) > 0:
                    opener = openerStack[-1]
                    if isMatchingContainerPair(opener,character):
                        openerStack.pop()
                    else:
                        return False
                else:
                    return False

    if len(openerStack) > 0:
        return False

    return True

def isMatchingContainerPair(opener,closer):
    if opener == '(' and closer == ')':
        return True
    elif opener == '[' and closer == ']':
        return True
    elif opener == '{' and closer == '}':
        return True
    else:
        return False

def isOpener(character):
    return character in '([{'

def isCloser(character):
    return character in ')]}'

def testCase(inputString):
    print('{} is valid: {}'.format(inputString,validateContainerCharacterPairs(inputString)))

testCase('')
testCase('nnn')
testCase('[')
testCase(']')
testCase('[]')
testCase('[}')
testCase('{ [ ] ( ) }')
testCase('{ [ ( ] ) }')
testCase('{ [ }')

