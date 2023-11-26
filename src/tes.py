html_array = ['html', 'head', 'title', '/title', '/head', 'body', 'h2', '/h2', 'form', 'action=', '"', '"', 'method=', '"', '"', 'div', 'id=', '"', '"', '/div', 'br', 'input', 'type=', '"', '"', 'id=', '"', '"', 'br', 'div', 'id=', '"', '"', '/div', 'br', 'input', 'type=', '"', '"', 'id=', '"', '"', 'br', 'br', 'input', 'type=', '"', '"', 'id=', '"', '"', 'br', 'br', 'button', 'type=', '"', '"', '/button', '/form', 'p', '/p', '/body', '/html']

method_values = ['POST']  
input_types = ['text', 'password', 'text']
button_types = ['submit']

def add_method_values(html_arr, method_values):
    i = 0
    j = 0
    while i < len(html_arr):
        if html_arr[i] == 'method=' and html_arr[i + 1] == '"':
            html_arr.insert(i + 2, method_values[j])
            i += 3
            j += 1
        else:
            i += 1

def add_input_types(html_arr, input_types):
    i = 0
    j = 0
    while i < len(html_arr):
        if html_arr[i] == 'input' and html_arr[i + 1] == 'type=' and html_arr[i + 2] == '"':
            html_arr.insert(i + 3, input_types[j])
            i += 4
            j += 1
        i += 1

def add_button_types(html_arr, button_types):
    i = 0
    j = 0
    while i < len(html_arr):
        if html_arr[i] == 'button' and html_arr[i + 1] == 'type=' and html_arr[i + 2] == '"':
            html_arr.insert(i + 3, button_types[j])
            i += 4
            j += 1
        i += 1

add_method_values(html_array, method_values)
print(html_array)
print("")
add_input_types(html_array, input_types)
print(html_array)
print("")
add_button_types(html_array, button_types)
print(html_array)
