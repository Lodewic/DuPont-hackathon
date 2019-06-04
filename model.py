from keras.models import Sequential
from keras import presprocessing
import sys
import numpy
from keras.layers import Dense, LSTM

import_file = sys.argv[1].readlines()
#encode
list_input = []
for line in import_file:
	list_input.append(preprocessing.text.one_hot(line, n, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' '))


n_list = numpy.array(list_input, "float32")

model = Sequential()
model.add(Dense(32, input_shape=n_list.shape[:1]))
model.add(LSTM(15))
model.add(Dense(3))
model.compile('SGD')
model.fit()
