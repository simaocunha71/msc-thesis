def extract_string(lst,n):
    return [i for i in lst if type(i) == str and len(i) > n]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'],8))

