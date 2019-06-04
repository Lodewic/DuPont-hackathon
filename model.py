from keras.models import Sequential
from keras import preprocessing
import sys
import numpy as np
from keras.layers import Dense, LSTM,Embedding
from keras.optimizers import Adam

import_file = open(sys.argv[1],'r').read().strip('\n').split('\n')
output_file = open(sys.argv[2],'r').read().strip('\n').split('\n')

output_file = np.array([[float(x) if x else 0 for x in line.split('\t')] for line in output_file ],'float32')

def one_hot_encode(sequence,encoding):
    return [ [ 1 if x == aa else 0 for aa in encoding ] for x in sequence ]

#encode
AA_LABELS = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
             'T', 'V', 'W', 'Y']


list_input = []
for line in import_file:
	list_input.append(one_hot_encode(line.strip(), AA_LABELS))

n_list = np.array(list_input, "float32")
n_list = np.reshape(n_list,(n_list.shape[0],n_list.shape[2], n_list.shape[1]))

model = Sequential()
model.add(Dense(len(AA_LABELS)+1,input_shape=(n_list.shape[1],n_list.shape[2])))
model.add(LSTM(15))
model.add(Dense(4))
model.compile(optimizer=Adam(lr=.005),
              loss='mse',
              metrics=['accuracy'])
model.fit(n_list, output_file, epochs=200, batch_size=64)
