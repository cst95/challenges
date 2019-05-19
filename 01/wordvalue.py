from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY) as dictionary:
        content = dictionary.readlines()
        stripped_content = [line.rstrip() for line in content]
        return stripped_content

def calc_word_value(word):
    score = 0
    for letter in (l.upper() for l in word):
        score += LETTER_SCORES.get(letter, 0)
    return score

def max_word_value(list_of_words=[]):
    if not list_of_words:
        list_of_words = load_words()

    best_word, best_score = list_of_words[0], calc_word_value(list_of_words[0])
    
    for word, score in {word: calc_word_value(word) for word in list_of_words}.items():
        if score > best_score:
            best_word, best_score = word, score

    return best_word

if __name__ == "__main__":
    pass # run unittests to validate
