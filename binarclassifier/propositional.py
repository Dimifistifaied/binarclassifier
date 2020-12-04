from neuron import Neuron as nr
import numpy as np
class Propositional:
    def __init__(self):
        self.precedence_table = {'not': 1,
                                 'and': 2,
                                 'or': 3,
                                 'then': 4,
                                 'if': 5}

    def propositional_evaluation(self, sentence):
        list_sentence = list(sentence.split(" "))
        sequence = []

        for ele in list_sentence:
            if ele in self.precedence_table.keys():
                sequence.append(self.precedence_table.get(ele))
            else:
                list_sentence[list_sentence.index(ele)] = 1
        sequence.sort();
        for ele in sequence:
            list_sentence = self.fire_sequence(ele, list_sentence)

        print(list_sentence)

    def fire_sequence(self, sequence, list_sentence):

        if sequence == 1:
            for ele in list_sentence:
                if ele == 'not':
                    bul_operand = list_sentence[list_sentence.index(ele) + 1]
                    not_neuron = nr.elicit_neuron('NOT')
                    result = not_neuron.predict(np.array([bul_operand]))
                    list_sentence.pop(list_sentence.index(ele) + 1)
                    list_sentence[list_sentence.index(ele)] = result
                    print(list_sentence)

        if sequence == 2:
            for ele in list_sentence:
                if ele == 'and':
                    and_neuron = nr.elicit_neuron('AND')
                    result = and_neuron.predict(np.array([list_sentence[list_sentence.index(ele) + 1],
                                                          list_sentence[list_sentence.index(ele) - 1]]))
                    list_sentence.pop(list_sentence.index(ele) - 1)
                    list_sentence.pop(list_sentence.index(ele) + 1)
                    list_sentence[list_sentence.index(ele)] = result

                    print(list_sentence)

        if sequence == 3:
            for ele in list_sentence:
                if ele == 'or':
                    and_neuron = nr.elicit_neuron('OR')
                    result = and_neuron.predict(np.array([list_sentence[list_sentence.index(ele) + 1],
                                                          list_sentence[list_sentence.index(ele) - 1]]))
                    list_sentence.pop(list_sentence.index(ele) - 1)
                    list_sentence.pop(list_sentence.index(ele) + 1)
                    list_sentence[list_sentence.index(ele)] = result

                    print(list_sentence)

        if sequence == 4:
            for ele in list_sentence:
                if ele == 'then':
                    and_neuron = nr.elicit_neuron('IMPLY')
                    result = and_neuron.predict(np.array([list_sentence[list_sentence.index(ele) + 1],
                                                          list_sentence[list_sentence.index(ele) - 1]]))
                    list_sentence.pop(list_sentence.index(ele) - 1)
                    list_sentence.pop(list_sentence.index(ele) + 1)
                    list_sentence[list_sentence.index(ele)] = result

                    print(list_sentence)

        if sequence == 5:
            for ele in list_sentence:
                if ele == 'if':
                    and_neuron = nr.elicit_neuron('XNOR')
                    result = and_neuron.predict(np.array([list_sentence[list_sentence.index(ele) + 1],
                                                          list_sentence[list_sentence.index(ele) - 1]]))
                    list_sentence.pop(list_sentence.index(ele) - 1)
                    list_sentence.pop(list_sentence.index(ele) + 1)
                    list_sentence[list_sentence.index(ele)] = result

                    print(list_sentence)

        return list_sentence
