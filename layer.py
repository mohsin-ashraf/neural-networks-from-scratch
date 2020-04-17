## From previous video
"""
inputs = [1, 2, 3]
wights = [0.2, 0.8, -0.5]
bias = 2

output = inputs[0] * wights[0] + inputs[1] * wights[1] + inputs[2] * wights[2] + bias

print ("Neuron output: {}".format(output))
"""
## Modeling the output layer neuron.

inputs = [1, 2, 3, 2.5]
wights = [0.2, 0.8, -0.5, 1.0]
bias = 2
output = inputs[0] * wights[0] + inputs[1] * wights[1] + inputs[2] * wights[2] + inputs[3] * wights[3] + bias
print ("Output layer single neuron: {}".format(output))


## Modeling 3 neurons with 4 inputs.


### Assuming the following input to be the output of a layer with 4 neurons
inputs = [1, 2, 3, 2.5]

wights1 = [0.2, 0.8, -0.5, 1.0]
wights2 = [0.5, -0.91, 0.26, -0.5]
wights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5

output = [inputs[0] * wights1[0] + inputs[1] * wights1[1] + inputs[2] * wights1[2] + inputs[3] * wights1[3] + bias1,
 inputs[0] * wights2[0] + inputs[1] * wights2[1] + inputs[2] * wights2[2] + inputs[3] * wights2[3] + bias2,
 inputs[0] * wights3[0] + inputs[1] * wights3[1] + inputs[2] * wights3[2] + inputs[3] * wights3[3] + bias3,
      ]


print ("Output of the layer: {}".format(output))
