def get_random_new_key():
    candidates = []
    for n in key_list:
        if (n[0] == new_text[-1]):
            candidates.append(n)
    new_text.append(candidates[random.randrange(0, len(candidates))][1])

import sys
import random
book = open('sherlock.txt', 'r')
text_dict = {}
text_list = ''.join(book.read().split('"')).split()
book.close()


for i in range(300):
    if ((new_text[-2], new_text[-1]) in text_dict):
        new_text.append(random.choice(text_dict[new_text[-2], new_text[-1]]))
    else:
        get_random_new_key()

if (new_text[-1][-1] != "."):
    new_text[-1] = new_text[-1] + "."

print(''.join(new_text))
