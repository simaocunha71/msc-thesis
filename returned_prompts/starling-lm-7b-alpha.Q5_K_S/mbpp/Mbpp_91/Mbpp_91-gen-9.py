def anagrams(string):
    anagrams=set()
    if len(string)==1:
        return {string}
    for i in string:
        for j in anagrams|set(anagrams.map(lambda x:x+i)):
            anagrams.add(j+i)
    return anagrams

# assert anagrams("cat")==["cat", "act", "tac", "cata", "atc", "cata"]

"""
Given a string, write a function to return the list of all possible permutations of the string.
assert permutations("cat")==["cat", "cta", "ct", "ata", "ac",