def is_pangram(sentence):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    sentence = list(sentence.lower())
    [alphabet.remove(l) for l in sentence if l in alphabet]
    if not alphabet:
        return True
    return False
