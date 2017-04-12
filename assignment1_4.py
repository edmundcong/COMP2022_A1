import sys

# our hardcoded minimal DFA
invalid_flag = False
alphabet = {'a', 'b'}
minimal_dfa = {'ajk':{'a':'bldg','b':'c'}, 'bldg':{'a':'bldg','b':'eh'}, 'c':{'a':'f', 'b':'f'}, 'f':{'a':'ajk', 'b':'m'}, 'eh':{'a':'bldg','b':'i'}, 'i':{'a':'ajk','b':'f'},'m':{'a':'m','b':'m'}}
current_state = 'ajk' # our initial state which is reused in our loop as our current state
accepting_states = {'ajk', 'bldg', 'eh'} # set of accepting states
input_string = str(sys.argv[1]) # get the first CLI argument
for index, token in enumerate(input_string): # iterate through each character in our string
    output = token + " " + current_state + " -- "
    if not token in alphabet: # if our character isn't in the alphabet then set run as error
        result = 'ERROR_INVALID_SYMBOL'
        invalid_flag = True
        break
    # transition form our current state to the next state with the given transition value
    current_state = minimal_dfa[current_state][token]
    # format: scanned_input from_state -- symbol --> to_state unscanned_input
    output+= current_state + " " + input_string[index:]
    print(output)
if not invalid_flag: # cannot be accepted or rejected if it's invalid
    if current_state in accepting_states:
        result = 'ACCEPTED'
    else:
        result = 'REJECTED'
print(result)
