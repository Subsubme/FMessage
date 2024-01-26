import random

alphabet = string.ascii_lowercase

def encrypt(plain_text, shift):
    int(shift)
    if shift > 25:
        shift = 25
    elif shift < 1:
        shift = 1

    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encrypted = plain_text.translate(table)
    return encrypted

def decrypt(text, shift):
    int(shift)
    if shift > 25:
        shift = 25
    elif shift < 1:
        shift = 1
    shift = 26-shift
    shift %= 26

    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encrypted = text.translate(table)
    return encrypted

# greatly thanks to @NeuralNine for posting the tutorial for this