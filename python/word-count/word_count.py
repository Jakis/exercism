import re


def clean(phrase):
    # strip elements we don't want
    phrase = re.sub(r"[^\da-z\s\'\_\,]+", "", phrase.lower())
    # replace elements that we do want which should be treated like spaces:
    phrase = re.sub(r",|\t|\n|\_|\,", " ", phrase)
    phrase = phrase.split(" ")
    phrase = [x for x in phrase if x]
    phrase = [x.replace("'", "") if x.startswith("'") else x for x in phrase]
    return phrase


def word_count(phrase):
    ret = {}
    phrase = clean(phrase)
    for word in phrase:
        if ret.get(word, {}):
            ret.update({word: (ret.get(word) + 1)})
        else:
            ret.update({word: 1})
    return ret
