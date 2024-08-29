def start_withp(lst):
    for item in lst:
        words = item.split()
        for word in words:
            if word.lower().startswith('p'):
                return word,

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))


