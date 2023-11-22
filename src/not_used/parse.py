# def parse_pda_text(text):
#     transitions = {}
#     lines = text.strip().split('\n')

#     for line in lines:
#         parts = line.split()
#         if len(parts) < 5:
#             continue

#         current_state = parts[0]
#         input_symbol = parts[1]
#         stack_top = parts[2]
#         next_state = parts[3]
#         stack_update = parts[4]
#         transition_key = (current_state, input_symbol, stack_top, next_state, stack_update)
#         transitions[transition_key] = transition_key

#     return transitions

# def create_transition_matrix(transitions):
#     states = set()
#     inputs = set()
#     matrix = {}

#     for (current_state, input_symbol, stack_top), (next_state, stack_update) in transitions.items():
#         states.add(current_state)
#         inputs.add(input_symbol)
#         matrix[(current_state, input_symbol, stack_top)] = f"{stack_update}{next_state}"

#     states = sorted(list(states))
#     inputs = sorted(list(inputs))

#     # Create an empty matrix
#     num_states = len(states)
#     num_inputs = len(inputs)
#     matrix_repr = [['' for _ in range(num_inputs + 1)] for _ in range(num_states + 1)]

#     # Fill in the first row and first column
#     matrix_repr[0][0] = 'STATE'
#     matrix_repr[0][1:] = inputs
#     for i, state in enumerate(states):
#         matrix_repr[i + 1][0] = state

#     # Fill in the matrix with transition values
#     for i, state in enumerate(states):
#         for j, input_symbol in enumerate(inputs):
#             stack_top = matrix.get((state, input_symbol, 'Z0'), '')
#             matrix_repr[i + 1][j + 1] = f"{stack_top}{state}"

#     return matrix_repr

# # Read the text from the file
# file_path = 'src/pdafix.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
#     pda_text = file.read()

# # Parse the PDA text
# transitions = parse_pda_text(pda_text)

# # Access the first element
# first_transition_key = (list(transitions.keys())[0])[1]
# print("First transition:", first_transition_key)

# # Create and print the transition matrix
# transition_matrix = create_transition_matrix(transitions)
# for row in transition_matrix:
#     print(row)


def parse_pda_text(text):
    transitions = {}
    lines = text.strip().split('\n')

    for line in lines:
        parts = line.split()
        if len(parts) < 5:
            continue

        current_state = parts[0]
        input_symbol = parts[1]
        stack_top = parts[2]
        next_state = parts[3]
        stack_update = parts[4]

        transitions[(current_state, input_symbol, stack_top)] = (next_state, stack_update)

    return transitions

def create_transition_matrix(transitions):
    states = set()
    inputs = set()
    matrix = {}

    for (current_state, input_symbol, stack_top), (next_state, stack_update) in transitions.items():
        states.add(current_state)
        inputs.add(input_symbol)
        matrix[(current_state, input_symbol, stack_top)] = f"{stack_update}{next_state}"

    states = sorted(list(states))
    inputs = sorted(list(inputs))

    # Create an empty matrix
    num_states = len(states)
    num_inputs = len(inputs)
    matrix_repr = [['' for _ in range(num_inputs + 1)] for _ in range(num_states + 1)]

    # Fill in the first row and first column
    matrix_repr[0][0] = 'STATE'
    matrix_repr[0][1:] = inputs
    for i, state in enumerate(states):
        matrix_repr[i + 1][0] = state

    # Fill in the matrix with transition values
    for i, state in enumerate(states):
        for j, input_symbol in enumerate(inputs):
            stack_top = matrix.get((state, input_symbol, 'Z0'), '')
            matrix_repr[i + 1][j + 1] = f"{stack_top}{state}"

    return matrix_repr

# Read the text from the file
file_path = 'src/pdafix.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    pda_text = file.read()

# Parse the PDA text
transitions = parse_pda_text(pda_text)

# Create and print the transition matrix
transition_matrix = create_transition_matrix(transitions)
print(transition_matrix)
