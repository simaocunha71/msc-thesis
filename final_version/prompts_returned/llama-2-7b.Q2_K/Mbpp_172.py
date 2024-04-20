"""
Write a function to count the number of occurence of the string 'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""
import re
def count_occurence(s):
    return [re.search('std', r).groups()[0] for i, r in enumerate(s)]