import re

def read_txt_to_matrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        tokens = line.split()
        matrix.append(tokens)
    return matrix

def tokenize_html_with_regex(html_content):
    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9\-]+)\s*([^>]*)\s*/?>|<\/\s*([a-zA-Z0-9\-]+)\s*>')
    matches = tag_pattern.findall(html_content)
    filtered_matches = []
    for opening_tag, attributes, closing_tag in matches:
        if attributes:
            attributes = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', '', attributes)
        if closing_tag:
            closing_tag = '/' + closing_tag
        filtered_matches.append((opening_tag, attributes, closing_tag))
    print(filtered_matches)
    return filtered_matches


if __name__ == "__main__":
    pda_file_path = "src/pdafix.txt"
    pda_matrix = read_txt_to_matrix(pda_file_path)

    html_file_path = 'src/text.html'
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    html_tags = tokenize_html_with_regex(html_content)

    opening_tags = [tag for tag, _, _ in html_tags if tag]
    closing_tags = [tag for _, _, tag in html_tags if tag]

    # Exclude tags that don't require closing
    tags_without_closing = {"br", "img", "hr", "input", "link", "!DOCTYPE", "!--"}
    opening_tags = [tag for tag in opening_tags if tag not in tags_without_closing]
    closing_tags = [tag for tag in closing_tags if tag not in tags_without_closing]
    print(opening_tags)
    print(closing_tags)
    print(tags_without_closing)

    if len(opening_tags) != len(closing_tags):
        print("Syntax Error")
    else:
        state = pda_matrix[0][0]
        for opening_tag in opening_tags:
            found_opening = False
            for row in pda_matrix:
                if opening_tag == row[1]:
                    found_opening = True
                    state = row[3]
                    break
            if not found_opening:
                print(f"Error: Opening tag '{opening_tag}' is not valid.")
                break

        if found_opening:
            for closing_tag in closing_tags:
                found_closing = False
                for row in pda_matrix:
                    if closing_tag == row[1]:
                        found_closing = True
                        state = row[3]
                        break
                if not found_closing:
                    print(f"Error: Closing tag '{closing_tag}' is not valid.")
                    break

        print("Final state:", state)

        if state == "FINAL":
            print("Accepted.")
        else:
            print("Syntax Error.")
