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
    # regular expression pattern for HTML tags and attributes
    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9\-]+)\s*([^>]*)>|<\/\s*([a-zA-Z0-9\-]+)\s*>')

    matches = tag_pattern.findall(html_content)
    filtered_matches = []
    for opening_tag, attributes, closing_tag in matches:
        # Append the opening tag after processing attributes, but only if it is not an empty string
        if opening_tag:
            filtered_matches.append(opening_tag)

        if attributes:
            # Remove content within quotes
            attributes = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', '', attributes)
            filtered_matches.append(attributes)

        if closing_tag:
            # Include the closing tag in the format '/closing_tag'
            filtered_matches.append('/' + closing_tag)

    return filtered_matches


################## MAIN ##################
if __name__ == "__main__":
    # baca file pda
    file_path = "src/pda.txt"
    pda_matrix = read_txt_to_matrix(file_path)
    # print(pda_matrix[0])

    # baca file html
    file_path = 'src/text.html'
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

    if (state == "FINAL"):
        print("Accepted.")
    else:
        print("Syntax Error.")

        