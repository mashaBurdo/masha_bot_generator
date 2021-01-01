import markovify
import random
import re

def parser(file): # Даем парсеру файл и он возвращиет список без новых строк и пробелов. Знаки препинания сохранены.
    main_line = []
    with open(file, 'r', encoding='utf8') as text:
        for line in text:
            line_list = line.replace('\n', ' ').replace(':', '').replace('(', '').replace(')', '').replace(';', '').split(' ')
            no_list = ['', '.', ',', 'т.', 'е.', 'т.е.', 'ч.', 'г.']
            for el in line_list:
                if el not in no_list and not el.isupper() and not re.match('\d', el):
                    main_line.append(el)
    return main_line

def generate_sent():
    parsed_text = parser('stom.txt') +parser('sex.txt')
    line = ' '.join(parsed_text)

    text_model = markovify.Text(line)
    return text_model.make_short_sentence(380).capitalize()

#print(generate_sent())
#print(parser('sex.txt'))