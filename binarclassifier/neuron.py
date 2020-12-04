from typing import List, Any

import numpy as np
from perceptron import Perceptron


class Neuron(object):

    def __init__(self, neuron_type):
        self.neuron_type = neuron_type
        self.weights = []

    def train(self):
        if self.neuron_type == 'AND':
            training_inputs = [np.array([1, 1]),
                               np.array([1, 0]),
                               np.array([0, 1]),
                               np.array([0, 0])]

            labels = np.array([1, 0, 0, 0])
            self.perceptron = Perceptron(2)
            self.perceptron.train(training_inputs, labels)

            self.save_neuron(self.neuron_type)

        elif self.neuron_type == 'OR':

            training_inputs = [np.array([1, 1]),
                               np.array([1, 0]),
                               np.array([0, 1]),
                               np.array([0, 0])]

            labels = np.array([1, 1, 1, 0])

            self.perceptron = Perceptron(2)
            self.perceptron.train(training_inputs, labels)
            self.save_neuron(self.neuron_type)

        elif self.neuron_type == 'NOT':

            training_inputs = [np.array([1]),
                               np.array([0])]

            labels = np.array([0, 1])

            self.perceptron = Perceptron(1)
            self.perceptron.train(training_inputs, labels)
            self.save_neuron(self.neuron_type)

        elif self.neuron_type == 'NOR':

            training_inputs = [np.array([0, 0]),
                               np.array([0, 1]),
                               np.array([1, 0]),
                               np.array([1, 1])]

            labels = np.array([1, 0, 0, 0])
            self.perceptron = Perceptron(2)
            self.perceptron.train(training_inputs, labels)

            self.save_neuron(self.neuron_type)

        elif self.neuron_type == 'NAND':

            training_inputs = [np.array([0, 0]),
                               np.array([0, 1]),
                               np.array([1, 0]),
                               np.array([1, 1])]

            labels = np.array([1, 1, 1, 0])
            self.perceptron = Perceptron(2)
            self.perceptron.train(training_inputs, labels)

            self.save_neuron(self.neuron_type)

        elif self.neuron_type == 'XNOR':

            training_inputs = [np.array([0, 0]),
                               np.array([0, 1]),
                               np.array([1, 0]),
                               np.array([1, 1])]

            labels = np.array([1, 0, 0, 1])
            self.perceptron = Perceptron(2)
            self.perceptron.train(training_inputs, labels)

            self.save_neuron(self.neuron_type)

        elif self.neuron_type == 'XOR':

            training_inputs = [np.array([0, 0]),
                               np.array([0, 1]),
                               np.array([1, 0]),
                               np.array([1, 1])]

            labels = np.array([0, 1, 1, 0])
            self.perceptron = Perceptron(2)
            self.perceptron.train(training_inputs, labels)

            self.save_neuron(self.neuron_type)

        elif self.neuron_type == 'IMPLY':

            training_inputs = [np.array([0, 0]),
                               np.array([0, 1]),
                               np.array([1, 0]),
                               np.array([1, 1])]

            labels = np.array([1, 1, 0, 1])
            self.perceptron = Perceptron(2)
            self.perceptron.train(training_inputs, labels)

            self.save_neuron(self.neuron_type)

    def elicit_weights(self):
        if not self.weights:
            with open(self.neuron_type + ".txt") as file:
                for line in file:
                    line = line.strip()
                    self.weights.append(float(line))  # storing everything in memory!
        return self.weights

    @staticmethod
    def elicit_neuron(neuron_type):
        new_neuron = Neuron(neuron_type)
        new_neuron.weights = new_neuron.elicit_weights()
        return new_neuron

    def predict(self, inputs):
        weights = self.elicit_weights()
        weights = np.array(weights)
        summation = np.dot(inputs, weights[1:]) + weights[0]
        if summation > 0:
            return 1
        else:
            return 0

    def save_neuron(self, neuron_type):
        with open(neuron_type + '.txt', 'w') as f:
            for item in self.perceptron.weights:
                f.write("%s\n" % item)

