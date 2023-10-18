# 2 Layer Neural Network in NumPy
"""What is this"""
import numpy as np

# X = input of our 3 input XOR gate
# set up the inputs of the neural netwrok (right from the table)
X = np.array(([0,0,0],[0,0,1],[0,1,0],  \
    [0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]), dtype=float)
# y = our output of our neural network
y = np.array(([1], [0], [0], [0], [0], \
    [0], [0], [1]), dtype=float)

# what value we want to predict
xPredicted = np.array(([0,0,1]), dtype=float)

X = X/np.amax(X, axis=0) # maximum of X input array
# maximum of xPredicted (our input data for the prediction)
xPredicted = xPredicted/np.amax(xPredicted, axis=0)

# set up our Loss file for graphing

lossFile = open("sumSquaredLoss List.csv", "w")
