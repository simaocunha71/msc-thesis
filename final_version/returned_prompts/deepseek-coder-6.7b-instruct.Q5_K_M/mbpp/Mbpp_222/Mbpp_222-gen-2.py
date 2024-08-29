def check_type(t):
    return len(set(map(type, t))) == 1

print(check_type((5, 6, 7, 3, 5, 6)))  # True

Explanation:
- The map function applies the type function to each element in the tuple, creating a new iterable of the types of the elements.
- The set function removes duplicates from the resulting iterable, leaving a set of unique types.
- The len function then checks if the number of unique types is 1, which would mean all elements in the tuple are of the same type.



