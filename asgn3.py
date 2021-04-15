#!/usr/bin/python
# -*- coding: utf-8 -*-

# References
# https://pysimpleautomata.readthedocs.io/en/latest/tutorial.html
# https://stackoverflow.com/questions/53526207/how-do-i-add-a-row-of-dashes-between-the-first-two-print-lines-in-python

from PySimpleAutomata import automata_IO
import json


class COMP5361:

    def __init__(self):
        self.data = {}
        self.alphabet = []
        self.states = []
        self.initial_states = []
        self.accepting_states = []
        self.transitions = []
        self.dfa_initial_states = []
        self.dfa_transitions = []
        self.dfa_result_transition = []
        self.dfa_states = []
        self.dfa_state_list = []
        self.dfa_result_states = []
        self.dfa_accepting_states = []

    def setData(self, key, value):
        self.data.update({key: value})

    def getData(self):
        return self.data

    def setAlphabet(self, alphabet):
        self.alphabet = sorted(alphabet)

    def getAlphabet(self):
        return self.alphabet

    def setStates(self, states):
        self.states = sorted(states)

    def getStates(self):
        return self.states

    def setInitialstates(self, initial_states):
        self.initial_states = sorted(initial_states)
        self.setDfainitialstates(self.getInitialstates())

    def getInitialstates(self, is_dfa=False):
        if is_dfa:
            if self.initial_states:
                return  self.initial_states[0]
        return self.initial_states

    def setAcceptingstates(self, accepting_states):
        self.accepting_states = sorted(accepting_states)

    def getAcceptingstates(self):
        return self.accepting_states

    def setTransitions(self, transitions):
        self.transitions = transitions

    def getTransitions(self):
        return self.transitions

    def setDfastate_list(self, state):
        self.dfa_state_list.append(state)

    def getDfastate_list(self):
        return self.dfa_state_list

    def setDfastates(self, state):
        self.dfa_states.append(state)

    def getDfastates(self):
        return self.dfa_states

    def setDfaresultstates(self, state):
        self.dfa_result_states.append(state)

    def getDfaresultstates(self):
        return self.dfa_result_states

    def setDfainitialstates(self, initial_states):
        self.dfa_initial_states = sorted(initial_states)

    def getDfainitialstates(self):
        if self.initial_states:
            return self.initial_states[0]
        return []

    def setDfaacceptingstates(self, accepting_state):
        self.dfa_accepting_states.append(accepting_state)

    def getDfaacceptingstates(self):
        return self.dfa_accepting_states

    def setDfatransitions(self, transition):
        self.dfa_transitions.append(transition)

    def getDfatransitions(self):
        return self.dfa_transitions

    def setDfaresulttransitions(self, transitions):
        self.dfa_result_transition.append(transitions)

    def getDfaresulttransitions(self):
        return self.dfa_result_transition

    def read_and_store_alphabets(self):
        alphabets = input("\nEnter alphabet(s), if multiple then seperate by comma : ")
        alphabets_list = [elem.strip() for elem in alphabets.split(",")]
        self.setAlphabet(alphabets_list)
        print("\n===== Alphabet(s) ===== : ", ", ".join(self.getAlphabet()))
        self.setData("alphabet", self.getAlphabet())

    def read_and_store_states(self):
        state = input("\nEnter state(s), if multiple then seperate by comma : ")
        state_list = [elem.strip() for elem in state.split(",")]
        self.setStates(state_list)
        print("\n===== State(s) ===== : ", ", ".join(self.getStates()))
        self.setData("states", self.getStates())

    def read_and_store_initial_states(self, is_dfa=False):
        num_of_initial_states = 0
        if is_dfa:
            num_of_initial_states = 1
        else:
            while num_of_initial_states == 0:
                try:
                    num_of_initial_states = int(input("\nEnter number of initial state(s) : "))
                except Exception:
                    num_of_initial_states = 0
                    print("===== Error: Please enter integer number =====")

        initial_states = []
        state_list = sorted(self.getStates())
        print("\nAvailable state(s) : {}".format(", ".join(state_list)))
        for count in range(num_of_initial_states):
            initial = None
            while True:
                if is_dfa:
                    initial = input("Select the initial state : ")
                else:
                    initial = input("Select the initial state {} : ".format(count + 1))
                if initial:
                    initial = initial.strip()
                if initial not in state_list:
                    print("\n===== Error: Please select initial state from the Available state(s) =====")
                else:
                    break
            initial_states.append(initial)

        self.setInitialstates(initial_states)
        print("\n===== Initial state(s) ===== : ", ", ".join(self.getInitialstates()))
        if is_dfa:
            self.setData("initial_state", self.getInitialstates(True))
        else:
            self.setData("initial_states", self.getInitialstates())

    def read_and_store_accepting_states(self):
        num_of_accepting_states = 0
        while num_of_accepting_states == 0:
            try:
                num_of_accepting_states = int(input("\nEnter number of accepting state(s) : "))
            except Exception:
                num_of_accepting_states = 0
                print("\n===== Error: Please enter integer number =====")

        accepting_states = []
        state_list = sorted(self.getStates())
        print("\nAvailable state(s) : {}".format(", ".join(state_list)))
        for count in range(num_of_accepting_states):
            accepting = None
            while True:
                accepting = input("Select the accepting state {} : ".format(count + 1))
                if accepting:
                    accepting = accepting.strip()
                if accepting not in state_list:
                    print("\n===== Error: Please select accepting state from the Available state(s) =====")
                else:
                    break
            accepting_states.append(accepting)

        self.setAcceptingstates(accepting_states)
        print("\n===== Accepting state(s) ===== : ", ", ".join(self.getAcceptingstates()))
        self.setData("accepting_states", accepting_states)

    def read_and_store_nfa_transitions(self):
        transitions_list = []
        state_list = sorted(self.getStates())
        alphabets_list = sorted(self.getAlphabet())
        print("\nAvailable state(s) : {}".format(", ".join(state_list)))
        print("Select next state(s) === Note: if multiple then seperate by comma / hit enter for leaving it empty")
        for state in state_list:
            for alphabet in alphabets_list:
                transited_state = ""
                while True:
                    print()
                    transited_state = input("{} => {} => (?) : ".format(state, alphabet))
                    transited_state = transited_state.strip()
                    if transited_state:
                        transited_state_list = [elem.strip() for elem in transited_state.split(",")]
                        for transition in transited_state_list:
                            if transition not in state_list:
                                print("\n===== Error: Please select next state from the Available state(s) =====")
                                break
                            else:
                                transitions_list.append([state, alphabet, transition])
                        else:
                            break
                    else:
                        break

        self.setTransitions(transitions_list)
        print("\n===== Transition(s) =====")
        for transition in self.getTransitions():
            print("{} => {} => {}".format(transition[0], transition[1], transition[2]))
        self.setData("transitions", self.getTransitions())

    def read_and_store_dfa_transitions(self):
        transitions_list = []
        state_list = sorted(self.getStates())
        alphabets_list = sorted(self.getAlphabet())
        print("\nAvailable state(s) : {}".format(", ".join(state_list)))
        print("Select next state(s) === Note: hit enter for leaving it empty")
        for state in state_list:
            for alphabet in alphabets_list:
                transited_state = ""
                while True:
                    print()
                    transited_state = input("{} => {} => (?) : ".format(state, alphabet))
                    transited_state = transited_state.strip()
                    if transited_state:
                        transited_state_list = [elem.strip() for elem in transited_state.split(",")]
                        if len(transited_state_list) > 1:
                            print("\n===== Error: Please select only 1 next state from the Available state(s) =====")
                            continue
                        for transition in transited_state_list:
                            if transition not in state_list:
                                print("\n===== Error: Please select next state from the Available state(s) =====")
                                break
                            else:
                                transitions_list.append([state, alphabet, transition])
                        else:
                            break
                    else:
                        break

        self.setTransitions(transitions_list)
        print("\n===== Transition(s) =====\n")
        for transition in self.getTransitions():
            print("{} => {} => {}".format(transition[0], transition[1], transition[2]))
        self.setData("transitions", transitions_list)

    def get_end_state(self, start, op):
        return_list = []
        for trans in self.getTransitions():
            if start == trans[0] and op == trans[1]:
                if trans[2] not in return_list:
                    return_list.append(trans[2])
        return ",".join(sorted(return_list))

    def update_transitions(self, state):
        start_states = state.split(",")
        for op in self.getAlphabet():
            end_state = []
            for start in start_states:
                for trans in self.getTransitions():
                    if start == trans[0] and op == trans[1]:
                        if trans[2] not in end_state:
                            end_state.append(trans[2])
            if end_state:
                self.transitions.append([state, op, ",".join(sorted(end_state))])

    def get_result_set_list(self, start):
        return_list = []
        for trans in self.getDfatransitions():
            if trans[0] == start:
                end_state = trans[-1]
                if end_state not in return_list:
                    return_list.append(end_state)
        return return_list

    def nfa_to_dfa_conversion(self):
        for state in self.getInitialstates(False):
            self.setDfastates(state)
            self.setDfastate_list(state)
        states = self.getStates()
        for state in states:
            if state not in self.getDfastates():
                self.setDfastate_list(state)
        for count, state in enumerate(states):
            for next_state in states[count + 1:]:
                new_state = ",".join([state, next_state])
                if new_state not in self.getDfastate_list():
                    self.setDfastate_list(new_state)
        new_state = ",".join(states)
        if new_state not in self.getDfastate_list():
            self.setDfastate_list(new_state)

        transitions_updated_list = states
        for state in self.getDfastate_list():
            for op in self.getAlphabet():
                if state not in transitions_updated_list:
                    transitions_updated_list.append(state)
                    self.update_transitions(state)

        for state in self.getDfastate_list():
            for op in self.getAlphabet():
                end_state = self.get_end_state(state, op)
                if end_state:
                    self.setDfatransitions([state, op, end_state])

        for state in self.getDfastates():
            result_list = self.get_result_set_list(state)
            for res_state in result_list:
                if res_state not in self.getDfaresultstates():
                    self.setDfaresultstates(res_state)
                if res_state not in self.getDfastates():
                    self.setDfastates(res_state)

        for state in self.getAcceptingstates():
            for res_state in self.getDfaresultstates():
                if state in res_state:
                    self.setDfaacceptingstates(res_state)
        for state in sorted(self.getDfaresultstates()):
            for trans in self.dfa_transitions:
                if trans[0] == state:
                    self.setDfaresulttransitions([trans[0], trans[1], trans[2]])

    def build_Data(self):
        self.setData("alphabet", self.getAlphabet())
        self.setData("initial_state", self.getDfainitialstates())
        self.setData("states", self.getDfaresultstates())
        self.setData("accepting_states", self.getDfaacceptingstates())
        self.setData("transitions", self.getDfaresulttransitions())

    def display_nfa_to_dfa_transition_table(self):
        display_list = []
        alphabet_display_list = []
        alphabet_display_list.append(" ")
        for op in self.getAlphabet():
            alphabet_display_list.append(op)
        display_list.append(alphabet_display_list)
        display_list.append(["=" * (15), "=" * (7), "=" * (7)])
        display_list.append(["∅", "∅", "∅"])
        key_dict = {}
        for state in self.getDfastate_list():
            key_dict.update({"{{{}}}".format(state): {}})
            for op in sorted(self.getAlphabet()):
                val_dict = key_dict.get("{{{}}}".format(state))
                val_dict.update({op: "∅"})

        for key, val_dict in key_dict.items():
            print_list = []
            print_list.append(key)
            for op_key, val in val_dict.items():
                for trans in self.getDfatransitions():
                    if "{{{}}}".format(trans[0]) == key and trans[1] == op_key:
                        val_dict.update({op_key: "{{{}}}".format(trans[2])})
                print_list.append(val_dict.get(op_key))
            display_list.append(print_list)

        dynamic_length = [max(map(len, colmn)) for colmn in zip(*[[str(word) for word in row] for row in display_list])]
        tab_formatted = '\t'.join('{{:{}}}'.format(var) for var in dynamic_length)
        display_table = [tab_formatted.format(*row) for row in [[str(word) for word in row] for row in display_list]]
        print("\n==============================================================")
        print('NFA To DFA Transition Table')
        print("==============================================================")
        print('\n'.join(display_table))
        print("==============================================================\n")

