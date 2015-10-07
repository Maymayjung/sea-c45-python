def get_random_new_key():
    candidates = []
    for n in key_list:
        if (n[0] == new_text[-1]):
            candidates.append(n)
    new_text.append(candidates[random.randrange(0, len(candidates))][1])

import random
book = open('sherlock.txt', 'r')
text_dict = {}
text_list = ''.join(book.read().split('"')).split()
book.close()

for i in range(2, len(text_list)):
    if ((text_list[i - 2], text_list[i - 1]) in text_dict):
        text_dict[(text_list[i - 2], text_list[i - 1])].append(text_list[i])
    else:
        text_dict[text_list[i - 2], text_list[i - 1]] = [text_list[i]]

key_list = list(text_dict.keys())
new_text = list(random.choice(key_list))
new_text[0] = new_text[0].capitalize()

for i in range(300):
    if ((new_text[-2], new_text[-1]) in text_dict):
        new_text.append(random.choice(text_dict[new_text[-2], new_text[-1]]))
    else:
        get_random_new_key()

if (new_text[-1][-1] != "."):
    new_text[-1] = new_text[-1] + "."

print(' '.join(new_text))
