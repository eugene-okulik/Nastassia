# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову)
# в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl,
# facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран. Знаки препинания не
# должны оказаться внутри слова. Если после слова идет запятая или точка,
# этот знак препинания должен идти после того же слова,
# но уже преобразованного.

text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()

for word in range(len(words)):
    if words[word][-1] in [',', '.']:
        punct = words[word][-1]
        words[word] = words[word][:-1]
    else:
        punct = ''
    words[word] += 'ing' + punct

text_mod = ' '.join(words)

print(text_mod)
