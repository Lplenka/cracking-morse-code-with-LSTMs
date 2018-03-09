import random
import numpy as np
import matplotlib.pyplot as plt
import pickle

# construct the Morse dictionary
alphabet = " ".join("abcdefghijklmnopqrstuvwxyz").split()
values = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-','.-.', '...', ' - ', '..-', '...-', '.--', ' - ..-', ' - .--', ' - -..']
morse_dict = dict(zip(alphabet, values))
l= []
def morse_ecode(word):
    letters = " ".join(word).split()
    morse_code = list(map(lambda x : morse_dict[x],letters))
    morse_code = "*".join(morse_code)

    return morse_code


docu = open("word_list9.txt","r")


for line in docu:
    l.append(morse_ecode(line))

print(len(l))

with open('morse_code_list', 'wb') as fp:
    pickle.dump(l, fp)



#with open ('outfile', 'rb') as fp:
    #itemlist = pickle.load(fp)
