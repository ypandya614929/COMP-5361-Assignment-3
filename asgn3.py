#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        state_list = self.getStates()
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
        state_list = self.getStates()
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
        state_list = self.getStates()
        alphabets_list = self.getAlphabet()
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
        state_list = self.getStates()
        alphabets_list = self.getAlphabet()
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
        print("\n===== Transition(s) =====")
        for transition in self.getTransitions():
            print("{} => {} => {}".format(transition[0], transition[1], transition[2]))
        self.setData("transitions", transitions_list)

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
                is_exit = True

        elif choice in ["3", 3]:
            is_exit = True

        else:
            print("\n========== Please select valid option ==========")
