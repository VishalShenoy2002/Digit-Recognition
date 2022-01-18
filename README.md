# Digit-Recognition

Handwritten digit recognition is the ability of a computer to recognize the human handwritten digits from different sources like images, papers, touch screens, etc, and classify them into 10 predefined classes (0-9).

The Program is written using the Python Programming Language. It uses the following Python Libraries:
1. Tensorflow
2. Numpy
3. OS
4. Open Cv (cv2)
5. Matplotlib


## Steps to Follow

Please Follow the following steps to run the program without error:
1. First Check if all the modules or libraries are installed. If not run the following command
``` 
pip install tensorflow numpy opencv-python mathplotlib os
```

2. Once all the Libraries or Modules are Installed run the following command.
```
python .\model.py
```

This will train and creae the model.

3. Once the Model is created, run the main program.
```
python .\main.py
```

***Note:***
The Pics folder contains 85 hand written images which are of 28x28 pixels in size.
If you want to use your own pictures you can add it in the Pics folder but make sure it is 28x28 pixels in size.



## Summary Of the Model
The Model has 3 Layers. They are as follows:
1. Flatten Layer
2. Dense Layer
3. Dense Layer

The Summary Table is given below


```Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 flatten (Flatten)           (None, 784)               0

 dense (Dense)               (None, 128)               100480

 dense_1 (Dense)             (None, 10)                1290

=================================================================
Total params: 101,770
Trainable params: 101,770
Non-trainable params: 0
_________________________________________________________________
```

