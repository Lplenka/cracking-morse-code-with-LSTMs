docu = open("word_list.txt","r")
new = open("word_list9.txt","w")
v = []
for line in docu:
    if len(line) == 9:
       v.append(line)

with open('word_list9', 'wb') as fp:
    pickle.dump(v, fp)
