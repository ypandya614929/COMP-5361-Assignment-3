# COMP-5361-Assignment-3
COMP-5361-Assignment-3

## To setup virtualenv if not already
    
    virtualenv -p python3.6 env
    source env/bin/activate
    pip install pysimpleautomata 

## Run Program
#### python asgn2.py

    - When the rogram runs user is displayed with following menu in the console
    
        COMP-5361 Assignment-3 Menu
        -------------------------------------------------------
        1. Produce Transition Diagram from Transition table
        2. Produce DFA Transition Diagram and Transition table from NFA Transition table
        3. Exit
        
        Select: 1


    - The user need to select any one of the available option at a time, otherwise 
      it will raise an error for invalid choice.

    - After selecting choice 1 user need to select another choice on what user wants go 
      generate a NFA or a DFA.

        Transition Table Generation Menu
        -------------------------------------------------------
        1. NFA
        2. DFA
        3. Exit
        
        Select: 1
    
    - After selecting making selection, interactive console input begins where user need
      to give some input as shown below.
        
        Enter alphabet(s), if multiple then seperate by comma : 0,1

        ===== Alphabet(s) ===== :  0, 1
        
        Enter state(s), if multiple then seperate by comma : q0,q1,q2
        
        ===== State(s) ===== :  q0, q1, q2
        
        Enter number of initial state(s) : 1
        
        Available state(s) : q0, q1, q2
        Select the initial state 1 : q0
        
        ===== Initial state(s) ===== :  q0
        
        Enter number of accepting state(s) : 1
        
        Available state(s) : q0, q1, q2
        Select the accepting state 1 : q2
        
        ===== Accepting state(s) ===== :  q2
        
        Available state(s) : q0, q1, q2
        Select next state(s) === Note: if multiple then seperate by comma / 
        hit enter for leaving it empty
        
        q0 => 0 => (?) : q0,q1
        
        q0 => 1 => (?) : q0
        
        q1 => 0 => (?) : 
        
        q1 => 1 => (?) : q2 
        
        q2 => 0 => (?) : 
        
        q2 => 1 => (?) : 
        
        ===== Transition(s) =====

        q0 => 0 => q0
        q0 => 0 => q1
        q0 => 1 => q0
        q1 => 1 => q2

    - above is the interactive console result for selection 
      choice 1: Produce Transition Diagram from Transition table 
      It also produces either NFA or DFA based on selected choice and 
      save it into the same directory with file name "nfa" or "dfa".
   
   ![NFA](https://github.com/ypandya614929/COMP-5361-Assignment-3/blob/main/nfa.dot.svg?raw=true)
   
    - choice 2: Produce DFA Transition Diagram and Transition table from 
      NFA Transition table

    - Above selection also takes the same input as selection choice 1. However,
      It produces the equivalent DFA transition table and displays on the console.
      
        ==============================================================
        NFA To DFA Transition Table
        ==============================================================
                        0       1      
        =============== ======= =======
        ∅               ∅       ∅      
        {q0}            {q0,q1} {q0}   
        {q1}            ∅       {q2}   
        {q2}            ∅       ∅      
        {q0,q1}         {q0,q1} {q0,q2}
        {q0,q2}         {q0,q1} {q0}   
        {q1,q2}         ∅       {q2}   
        {q0,q1,q2}      {q0,q1} {q0,q2}
        ==============================================================

    - It also generates, equivalent DFA image within the same directory with name
      "dfa_Part2".
   
   ![NFA to Equivalent DFA](https://github.com/ypandya614929/COMP-5361-Assignment-3/blob/main/dfa_Part2.dot.svg?raw=true)
