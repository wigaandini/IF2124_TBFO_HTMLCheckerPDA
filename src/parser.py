# for checking

from html.parser import HTMLParser
from pathlib import Path

def getPath(namaFile):
    path = Path().absolute()
    pathFile = str(path) + "\\src\\" + namaFile
    return pathFile

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start tag: {tag}, Attributes: {attrs}")

    def handle_endtag(self, tag):
        print(f"End tag: {tag}")

    def handle_data(self, data):
        print(f"Data: {data}")

def parse_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    parser = MyHTMLParser()
    parser.feed(html_content)

html_file_path = getPath(name)
# Example usage:
# html_file_path = 'your_html_file.html'  # Replace with your HTML file path
parse_html_file(html_file_path)
