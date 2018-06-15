spam = ['apples', 'bananas', 'tofu', 'cats']

def listThing(words):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])
