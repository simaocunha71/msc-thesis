def count_substring(s, sub):
    count = start = 0
    while start < len(s):
        pos = s.find(sub, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

print(count_substring("Hello World