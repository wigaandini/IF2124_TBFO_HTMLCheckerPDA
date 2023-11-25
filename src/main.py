import re

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

        if closing_tag:
            filtered_matches.append('/' + closing_tag)

        if comment_content:
            continue

    return filtered_matches

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
    html_file_path = input("Enter the file name for HTML (.html): ")
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # tokenize html
    filename = pda_file_path.split('/')[-1]
    html_tags = tokenize_html_with_regex(html_content)
    print("")
    print("HTML tags found in " + filename + ":")
    print(html_tags)
    print("")

    state = pda_matrix[0][0]
    for tag in html_tags:
        found = False
        for row in pda_matrix:
            if tag == row[1] and state == row[0]:
                found = True
                state = row[3]
                break

        if not found:
            print(f"Error: Tag '{tag}' is not valid because the previous tag isn't complete.")
            break

    print("Final state:", state)

    if state == "FINAL":
        print("Accepted.")
    else:
        print("Syntax Error.")
