import io
from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    str_num = 0
    for string in strings:
        str_num += 1
        cursor_position = file.tell()
        file.write(f'{string}\n')
        strings_positions[(str_num, cursor_position)] = string
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)