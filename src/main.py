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
    # regular expression pattern untuk HTML tags and attributes
    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9\-]+)\s*([^>]*)\s*(\/)?>|<\/\s*([a-zA-Z0-9\-]+)\s*>')

    matches = tag_pattern.findall(html_content)
    filtered_matches = []
    for opening_tag, attributes, self_closing_tag, closing_tag in matches:
        if attributes:
            # hilangin isi dari attributes, karena semua dianggap valid
            # misal id= 'sesuatu', sesuatunya itu gaperlu diperhatiin jadi yang di keep cuman id= ''
            attributes = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', '', attributes)
        if closing_tag:
            closing_tag = '/' + closing_tag
        filtered_matches.append((opening_tag, attributes, self_closing_tag, closing_tag))

    return filtered_matches

################## MAIN ##################
if __name__ == "__main__":
    # baca file pda
    file_path = "pda.txt"
    pda_matrix = read_txt_to_matrix(file_path)
    #print(pda_matrix)

    # baca file html
    file_path = 'text.html'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # tokenize html
    html_tags = tokenize_html_with_regex(html_content)
    #print(html_tags)
    for opening_tag, attributes, self_closing_tag, closing_tag in html_tags:
        if opening_tag:
            if self_closing_tag:
                print(f'Self-closing Tag: {self_closing_tag}, Attributes: {attributes}')
            else:
                print(f'Tag: {opening_tag}, Attributes: {attributes}')
        else:
            print(f'Closing Tag: {closing_tag}, Attributes:')

    opening_tags = [opening_tag for opening_tag, attributes, _, _ in html_tags if opening_tag and not '/' in attributes]
    closing_tags = [closing_tag for _, _, _, closing_tag in html_tags if closing_tag and '/' in closing_tag]
    self_closing_tags = [self_closing_tag for self_closing_tag, attributes, _, _ in html_tags if self_closing_tag and '/' in attributes]
    # print(len(opening_tags))
    print("opening_tags : ")
    print(opening_tags)
    print("closing_tags : ")
    print(closing_tags)
    print("self closing_tags : ")
    print(self_closing_tags)
        
    # print tags and attributes
    # for opening_tag, attributes, closing_tag in html_tags:
    #     if opening_tag:
    #         print(f'Tag: {opening_tag}, Attributes: {attributes}')
    #     else:
    #         print(f'Tag: {closing_tag}, Attributes:')


    # udah pasti ga sama
    if len(opening_tags) != len(closing_tags):
        print("Syntax Error")
    else:
        state = pda_matrix[0][0]
        for self_closing_tag in self_closing_tags:
            self_closing_tag_valid = False
            for row in pda_matrix:
                if self_closing_tag == row[1]:
                    self_closing_tag_valid = True
                    state = row[3]
            if not self_closing_tag_valid:
                print(f"Error: Self closing tag '{self_closing_tag}' is not valid.")
                      

        for opening_tag in opening_tags:
            found_opening = False
            for row in pda_matrix:
                if opening_tag == row[1]:
                    found_opening = True
                    state = row[3]
                    break
            if not found_opening:
                print(f"Error: Opening tag '{opening_tag}' is not valid.")

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


        #print("Final state:", state)
        if state == "FINAL" and self_closing_tag_valid:
            print("Accepted.")
        else:
            print("Syntax Error.")