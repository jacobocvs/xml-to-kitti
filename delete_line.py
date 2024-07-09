import os

def delete_last_blank_char(filename):
    with open(filename, 'r') as file:
        content = file.read()

    if content and content[-1] == ' ':
        content = content[:-1]

    with open(filename, 'w') as file:
        file.write(content)

def delete_last_blank_char_in_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            delete_last_blank_char(file_path)

directory = './labelsKitti/'

delete_last_blank_char_in_files(directory)