def count_kmers(sequences, kmers=("A",)):
    """Takes first arg as sequence of CATG nucleotides.
    Second arg is a short n length sequence of nucleotides within
    the first arg. Returns the dict of those kmers."""
    
    result = {}
    for key,value in sequences.items():
        counts= {}
        for kmer in kmers:
            if set(kmer.upper()).issubset(set('ACTG')): #finds the kmer within the set of actg
                counts[kmer.upper()] = value.replace("/n","").upper().count(kmer.upper()) #returns int because of .count at the end
        result[key] = counts
        print(result)
    return result
