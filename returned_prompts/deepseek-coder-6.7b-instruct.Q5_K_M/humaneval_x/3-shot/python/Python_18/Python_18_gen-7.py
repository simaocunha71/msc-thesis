    count = start 0
    while True:
        start = string.find(substring, start) 
        if start == -1: return count
        start 
A: start + len(substring)
        count += 1


