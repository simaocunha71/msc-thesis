"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""
import collections

def extract_rear(tuple):
    out = tuple[:]
    for s in (str(e) for e in sorted(tuple)):
        if "." not in s:
            break
        out.append("." + s[::-1])

    return out
\end{code}

Output :
    ['.', '.s', 'r', '.']