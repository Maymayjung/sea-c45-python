import trigrams

storyF = "/home/may/Desktop/Python/sea-c45-python/hw/hw21/sherlock_small.txt"


def test_open_flie():
    trigrams.words_from_file(storyF)


def test_read_lines():
    words = trigrams.words_from_file(storyF)
    assert(len(words))


def test_is_trigrams_dictionary():
    words = trigrams.words_from_file(storyF)
    dictionary = trigrams.trigrams_from_words(words)
    assert(type(dictionary) == dict)


def test_length_of_story():
    words = trigrams.words_from_file(storyF)
    dictionary = trigrams.trigrams_from_words(words)
    story = trigrams.story_from_trigrams(dictionary, 400)
    splitted_story = story.split(" ")
    assert(len(splitted_story) >= 300)
