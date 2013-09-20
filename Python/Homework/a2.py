def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    nuc_cnt = 0
    for i in dna:
        if nucleotide == i:
            nuc_cnt +=1
    return nuc_cnt

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.find(dna2) >= 1

def is_valid_sequence(dna):
    """ (str) -> bool

    The parameter is a potential DNA sequence. Return True if and only if the
    DNA sequence is valid (that is, it contains no characters other than
    'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ATCG')
    True
    
    >>> is_valid_sequence('atcg')
    False
    
    """
    invalid = 0
    for i in dna:
        if i in 'ATCG':
            invalid += 0
        else:
            invalid += 1
    return invalid == 0

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    The first two parameters are DNA sequences and the third parameter is an
    index. Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index. (You can assume that the
    index is valid.)

    >>> insert_sequence('ATCG', 'TA', 2)
    'ATTACG'

    >>> insert_sequence('TTCCGAGT', 'CGTA', 5)
    'TTCCGCGTAAGT'

    """
    return dna1[0:index] + dna2 + dna1[index:]


def get_complement(nucleotide):
    
    """(str) -> str

    The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the
    nucleotide's complement.

    >>> get_complement('A')
    'T'

    >>>get_complement('C')
    'G'

    """
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'G':
        return 'C'
    if nucleotice == 'C':
        return 'G'

  
def get_complementary_sequence(DNA):
    """(str) -> str

    The parameter is a DNA sequence. Return the DNA sequence that is
    complementary to the given DNA sequence.
    
    >>> get_complementary_sequence('ATGC')
    'GCTA'

    >>> get_complementary_sequence('GATCATG')
    'GTACTAG'
    """
    return DNA[::-1]
