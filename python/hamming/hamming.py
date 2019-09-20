def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Cannot compute hamming for strands of inequal length.")
    hamming = 0
    for ind, element in enumerate(strand_a):
        if element != strand_b[ind]:
            hamming += 1
    return hamming
