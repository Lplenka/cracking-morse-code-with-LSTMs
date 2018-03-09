import numpy as np
from keras.models import Sequential
from keras import layers
import pickle

#include the white space as a character in both cases below.
chars_in = '*-. '
chars_out = 'abcdefghijklmnopqrstuvwxyz '
word_len = 9
max_len_x = 4*word_len + (word_len-1)
max_len_y = word_len

def one_hot_encode(inputs,outputs):
    class CharTable(object):
          def __init__(self, chars):
              self.chars = sorted(set(chars))
              self.char_indices = dict((c, i) for i, c in
                                            enumerate(self.chars))
              self.indices_char = dict((i, c) for i, c in
                                            enumerate(self.chars))

          def encode(self, token, num_rows):
              x = np.zeros((num_rows, len(self.chars)))
              for i, c in enumerate(token):
                  x[i, self.char_indices[c]] = 1
              return x

          def decode(self, x, calc_argmax=True):
              if calc_argmax:
                 x = x.argmax(axis=-1)
              return ''.join(self.indices_char[x] for x in x)

    #CharTable Objects
    ctable_in = CharTable(chars_in)
    ctable_out = CharTable(chars_out)
    x = np.zeros((len(inputs), max_len_x, len(chars_in)))
    y = np.zeros((len(outputs), max_len_y, len(chars_out)))
    for i, token in enumerate(inputs):
        x[i] = ctable_in.encode(token, max_len_x)
    for i, token in enumerate(outputs):
        y[i] = ctable_out.encode(token, max_len_y)

    return x,y


def prepare_arrays(input_list,output_list):
    X , Y =one_hot_encode(input_list,output_list)
    m = len(X)// 4
    (x_train, x_val) = X[:m], X[m:]
    (y_train, y_val) = Y[:m], Y[m:]
    return x_train, x_val,y_train, y_val



def prepare_model(x_train, x_val,y_train, y_val):
    latent_dim = 256
    model = Sequential()
    model.add(layers.LSTM(latent_dim, input_shape=(max_len_x,len(chars_in))))
    model.add(layers.RepeatVector(max_len_y))
    model.add(layers.LSTM(latent_dim, return_sequences=True))
    model.add(layers.TimeDistributed(layers.Dense(len(chars_out))))
    model.add(layers.Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam',
                                           metrics=['accuracy'])
    model.summary()
    Epochs = 120
    Batch_size = 1024
    hist = model.fit(x_train, y_train, batch_size=Batch_size, epochs=
                            Epochs, validation_data=(x_val, y_val))
    plt.figure(figsize=(20,5))
    plt.subplot(121)
    plt.plot(hist.history['acc'])
    plt.plot(hist.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.subplot(122)
    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper right')
    plt.show()
    return None

if __name__ == '__main__':
    #Get Dataset
    with open ('input_data', 'rb') as ip:
        input_list = pickle.load(ip)

    with open ('output_data', 'rb') as op:
        output_list = pickle.load(op)

    x_train, x_val,y_train, y_val = prepare_arrays(input_list,output_list)
    prepare_model(x_train, x_val,y_train, y_val)
