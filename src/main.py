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
    # regular expression pattern
    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9\-]+)\s*([^>]*)>|<\/\s*([a-zA-Z0-9\-]+)\s*>')

    matches = tag_pattern.findall(html_content)
    filtered_matches = []
    for opening_tag, attributes, closing_tag in matches:
        # append opening tag after processing attributes, only if it's not empty
        if opening_tag:
            filtered_matches.append(opening_tag)

        if attributes:
            # extract attribute with '=' and optional double quotes
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
            # include closing tag
            filtered_matches.append('/' + closing_tag)

    return filtered_matches

################## MAIN ##################
if __name__ == "__main__":
    # baca file pda
    file_path = "pda.txt"
    pda_matrix = read_txt_to_matrix(file_path)

    # baca file html
    file_path = 'text.html'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # tokenize html
    html_tags = tokenize_html_with_regex(html_content)
    print(html_tags)

    state = pda_matrix[0][0]
    for tag in html_tags:
        found = False
        for row in pda_matrix:
            if tag == row[1] and state == row[0]:
                found = True
                state = row[3]
                break

        if not found:
            print(f"Error: Tag '{tag}' is not valid.")
            break

    print("Final state:", state)

    if state == "FINAL":
        print("Accepted.")
    else:
        print("Syntax Error.")
