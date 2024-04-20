"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""
from typing import Dict
def get_freq(l:list)->Dict :
    d={}
    for k in l:
        d[k]=(d.get(k,0)+1) if d.get(k,0)>0 else (d.get(k,0),1)
    return d