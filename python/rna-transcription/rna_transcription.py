def to_rna(dna_strand):
    rna_strand = ""
    for letter in list(dna_strand):
        if letter == 'C':
            rna_strand += 'G'
        elif letter == 'G':
            rna_strand += 'C'
        elif letter == 'T':
            rna_strand += 'A'
        elif letter == 'A':
            rna_strand += 'U'
        else:
            raise Exception("Found invalid DNA element {}".format(letter))
    return rna_strand
