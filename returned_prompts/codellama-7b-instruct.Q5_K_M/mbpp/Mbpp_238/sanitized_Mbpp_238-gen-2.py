def number_of_substrings(s):
    return len(list(itertools.chain(*[itertools.combinations(s,i) for i in range(1,len(s)+1)])))