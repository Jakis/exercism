def reverse(text=''):
    if text is None:
        raise Exception("Text cannot be found, no reversal is possible")
    text_list = list(text)
    text_list.reverse()
    return "".join(text_list)
