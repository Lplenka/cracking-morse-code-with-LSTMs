import random
import morse_encode
import pickle
word_len = 9
max_len_x = 4*word_len + (word_len-1)
max_len_y = word_len
def data_gen(n):

        with open ('word_list9', 'rb') as fp:
             words = pickle.load(fp)
        # Shuffle the list since the words are ordered
        random.shuffle(words)

        g_out = lambda x: ' '*(max_len_y -len(x)) + x
        output_list = [g_out(word) for word in words]

        g_in = lambda x: morse_encode.morse_ecode(x)+' '*(max_len_x
                                             - len(morse_encode.morse_ecode(x)))
        input_list = [g_in(word) for word in words]

        return output_list, input_list

output_list, input_list = data_gen(9)
with open('input_data', 'wb') as ip:
    pickle.dump(input_list, ip)
with open('output_data', 'wb') as op:
    pickle.dump(output_list, op)
print(len(output_list))
print(len(input_list))

for i in range(len(output_list)):
    if len(input_list[i]) > 44:
       print(output_list[i], "   ", input_list[i])
