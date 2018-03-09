import random
import numpy as np
import matplotlib.pyplot as plt

# construct the Morse dictionary
alphabet = " ".join("abcdefghijklmnopqrstuvwxyz").split()
values = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-','.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
morse_dict = dict(zip(alphabet, values))

def morse_ecode(word):
    letters = " ".join(word).split()
    morse_code = list(map(lambda x : morse_dict[x],letters))
    morse_code = "*".join(morse_code)

    return morse_code

#print(morse_ecode("aardvark"))