# python main method
if __name__ == '__main__':

    is_exit = False
    while not is_exit:
        print('\nCOMP-5361 Assignment-3 Menu')
        print("-------------------------------------------------------")
        print('1. Produce Transition Diagram from Transition table')
        print('2. Produce DFA Transition Diagram and Transition table from NFA Transition table')
        print('3. Exit\n')

        choice = input('Select: ')
        choice = choice.strip()

        if choice in ["1", 1, "2", 2]:

            is_dfa = False

            if choice in ["1", 1]:
                is_dfa_nfa_selection_exit = False
                while not is_dfa_nfa_selection_exit:
                    print('\nTransition Table Generation Menu')
                    print("-------------------------------------------------------")
                    print('1. NFA')
                    print('2. DFA')
                    print('3. Exit\n')
                    new_choice = input('Select: ')
                    new_choice = new_choice.strip()
                    if new_choice in ["1", 1, "2", 2]:
                        if new_choice in ["2", 2]:
                            is_dfa = True
                            is_dfa_nfa_selection_exit = True
                    else:
                        is_dfa_nfa_selection_exit = True
                        break

                    instance = COMP5361()
                    instance.read_and_store_alphabets()
                    instance.read_and_store_states()
                    if is_dfa:
                        instance.read_and_store_initial_states(True)
                        instance.read_and_store_accepting_states()
                        instance.read_and_store_dfa_transitions()
                    else:
                        instance.read_and_store_initial_states()
                        instance.read_and_store_accepting_states()
                        instance.read_and_store_nfa_transitions()

                    with open("Part1.json", "w") as file:
                        json.dump(instance.getData(), file)

                    if is_dfa:
                        dfa = automata_IO.dfa_json_importer('Part1.json')
                        automata_IO.dfa_to_dot(dfa, 'dfa')
                    else:
                        nfa = automata_IO.nfa_json_importer('Part1.json')
                        automata_IO.nfa_to_dot(nfa, 'nfa')

                    is_dfa_nfa_selection_exit = True
                    is_exit = True

            if choice in ["2", 2]:
                instance = COMP5361()
                instance.read_and_store_alphabets()
                instance.read_and_store_states()
                instance.read_and_store_initial_states()
                instance.read_and_store_accepting_states()
                instance.read_and_store_nfa_transitions()
                instance.nfa_to_dfa_conversion()
                instance.build_Data()
                instance.display_nfa_to_dfa_transition_table()

                with open("Part2.json", "w") as file:
                    json.dump(instance.getData(), file)

                dfa = automata_IO.dfa_json_importer('Part2.json')
                automata_IO.dfa_to_dot(dfa, 'dfa_Part2')

                is_exit = True

        elif choice in ["3", 3]:
            is_exit = True

        else:
            print("\n========== Please select valid option ==========")