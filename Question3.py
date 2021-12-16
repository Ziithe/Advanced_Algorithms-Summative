#Cryptography algorithm by Ziithe Ewen Hiwa

import math
import time

#Main function, get the plain text and key
# run encryption and decryption algorithms
def main(text, key):
    eText = encryption(key, text)
    dText = decryption(key, eText)

    print("\nYour encrypted text is:", eText)
    print("\nYour decrypted text is:", dText)

#encryption function
def encryption(key, text):
    #create a matrix using the key and text length as rows and columns
    #initialise matrix values as empty strings
    cryptText = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(text):
            #add the string characters in matrix
            cryptText[col] += text[pointer]
            pointer += key
    return "".join(cryptText)


def decryption(key, text):
    #reverse encryption by calculating number of columns
    numCols = math.ceil(len(text) / key)
    numRows = key
    #calculate boxed with values 
    occupiedBoxes = (numCols * numRows) - len(text)
    plainText = [""] * numCols
    col = 0
    row = 0

    #reverse the input method to reorder the texts
    for i in text:
        plainText[col] += i
        col += 1

        if (
            (col == numCols)
            or (col == numCols - 1)
            and (row >= numRows - occupiedBoxes)
        ):
            col = 0
            row += 1
    return "".join(plainText)


main("Plain text", 2)