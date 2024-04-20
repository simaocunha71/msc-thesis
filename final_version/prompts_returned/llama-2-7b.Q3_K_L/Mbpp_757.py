"""
Write a function to count the pairs of reverse strings in the given string list. 
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""

def count_reverse_pairs(s):
    """Count reversed chars pairs"""
    s = sorted(s)
    d = {s[i:]:1 for i, x in enumerate(s)}
    
    return sum([len(d.get(x))//2 for x in s]) 

# count_reverse_pairs("julia")
