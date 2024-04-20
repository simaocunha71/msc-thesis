"""
Write a function to find the combinations of sums with tuples in the given tuple list. 
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""

def find_combinations(tuples):
    """Find the combinations with tuples as inputs."""
    
    def helper(pairs, cur_tuple, i):
        if p.sum() == cur_tuple:
            yield (cur_tuple,) + pairs[:i] + [p] + pairs[i+1:]
        elif pairs[i].sum() < cur_tuple:
            helper(list(reversed(pairs)), cur_tuple, i+1)
            
    tuples = sorted(tuples) # sort the input so that the combination is not out of order. 
    
    for pair in tuples[::2]:
        helper([(pair,)], pair, 0)
        
    return [x for x in find_combinations([tuple-(cur,(cur+1)), for cur in pairs[:-1]]) if sum(x)+sum(pairs[-1]) == tuples[len(tuples)/2]]

#print find_combinations([(2,4),(6,7),(5,1)], (5, 9))