    words = s.split()
    oranges = int(''.join(filter(str.isdigit, [word for word in words if 'oranges' in word])))
    apples = int(''.join(filter(str.isdigit, [word for word in words if 'apples' in word])))
    total_fruits = sum(int(word) for word in words if word.isdigit())
    return total_fruits - oranges - apples


