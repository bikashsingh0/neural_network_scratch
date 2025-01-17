#!/bin/python3

import sys
sys.path.append('..')
from perceptron import Perceptron

inputLen = 3
learnRate = 0.1
bias = 1
p = Perceptron(inputLen,"sigmoid")

# Classification function to be used and pass to perceptron when training
# Kind of regresssion
def classification(x):
    if ( x < 0.5):
        return 0
    else:
        return 1

for i in range(20):
    inputs = [bias,0,0]
    target = 1
    p.train(inputs,target, learnRate, classification)
    inputs = [bias,0,1]
    target = 1
    p.train(inputs,target, learnRate, classification)
    inputs = [bias,1,0]
    target = 1
    p.train(inputs,target, learnRate, classification)
    inputs = [bias,1,1]
    target = 0
    p.train(inputs,target, learnRate, classification)

result = p.guess([bias,0,0])
output = classification(result)
print("After training => " + str(output))

result = p.guess([bias,0,1])
output = classification(result)
print("After training => " + str(output))

result = p.guess([bias,1,0])
output = classification(result)
print("After training => " + str(output))

result = p.guess([bias,1,1])
output = classification(result)
print("After training => " + str(output))
