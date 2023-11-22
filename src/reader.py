# # # Open the HTML file in read mode
# # with open('text.html', 'r') as file:
# #     # Read the content of the file
# #     html_content = file.read()

# # # Now 'html_content' contains the content of the HTML file
# # print(html_content)

# # import re

# # txt = "The rain in Spain"
# # x = re.search("^The.*Spain$", txt)

# import urllib2
# from bs4 import BeautifulSoup

# # Fetch the html file
# response = urllib2.urlopen('http://tutorialspoint.com/python/python_overview.htm')
# html_doc = response.read()

# # Parse the html file
# soup = BeautifulSoup(html_doc, 'html.parser')

# # Format the parsed html file
# strhtm = soup.prettify()

# # Print the first few characters
# print (strhtm[:225])

import re
from pathlib import Path

def getPath(namaFile):
    path = Path().absolute()
    pathFile = str(path) + "\\src\\" + namaFile
    return pathFile

def tokenize_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Updated pattern to handle spaces in tags, attribute names, and attribute values
    pattern = r'<\s*[^>]*>|<[^>]+\s+[^=\s]+(?:\s*=\s*"[^"]*")?[^>]*>|[^<]+'

    regex = re.compile(pattern)
    matches = regex.finditer(html_content)

    tokens = []

    for match in matches:
        tokens.append(match.group())

    return tokens

# Example usage:
name = input("Nama file : ")
html_file_path = getPath(name)
tokens = tokenize_html_file(html_file_path)

for token in tokens:
    print(token)
