import pickle

new = open("word_list.txt","r")
v = []
for line in new:
    if len(line) == 9:
       v.append(line)
print(len(v))
with open('word_list9', 'wb') as fp:
    pickle.dump(v, fp)
