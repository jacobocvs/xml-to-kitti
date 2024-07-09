import os

def replace_in_file(file_path, search_word_1, search_word_2, search_word_3, replace_word_1, replace_word_2, replace_word_3):

    with open(file_path, 'r') as file:
        file_content = file.read()


    modified_content = file_content.replace(search_word_1, replace_word_1)
    modified_content = modified_content.replace(search_word_2, replace_word_2)
    modified_content = modified_content.replace(search_word_3, replace_word_3)


    with open(file_path, 'w') as file:
        file.write(modified_content)

def batch_replace_in_files(directory, search_word_1, search_word_2, search_word_3, replace_word_1, replace_word_2, replace_word_3):

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            replace_in_file(file_path, search_word_1, search_word_2, search_word_3, replace_word_1, replace_word_2, replace_word_3)

directory = './labelsKitti/'

search_word_1 = 'persons'
replace_word_1 = 'person'
search_word_2 = 'Car'
replace_word_2 = 'car'
search_word_3 = 'two-wheeler'
replace_word_3 = 'bicycle'

batch_replace_in_files(directory, search_word_1, search_word_2, search_word_3, replace_word_1, replace_word_2, replace_word_3)
