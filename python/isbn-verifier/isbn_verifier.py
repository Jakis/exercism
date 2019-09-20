import re


def verify(isbn):
    isbn = re.sub(r"[^\dx]+", "", isbn.lower())
    if re.match(r"^\d{9}[x|\d]$", isbn):
        isbn = [10 if x == 'x' else int(x) for x in list(isbn)]
        isbn = [element * (10 - ind) for ind, element in enumerate(isbn)]
        if sum(isbn) % 11 == 0:
            return True
    return False
