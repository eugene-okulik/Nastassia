# Создать словарь (и сохранить его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’.

my_dict = {
    'tuple': (2, 4, 'love', True, 7),
    'list': [1, 5, 5, 3, None],
    'dict': {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5'},
    'set': {2, 5, 7, 1, 8}
}

# ‘tuple’: вывести на экран последний элемент:

print(my_dict['tuple'][-1])

# ‘list’: добавить в конец списка еще один элемент

my_dict['list'].append('sunny')

# ‘list’: удалить второй элемент списка

my_dict['list'].pop(1)

# ‘dict’: добавить элемент с ключом ('i am a tuple',) и любым значением, удалить какой-нибудь элемент

my_dict['dict'].update({'i am a tuple': (None, 1, 'text')})
my_dict['dict'].pop('two')

# ‘set’: добавить новый элемент в множество, удалить элемент из множества

my_dict['set'].add(6)
my_dict['set'].remove(2)

# вывести на экран весь словарь
print(my_dict)
