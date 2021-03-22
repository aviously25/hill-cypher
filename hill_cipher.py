import numpy as np
import math
from functions import *

# class to print out colored text in terminal
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Read in the matrix
keyMatrix = []
keyMatrix.append([int(x) for x in input(f"{colors.OKBLUE}Enter the first row of the key matrix, seperate elements by a space:{colors.ENDC}\n").split()])
keyMatrix.append([int(x) for x in input(f"{colors.OKBLUE}Enter the second row of the key matrix, seperate elements by a space:{colors.ENDC}\n").split()])

# convert into a numpy array
A = np.array(keyMatrix) % 27

# find the determinant and check if it is valid
A_det = int(np.linalg.det(A) % 27)
if(A_det % 3 == 0 or A_det == 0):
    print(f"{colors.FAIL}Bad key matrix! Inverse cannot be found.{colors.ENDC}")
    quit()

# encode or decode 
if(int(input(f"\n{colors.OKBLUE}Enter 1 to encode a string or enter 2 to decode:{colors.ENDC} ")) == 1):
    string = input(f"{colors.OKBLUE}Enter String to encode: {colors.ENDC}").upper()
    if(len(string) % 2 != 0): string += " " # cannot have odd number of letters

    #enocde the matrix
    encodedMatrix = np.array(getMatrixString(string))
    encodedMatrix = np.matmul(A,encodedMatrix) % 27

    #print encoded
    encodedStr = ""
    for i in range(len(encodedMatrix[0])):
        encodedStr += str(encodedMatrix[0][i]).zfill(2)
        encodedStr += str(encodedMatrix[1][i]).zfill(2)
    print(f"\n{colors.OKGREEN}Encoded message: \n{colors.ENDC}", encodedStr)

else:
    # find inverse of key matrix
    multiInv = findMultInv(A_det, 27) # multiplicative inverse of determinant in mod 27
    A_adj = np.array(getAdj(A.tolist())) % 27 # adjoint of the key matrix
    A_inv = (multiInv * A_adj) % 27 # actual inverse matrix

    # get the encoded message:
    encoded = input(f"{colors.OKBLUE}Enter the encoded string: {colors.ENDC}\n")
    encodedMatrix = np.array(getMatrixEncoded(encoded))

    # decode the message:
    decodedMatrix = np.matmul(A_inv, encodedMatrix) % 27
    decoded = getDecodedString(decodedMatrix)

    print(f"\n{colors.OKGREEN}Decoded message: \n{colors.ENDC}", decoded)
