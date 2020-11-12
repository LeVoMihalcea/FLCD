class FiniteAutomata:
    states = []
    alphabet = []
    start = ''
    finals = []
    transitions = {}

    def __init__(self, states, alphabet, start, finals, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start = start
        self.finals = finals
        self.transitions = transitions

    def __str__(self):
        toReturn  = 'FA{\n'
        toReturn += 'states: ' + str(self.states) + '\n'
        toReturn += 'start: ' + str(self.start) + '\n'
        toReturn += 'finals: ' + str(self.finals) + '\n'
        toReturn += 'transitions' + str(self.transitions) + '\n'
        return toReturn
