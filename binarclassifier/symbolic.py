class Symbolic:
    def __init__(self):
        self.quantifiers = []
        self.connectives = []
        self.connectives_position_in_sentence = []
        self.connectives_operator_in_sentence = []
        self.next_variable = 0
        with open("Logical_connectives.txt") as file:
            for line in file:
                line = line.strip()
                self.connectives.append(line)
        with open("Quantifiers.txt") as file:
            for line in file:
                line = line.strip()
                self.quantifiers.append(line)

    def check_connectives(self, sentence):
        member_list = list(sentence.split(" "))
        position = 0
        for member in member_list:
            if member in self.connectives:
                self.connectives_position_in_sentence.append(position)
                position += 1
                self.connectives_operator_in_sentence.append(member)
        if len(self.connectives_operator_in_sentence) > 0:
            return True
        else:
            return False

    def check_quantifiers(self, sentence):
        member_list = list(sentence.split(" "))
        for member in member_list:
            if member in self.quantifiers:
                return False

        return True

    def evaluator(self, sentence):
        if self.check_connectives(sentence) and self.check_quantifiers(sentence):
            converted = self.symbolic_converter(sentence)

            self.connectives_operator_in_sentence.clear()
            self.connectives_position_in_sentence.clear()
            print(converted)
            return converted


        else:
            print("Sentence contains quantifiers or does not contains connectives")
            self.connectives_operator_in_sentence.clear()
            self.connectives_position_in_sentence.clear()

    # experimental
    def symbolic_converter(self, sentence):
        propositional_sentence = []
        return_sentence = ""
        for position, connective in zip(self.connectives_position_in_sentence, self.connectives_operator_in_sentence):
            propositional_sentence += self.symbolic_var() + " " + connective + " "
            self.next_variable += 1
        propositional_sentence += self.symbolic_var()
        self.next_variable = 0

        for ele in propositional_sentence:
            return_sentence += ele

        clear_list = list(return_sentence.split(" "))
        return_sentence = ""

        for ele in clear_list:
            if ele == 'then' or ele == 'if':
                if clear_list[clear_list.index(ele) + 2] == 'not':
                    clear_list.pop(clear_list.index(ele) + 1)
            if clear_list.index(ele) + 1 < len(clear_list):
                return_sentence += ele + " "
            else:
                return_sentence += ele

        return return_sentence

    def symbolic_var(self):
        list_variables = ['P', 'Q', 'R', 'A', 'B', 'C']
        return list_variables[self.next_variable]





