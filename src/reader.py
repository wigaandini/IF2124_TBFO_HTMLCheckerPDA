import re

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
        filtered_matches.append((opening_tag, attributes, closing_tag))

    return filtered_matches

def main():
    # Read HTML file
    file_path = 'src/text.html'  # Replace with the path to your HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Tokenize HTML using regular expressions
    html_tags = tokenize_html_with_regex(html_content)

    # Print tags and attributes
    for opening_tag, attributes, closing_tag in html_tags:
        if opening_tag:
            print(f'Tag: {opening_tag}, Attributes: {attributes}')
        else:
            print(f'Tag: /{closing_tag}, Attributes:')

if __name__ == "__main__":
    main()

state = 'START'
stack = 'Z0'
