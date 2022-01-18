# Importing Required Modules
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2 as cv
import tensorflow.keras as tfk


# Loading the Model
model=tfk.models.load_model(os.path.join('number_recognition.model'))

# Clearing the Screen After the Model is Loaded
os.system('cls')

# Going throught the Pics directory to recognise the digits
for pic in os.listdir('Pics'):
    
    # Getting full path to open the image
    picpath=os.path.join('Pics',pic)
    
    # Reading the Image
    img=cv.imread(picpath)[:,:,0]
    
    # Converting the Image into an array and Inverting it
    img=np.invert(np.array([img]))

    # Predicting the Number that is present in the Image
    prediction=model.predict(img)

    # Printing the Prediction
    print("The Number is : {}".format(np.argmax(prediction)))
    
    # Displaying the Image with colour map of Binary i.e Black and White
    plt.imshow(img[0],cmap=plt.cm.binary)
    plt.show()

