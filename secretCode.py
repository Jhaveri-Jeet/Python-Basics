# Making an secret code
# incomplete code


def sendCode(code):
    temp = code[-1]
    code[-1] = code[0]
    code[0] = temp
    print(code)


sendCode("This is the code")
