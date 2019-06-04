from keras.models import Sequential
from keras import preprocessing
import sys
import numpy as np
from keras.layers import Dense, LSTM

import_file = open(sys.argv[1],'r').readlines()

def one_hot_encode(sequence: list or str, encoding: dict, max_len: int = None) -> np.array:
    one_hot_sequence = np.array([encoding[element] for element in sequence])
    if max_len is not None:
        padding = np.zeros(shape=(max_len - len(sequence), len(encoding[sequence[0]])))
        one_hot_sequence = np.concatenate([one_hot_sequence, padding])
    return one_hot_sequence.tolist()

#encode
list_input = []
for line in import_file:
	list_input.append(one_hot_encode(line, 26))

n_list = np.array(list_input, "float32")

model = Sequential()
model.add(Dense(32, input_shape=n_list.shape[:1]))
model.add(LSTM(15))
model.add(Dense(3))
model.compile('SGD')
model.fit()
