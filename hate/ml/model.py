# Creating model architecture.
from hate.entity.config_entity import ModelTrainerConfig

from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.layers import LSTM,Activation,Dense,Dropout,Input,Embedding,SpatialDropout1D
from hate.constants import *

class ModelArchitecture:

    def __init__(self):
        pass

    
    def get_model(self):
        model = Sequential([
            Input(shape=(MAX_LEN,)),
            Embedding(input_dim=MAX_WORDS, output_dim=100),
            SpatialDropout1D(0.2),
            LSTM(100, dropout=0.2, recurrent_dropout=0.2),
            Dense(1, activation='sigmoid')
        ])
        model.summary()
        model.compile(loss=LOSS,optimizer=RMSprop(),metrics=METRICS)

        return model