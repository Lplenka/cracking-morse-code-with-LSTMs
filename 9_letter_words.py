docu = open("word_list.txt","r")
new = open("word_list9.txt","w")

for line in docu:
    if len(line) == 9:
       new.write(line)
