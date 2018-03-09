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
print(output_list[:2])
print(input_list[:2])
