import re

def tokenize_html_with_regex(html_content):
    # Define the regular expression pattern for HTML tags and attributes
    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9\-]+)\s*([^>]*)\s*>|<\/\s*([a-zA-Z0-9\-]+)\s*>')

    # Find all matches of the pattern in the HTML content
    matches = tag_pattern.findall(html_content)

    return matches

def pda_acceptance(html_tags):
    # PDA configuration
    productions = {
        'q0': [('html', '', 'S', 'q1')],
        'q1': [('', 'S', '', 'q2')],
        'q2': [('head', '', '', 'q3')],
        'q3': [('title', '', '', 'q4')],
        'q4': [('', '', '', 'q5')],
        'q5': [('/title', '', '', 'q6')],
        'q6': [('', '', '', 'q7')],
        'q7': [('/head', '', '', 'q8')],
        'q8': [('', '', '', 'q9')],
        'q9': [('body', '', '', 'q10')],
        'q10': [('', '', '', 'q11')],
        'q11': [('p', '', '', 'q12')],
        'q12': [('', '', '', 'q13')],
        'q13': [('/p', '', '', 'q14')],
        'q14': [('', '', '', 'q15')],
        'q15': [('/body', '', '', 'q16')],
        'q16': [('', '', '', 'q17')],
        'q17': [('/html', '', '', 'q_accept')],
        'q_accept': []
    }

    start_symbol = 'q0'
    start_stack = 'Z0'
    acceptable_states = ['q_accept']
    accept_with = 'E'  # Accept on empty stack

    # PDA variables
    state = start_symbol
    input_str = ''
    stack = start_stack

    for tag, attributes, closing_tag in html_tags:
        # Print current configuration
        print(f'State: {state}, Input: {input_str}, Stack: {stack}')

        # Check if the current configuration is accepted
        if state in acceptable_states and accept_with == 'E' and stack == '':
            print('Input accepted!')
            return

        # Find applicable production rules
        moves = get_moves(state, input_str, stack, productions)
        if len(moves) == 0:
            print('No valid moves!')
            return

        # Choose the first valid move
        move = moves[0]

        # Apply the move
        state = move[0]
        input_str = move[1]
        stack = move[2]

    print('Input not accepted!')

def get_moves(state, input_str, stack, productions):
    moves = []

    for production in productions.get(state, []):
        new_state = production[3]
        new_input = input_str[len(production[0]):]
        new_stack = stack[:-len(production[1])] + production[2]

        moves.append((new_state, new_input, new_stack))

    return moves

def main():
    # Read HTML file
    file_path = 'src/text.html'  # Replace with the path to your HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Tokenize HTML using regular expressions
    html_tags = tokenize_html_with_regex(html_content)

    # PDA Acceptance
    pda_acceptance(html_tags)

if __name__ == "__main__":
    main()
