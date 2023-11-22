import re

################## TOKENIZER ##################
# mendapatkan tags dari file html (.html)
def tokenize_html_with_regex(html_content):
    # regular expression pattern untuk HTML tags and attributes
    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9\-]+)\s*([^>]*)>|<\/\s*([a-zA-Z0-9\-]+)\s*>')

    # find all matches of the pattern in the HTML content
    matches = tag_pattern.findall(html_content)

    # filter out the content within quotes in attributes
    filtered_matches = []
    for opening_tag, attributes, closing_tag in matches:
        if attributes:
            # hilangin isi dari attributes, karena semua dianggap valid
            # misal id= 'sesuatu', sesuatunya itu gaperlu diperhatiin jadi yang di keep cuman id= ''
            attributes = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', '', attributes)
        filtered_matches.append((opening_tag, attributes, closing_tag))

    return filtered_matches

################## HTML CHECKED BASED ON PDA ##################
class HTMLChecker:
    # inisialisasi stack kosong
    def __init__(self):
        self.stack = []

    # push tag
    def push(self, tag):
        self.stack.append(tag)

    # pop tag
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return not bool(self.stack)

def check_html(html_tags):
    html_checker = HTMLChecker()

    for opening_tag, _, closing_tag in html_tags:
        # kalau ketemu opening tag, di push
        if opening_tag:
            html_checker.push(opening_tag)
        # kalau ketemu closing tag, di pop
        elif closing_tag:
            popped_tag = html_checker.pop()
            if not popped_tag or popped_tag != closing_tag:
                return False

    # true apabila stack kosong
    return html_checker.is_empty()

def main():
    file_path = 'text.html'
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    html_tags = tokenize_html_with_regex(html_content)
    print(html_content)
    is_valid_html = check_html(html_tags)
    print(html_tags)

    if is_valid_html:
        print("Accepted.")
    else:
        print("Syntax Error.")

if __name__ == "__main__":
    main()
