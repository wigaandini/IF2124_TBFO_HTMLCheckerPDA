# Open the HTML file in read mode
with open('text.html', 'r') as file:
    # Read the content of the file
    html_content = file.read()

# Now 'html_content' contains the content of the HTML file
print(html_content)

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)