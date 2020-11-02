import markovify
import random
import numpy

def parser(file): # Даем парсеру файл и он возвращиет список без новых строк и пробелов. Знаки препинания сохранены.
    main_line = []
    with open(file, 'r', encoding='utf8') as text:
        for line in text:
            line_list = line.replace('\n', ' ').split(' ')
            '''for el in line_list:
                if el != '':
                    main_line.append(el)'''
            main_line.append(line_list)
            random.shuffle(main_line)
    result = []
    for line in main_line:
        temp = result.extend(line)
    return result

def generate_sent():
    parsed_text = parser('text.txt')
    line = ' '.join(parsed_text)

    text_model = markovify.Text(line)
    return text_model.make_short_sentence(380)

print(generate_sent())