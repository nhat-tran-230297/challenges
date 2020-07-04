from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        return [w.replace('\n', '') for w in f.readlines()]

dictionary = load_words()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total = 0
    for char in word.upper():
        total += LETTER_SCORES.get(char, 0)

    return total


def max_word_value(word_list=dictionary):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_value_dict = {word: calc_word_value(word) for word in word_list}
    max_value = max(list(word_value_dict.values()))
    sorted_word = [word for word, value in word_value_dict.items() if value == max_value]

    if len(sorted_word) > 1:
        return sorted_word
    else:
        return sorted_word[0]


if __name__ == "__main__":
    # run unittests to validate
    max_word = max_word_value()
    print(max_word)
