"""
turing mahcine is a mathematical model. it is not a machine.
It consists only of few components::
1. A Tape on which data can be sequentially stored. It has no limits.
2. A TM also contains a head moving in both directions over the tape.
A turing program is a list of transitions which determine for a given state and character a new state.
It consists of seven tuples.
"""

class Tape(object):
    blank_symbol = " "

    def __init__(self, tape_string = ""):
        self.__tape = dict((enumerate(tape_string)))

    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys())
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s

    def __getitem__(self, index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char

class TuringMachine(object):
    def __init__(self,
                 tape = "",
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        return str(self.__tape)

    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == 'R':
                self.__head_position += 1
            elif y[2] == 'L':
                self.__head_position -= 1
            self.__current_state = y[0]

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False

# using the Turing Machine class

initial_state = 'init'
accepting_states = ['final']
transition_function = {('init','0'):('init','1','R'),
                       ('init','1'):('init','0','R'),
                       ('init',' '):('final',' ','N')
                       }

final_states = {'final'}

t = TuringMachine('010011 ',
                  initial_state = 'init',
                  final_states = final_states,
                  transition_function = transition_function)

print('input on tape:\n' + t.get_tape())

while not t.final():
    t.step()


print('result of turing machine calculaiton:')

print(t.get_tape())
        
