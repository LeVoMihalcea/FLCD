import re

from FiniteAutomata import FiniteAutomata

reservedWords = ['read', 'write', 'not', 'break', 'start', 'Char', 'continue', 'do', 'else',
                 'float', 'for', 'while', 'if', 'pass', 'return', 'Integer', 'String', 'Float', 'Boolean']
reservedOperatorsSeparators = ['+', '-', '*', '/', '%', '=', '==', '!=', '>=', '<=', '>', '<', '[', ']',
                               '{', '}', '(', ')', ';', ':', ' ', '"', "&&", "||", '"']

def is_float_or_identifier(token):
    try:
        if (token[0] == '0' and (len(token) > 1 or token[1] == '.')):
            return False
        float(token)
    except:
        return re.search("[a-zA-Z0-9 \.\&]*", token).group()
    return True


def readFiniteAutomata():
    with open('input.txt', 'r') as f:
        states = f.readline().strip().split(' ')
        alphabet = f.readline().strip().split(' ')
        start = f.readline().strip().split(' ')
        finals = f.readline().strip().split(' ')
        aux_transitions = f.readline().strip().split(';')
        transitions = {}
        for transition in aux_transitions:
            transition = transition.split(' ')
            transitions[(transition[0], transition[1])] = transition[2]

        finiteAutomata = FiniteAutomata(states, alphabet, start, finals, transitions)

        print(finiteAutomata)




readFiniteAutomata()