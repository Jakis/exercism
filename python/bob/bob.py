import re


def question(yell=False):
    '''
    Bob answers 'Sure.' if you ask him a question.
    bob.hey("Does this cryogenic chamber make me look fat?"), "Sure.")
    self.assertEqual(bob.hey("You are, what, like 15?"), "Sure.")
    self.assertEqual(bob.hey("fffbbcbeab?"), "Sure.")
    self.assertEqual(bob.hey("4?"), "Sure.")
    self.assertEqual(bob.hey(":) ?"), "Sure.")
    bob.hey("Wait! Hang on. Are you going to be OK?"), "Sure.")
    bob.hey("Okay if like my  spacebar  quite a bit?   "), "Sure.")
    '''
    if yell:
        '''
        He answers  if you yell a question at him.
        '''
        return "Calm down, I know what I'm doing!"
    return "Sure."


def yell():
    '''
    He answers 'Whoa, chill out!' if you yell at him.
    '''
    return 'Whoa, chill out!'


def address():
    '''
    He says 'Fine. Be that way!' if you address him without actually saying
    anything.
    '''
    return 'Fine. Be that way!'


def check_phrase(phrase):
    phrase_array = list(phrase)
    alpha_only = [e for e in phrase_array if e.isalpha()]
    non_alpha = [e for e in phrase_array if e not in alpha_only]
    upper_array = [e.upper() for e in phrase_array]
    # print(list(phrase))
    # print(alpha_phrase)
    # # alpha_phrase = "".join(alpha_phrase)

    is_question = re.match(".*\?", phrase)
    is_exclaim = re.match(".*\!", phrase)
    no_punctuation = phrase_array[-1] not in ["!", "?", "."]
    is_shout = (upper_array == phrase_array) and alpha_only
    print("original: {0} \n".format(phrase_array))
    print("alpha: {0} \n".format(alpha_only))
    print("non alpha: {0} \n".format(non_alpha))
    print("no_punctuation: {0} \n".format(no_punctuation))
    if is_question:
        if is_shout:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    return None


def clean(phrase):
    trailing_spaces = re.match(r'^(.*)([\?|\!]\s+)$', phrase)
    if trailing_spaces:
        phrase = trailing_spaces.groups()[0] + "?"
    return phrase


def hey(phrase):
    print("checking : ---{0}---".format(phrase))
    phrase = clean(phrase)
    response = check_phrase(phrase)
    print("resp : ---{0}--- \n".format(response))
    return response
    # has_no_words = re.match(r'[^\W|\D|\S]$', phrase)
    # print("has no words: {0}".format(has_no_words))
    # if re.match(r'.*(\?|\?\s+)$', phrase):
    #     print("question")
    # if re.match(r'.*(\!|\!\s+)$', phrase):
    #     print("yelling")
    # if re.match(r'.*(\.|\.\s+)$', phrase):
    #     print("statement")

    # # questions
    # if re.match(r'[\w|\s|\!|\,|\:|\|\.)]+\?', phrase):
    #     # yelling questions
    #     if re.match(r'[A-Z|\s]+\?($|/s+$)', phrase):
    #         return "Calm down, I know what I'm doing!"
    #     return "Sure."
    # if re.match(r'.*\!$', phrase):
    #     return 'Whoa, chill out!'
    # return 'Whatever.'
    return ""


print("Looking for Sure:  ===============================")
print(hey("Does this cryogenic chamber make me look fat?"))
print(hey("You are, what, like 15?"))
print(hey("fffbbcbeab?"))
print(hey("Okay if like my  spacebar  quite a bit?   "))
print(hey("4?"))
print(hey(":) ?"))
print(hey("Wait! Hang on. Are you going to be OK?"))
print("Looking for Calm down, I know what I'm doing!  ===============================")
print(hey("WHAT THE HELL WERE YOU THINKING?"))
print("Whoa, chill out!  ===============================")
print(hey("WATCH OUT!"))
print(hey("FCECDFCAAB"))
print(hey("1, 2, 3 GO!"))
print(hey("I HATE YOU"))
