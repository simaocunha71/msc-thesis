def start_withp(words):
    pair = ()
    for word in words:
        w = word.split(' ')
        for i in w:
            if i[0].lower() == 'p':
                pair += (i,)
    return pair[:2]

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))

The function 'start_withp' works by splitting each string in the list into words. Then it checks each word to see if it starts with 'p'. If it does, it adds it to a tuple. The function returns the first two words it finds that start with '