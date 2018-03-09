import pickle

new = open("word_list.txt","r")
v = []
for line in new.readlines():
    if len(line) == 10:
       v.append(line[:-1])
print(len(v))
with open('word_list9', 'wb') as fp:
    pickle.dump(v, fp)
