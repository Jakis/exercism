def is_isogram(match):
    match = list(match.lower().replace(" ", "").replace("-", ""))
    if sorted(match) != sorted(set(match)):
        return False
    return True
