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
    # Define the regular expression pattern for HTML tags and attributes
    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9\-]+)\s*([^>]*)>|<\/\s*([a-zA-Z0-9\-]+)\s*>')

    # Find all matches of the pattern in the HTML content
    matches = tag_pattern.findall(html_content)

    # Filter out the content within quotes in attributes
    filtered_matches = []
    for opening_tag, attributes, closing_tag in matches:
        if attributes:
            # Remove content within quotes
            attributes = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', '', attributes)
        if closing_tag:
            closing_tag = '/' + closing_tag
        filtered_matches.append((opening_tag, attributes, closing_tag))

    return filtered_matches

################## MAIN ##################
if __name__ == "__main__":
    # baca file pda
    file_path = "pda.txt"
    my_matrix = read_txt_to_matrix(file_path)
    # print(my_matrix[0])

    # baca file html
    file_path = 'text.html'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # tokenize html
    html_tags = tokenize_html_with_regex(html_content)

    closing_tags = [closing_tag for _, _, closing_tag in html_tags if closing_tag]
    # print(closing_tags)

    # print tags and attributes
    for opening_tag, attributes, closing_tag in html_tags:
        if opening_tag:
            print(f'Tag: {opening_tag}, Attributes: {attributes}')
        else:
            print(f'Tag: {closing_tag}, Attributes:')
