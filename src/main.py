import re
from pathlib import Path

################## READ .HMTL ##################
def get_HTML_path(html_file_name):
    path = Path().absolute()
    pathFile = str(path) + "/../test/" + html_file_name
    return pathFile

################## READ PDA.TXT ##################
def read_txt_to_matrix(file_path):
    matrix = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        tokens = line.split()
        matrix.append(tokens)

    return matrix

################## TOKENIZER ##################
def tokenize_html_with_regex(html_content):
    # regular expression pattern excluding comments (including multiline comments)
    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9\-]+)\s*([^>]*)>|<\/\s*([a-zA-Z0-9\-]+)\s*>|<!--(.*?)-->', re.DOTALL)

    matches = tag_pattern.findall(html_content)
    filtered_matches = []
    method_values = []
    input_types = []
    button_types = []

    for opening_tag, attributes, closing_tag, comment_content in matches:
        if opening_tag:
            filtered_matches.append(opening_tag)

        if attributes:
            attribute_names = re.findall(r'(\S+?=)(?:"(.*?)"|\'(.*?)\'|(.*?))(?=\s|$)', attributes)
            for attr_name, double_quoted, single_quoted, unquoted in attribute_names:
                filtered_matches.append(attr_name)
                if double_quoted:
                    filtered_matches.append('"')
                    filtered_matches.append('"')
                elif single_quoted:
                    filtered_matches.append("'")
                    filtered_matches.append("'")
                elif unquoted:
                    filtered_matches.append(unquoted)

                # check for method attribute
                if opening_tag.lower() == 'form' and attr_name.lower() == 'method=':
                    method_values.append(double_quoted or single_quoted or unquoted)

                # check for input type attribute
                if opening_tag.lower() == 'input' and attr_name.lower() == 'type=':
                    input_types.append(double_quoted or single_quoted or unquoted)

                # check for input type attribute
                if opening_tag.lower() == 'button' and attr_name.lower() == 'type=':
                    button_types.append(double_quoted or single_quoted or unquoted)

        if closing_tag:
            filtered_matches.append('/' + closing_tag)

        if comment_content:
            continue

    return filtered_matches, method_values, input_types, button_types

################## ATTRIBUTES FOR FORM-METHOD, INPUT TYPES, BUTTON TYPES ##################
def add_method_values(html_arr, method_values):
    i = 0
    j = 0
    while i < len(html_arr):
        if html_arr[i] == 'method=' and html_arr[i + 1] == '"':
            html_arr.insert(i + 2, method_values[j])
            i += 3
            j += 1
        else:
            i += 1

def add_input_types(html_arr, input_types):
    i = 0
    j = 0
    while i < len(html_arr):
        if html_arr[i] == 'input' and html_arr[i + 1] == 'type=' and html_arr[i + 2] == '"':
            html_arr.insert(i + 3, input_types[j])
            i += 4
            j += 1
        i += 1

def add_button_types(html_arr, button_types):
    i = 0
    j = 0
    while i < len(html_arr):
        if html_arr[i] == 'button' and html_arr[i + 1] == 'type=' and html_arr[i + 2] == '"':
            html_arr.insert(i + 3, button_types[j])
            i += 4
            j += 1
        i += 1

################## MAIN ##################
if __name__ == "__main__":

    ascii_art = '''
    _  _    _____  __  __    _                ___    _  _     ___     ___    _  __    ___     ___   
    | || |  |_   _||  \/  |  | |       o O O  / __|  | || |   | __|   / __|  | |/ /   | __|   | _ \  
    | __ |    | |  | |\/| |  | |__    o      | (__   | __ |   | _|   | (__   | ' <    | _|    |   /  
    |_||_|   _|_|_ |_|__|_|  |____|  TS__[O]  \___|  |_||_|   |___|   \___|  |_|\_\   |___|   |_|_\  
    |"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
    "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
    '''

    # print intro
    for line in ascii_art.split('\n'):
        print(line)
    
    print("Welcome to HTML Checker!")

    # baca file pda
    pda_file_path = "pda.txt"
    pda_matrix = read_txt_to_matrix(pda_file_path)

    # baca file html
    print("")
    # cek filenya exist/tidak
    html_file_name = input("Enter the file name for HTML (.html): ")
    html_file_path = get_HTML_path(html_file_name)
    
    while not Path(html_file_path).exists():
        print(f"\nError: File '{html_file_name}' does not exist in 'test' folder.")
        html_file_name = input("Enter the file name for HTML (.html): ")
        html_file_path = get_HTML_path(html_file_name)

    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # tokenize html
    filename = pda_file_path.split('/')[-1]
    html_tags, method_values, input_types, button_types = tokenize_html_with_regex(html_content)
    add_method_values(html_tags, method_values)
    add_input_types(html_tags, input_types)
    add_button_types(html_tags, button_types)
    print("")
    print("HTML tags found in " + filename + ":")
    print(html_tags)
    print("")

    state = pda_matrix[0][0]
    for tag in html_tags:
        found = False
        for row in pda_matrix:
            if tag == row[1] and state == row[0]:
                print("Processing " + tag + "...")
                found = True
                state = row[3]
                print("Current state:", state)
                break
            
        if not found:
            # print(f"Error: Tag '{tag}' is not valid because the previous tag isn't complete.")
            break

    print("")
    print("Final state:", state)

    if state == "FINAL":
        print("Accepted.")
    else:
        print("Syntax Error.")