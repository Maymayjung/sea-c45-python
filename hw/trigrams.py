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
