def start_withp(words):
    for word in words:
        if word.split()[0][0] in ('P', 'p'):
            return tuple(word.split())

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))

This solution works by iterating over the list of words. For each word, it checks if the first character of the word is 'P' or 'p' (by accessing the first character of the word using word.split()[0][0]). If it is, it returns the two words that start with 'P' or 'p' (by splitting the word into two parts using word.