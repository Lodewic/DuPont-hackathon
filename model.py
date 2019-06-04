from keras.models import Sequential
from keras import preprocessing
import sys
import numpy as np
from keras.layers import Dense, LSTM,Embedding

import_file = open(sys.argv[1],'r').read().strip('\n').split('\n')

def one_hot_encode(sequence,encoding):
    return [ [ 1 if x == aa else 0 for aa in encoding ] for x in sequence ]

#encode

AA_LABELS = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
             'T', 'V', 'W', 'Y']

list_input = []
for line in import_file:
	list_input.append(one_hot_encode(line.strip(), AA_LABELS))

n_list = np.array(list_input, "float32")

model = Sequential()
model.add(Embedding(len(AA_LABELS)+1, 100,input_length=(n_list.shape[1],n_list.shape[2])))
model.add(LSTM(15))
model.add(Dense(3))
model.compile(optimizer='rmsprop',
              loss='mse',
              metrics=['accuracy'])
model.fit(n_list, epochs=10, batch_size=32)

