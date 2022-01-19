# Importing Required Libraries
import tensorflow as tf
import tensorflow.keras as tfk
from tensorflow.keras import datasets
from tensorflow.keras.layers import Flatten,Dense
from tensorflow.keras import Sequential

from matplotlib import pyplot as plt

# Calling the MNIST Data Set which contains Pictures of Hand written digits
mnist=datasets.mnist

# Splitting the data into Testing set and Training Set
(x_train,y_train),(x_test,y_test)=mnist.load_data()

x_train=x_train/255.0
x_test=x_test/255.0

# Creating the Model 
    # Here we are creating a Sequential Model which will have 3 Layers i.e
    #     1.Flat Layer for Input 
    #     2. Dense Layer with 128 units and relu activation
    #     3. Dense Layer with 10 units and softmax activation

model=Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(128,activation="relu"))
model.add(Dense(10,activation="softmax"))

# Printing the Summary of the Model that was Created
model.summary()

# Compiling the Model
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

# Training the Model
model.fit(x_train,y_train,epochs=100)

# And Finally Saving the Model For Future Use.
model.save("number_recognition.model")
