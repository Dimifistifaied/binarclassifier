import neuron as nr


class Network:
    @staticmethod
    def create_network():
        or_neuron = nr.Neuron('OR')
        and_neuron = nr.Neuron('AND')
        not_neuron = nr.Neuron('NOT')
        nor_neuron = nr.Neuron('NOR')
        xor_neuron = nr.Neuron('XOR')
        nand_neuron = nr.Neuron('NAND')
        xnor_neuron = nr.Neuron('XNOR')
        imply_neuron = nr.Neuron('IMPLY')

        or_neuron.train()
        and_neuron.train()
        not_neuron.train()
        nor_neuron.train()
        xor_neuron.train()
        nand_neuron.train()
        xnor_neuron.train()
        imply_neuron.train()




