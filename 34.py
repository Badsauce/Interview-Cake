import string

def make_word_cloud(input_string):
    striped_input = input_string.strip(string.punctuation)
    raw_words = striped_input.split()

    words = {}

    for word in raw_words:
        if word.lower() in words:
            words[word.lower()] += 1
        elif word in words:
            words[word] += 1
        else:
            words[word] = 1

    return words

result = make_word_cloud('Add milk and eggs, then add flour and sugar. Add')

print(result)
