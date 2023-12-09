
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """

def levenshtein(s1, s2):
    """Write a function levenshtein which takes two string as input and returns the Levenshtein Distance between them.
    
    The Levenshtein Distance is defined as:
    d (s1, s2) = min { | n | Σ i=1..n, Δi, j ≥ 0 }
                 where Δij = the minimum cost of changing a character in s1 to get it equal with character at position j in s2.
    
    Example:
    >>> levenshtein("abcde","ACEDY")
    3
    """

def count_vowels(s):
    """Write a function count_vowels which takes a string as input and returns the number of vowels in the given string,
   using the vowels_count() function.
    Example:
    >>> s = 'ACEDY'
    >>> count_vowels(s)
    3
    """
def levenshtein_example():
    "Write a function levenshtein_example which takes one string as input, computes the Levenshtein Distance between that and another given string (also as input),  prints both the strings along with that distance.
    
    Example:
    >>> levenshtein_example("ACEDY", "AAC")
    'ACEDY' 'AAC' 0
    """
if __name__ == '__main__':
    s = input()
    if vowels_