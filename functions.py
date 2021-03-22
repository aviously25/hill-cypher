# finds the multiplicative inverse of x in modulo mod
def findMultInv(x, mod):
    for i in range(mod):
        if((x * i) % mod == 1):
            return i;
    return -1;

# returns the adjoint matrix
def getAdj(matrix):
    matrix_adj = [
                    [matrix[1][1], -matrix[0][1]],
                    [-matrix[1][0], matrix[0][0]]
                    ]
    return matrix_adj

# returns original string converted to matrix
def getMatrixString(string):
    row1 = []
    row2 = []
    for i, char in enumerate(string[::2]):
        charNum = ord(char) - 64
        if(charNum == -32): charNum = 0
        row1.append(charNum)

    for i, char in enumerate(string[1::2]):
        charNum = ord(char)-64
        if(charNum == -32): charNum = 0
        row2.append(charNum)
    
    return [row1, row2]

def getMatrixEncoded(string):
    row1 = []
    row2 = []
    string = [int(string[i:i+2]) for i in range(0, len(string), 2)]

    for num in string[::2]:
        row1.append(num)

    for num in string[1::2]:
        row2.append(num)


    return [row1, row2]

def getDecodedString(decodedMatrix):
    decoded = ""

    for i in range(len(decodedMatrix[0])):
        if(decodedMatrix[0][i] == 0): char1 = " "
        else: char1 = chr(decodedMatrix[0][i] + 64)

        if(decodedMatrix[1][i] == 0): char2 = " "
        else: char2 = chr(decodedMatrix[1][i] + 64)

        decoded = decoded + char1 + char2

    return decoded
