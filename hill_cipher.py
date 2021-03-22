import numpy as np
import math
from functions import *

# Read in the matrix
keyMatrix = []
keyMatrix.append([int(x) for x in input("Enter the first row of the key matrix, seperate elements by a space:\n").split()])
keyMatrix.append([int(x) for x in input("Enter the second row of the key matrix, seperate elements by a space:\n").split()])

# convert into a numpy array
A = np.array(keyMatrix) % 27

# find the determinant and check if it is valid
A_det = int(np.linalg.det(A) % 27)
if(A_det % 3 == 0 or A_det == 0):
    print("Bad key matrix! Inverse cannot be found.")
    quit()

# encode or decode 
if(int(input("Enter 1 to encode a string or enter 2 to decode: ")) == 1):
    string = input("Enter String to encode: ").upper()
    if(len(string) % 2 != 0): string += " " # cannot have odd number of letters

    #enocde the matrix
    encodedMatrix = np.array(getMatrixString(string))
    encodedMatrix = np.matmul(A,encodedMatrix) % 27

    #print encoded
    encodedStr = ""
    for i in range(len(encodedMatrix[0])):
        encodedStr += str(encodedMatrix[0][i]).zfill(2)
        encodedStr += str(encodedMatrix[1][i]).zfill(2)
    print("Encoded message: \n", encodedStr)

else:
    # find inverse of key matrix
    multiInv = findMultInv(A_det, 27) # multiplicative inverse of determinant in mod 27
    A_adj = np.array(getAdj(A.tolist())) % 27 # adjoint of the key matrix
    A_inv = (multiInv * A_adj) % 27 # actual inverse matrix

    # get the encoded message:
    encoded = input("Enter the encoded string: \n")
    encodedMatrix = np.array(getMatrixEncoded(encoded))

    # decode the message:
    decodedMatrix = np.matmul(A_inv, encodedMatrix) % 27
    decoded = getDecodedString(decodedMatrix)

    print("Decoded message: \n", decoded)
