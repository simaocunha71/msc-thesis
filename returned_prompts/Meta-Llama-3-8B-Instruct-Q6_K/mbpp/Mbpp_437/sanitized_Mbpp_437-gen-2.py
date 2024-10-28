def remove_odd(s):
    return ''.join([c for c in s if int(c) % 2 == 0])  # or use string methods: s.translate(str.maketrans("13579", "      "))
    # or use list comprehension with string join: ''.join([c for c in s if int(c) % 2 == 0])
    # or use string comprehension: ''.join([c for c in s if int(c) % 2 == 0])  # python 3.6 and later
    # or use dictionary comprehension: ''.join([c for c in s if int(c) % 2 == 0])  # python 3.6 and later
    # or use lambda function: ''.join(map(lambda c: c if int(c) % 2 == 0 else '', s))
    # or use map function: ''.join(map(lambda c: c if int(c) % 2 == 0 else '', s))
    # or use filter function: ''.join(list(filter(lambda c: int(c) % 2 == 0, s)))
    # or use regular expressions: re.sub('[13579]', '', s)  # python 3.7 and later
    # or use regular expressions: ''.join(re.findall(r'\d', s))  # python 3.7 and later
    # or use regular expressions: re.sub('[13579]', '', s)  # python 3.7 and later
    # or use regular expressions: ''.join(re.findall(r'\d', s))  # python 3.7 and later
    # or use regular expressions: re.sub('[13579]', '', s)  # python 3.7 and later
    # or use regular expressions: ''.join(re.findall(r'\d', s))  # python 3.7 and later
    # or use regular expressions: re.sub('[13579]', '', s)  # python 3.7 and later
    # or use regular expressions: ''.join(re.findall(r'\d', s))  # python 3.7 and later
    # or use regular expressions: re.sub('[13579]', '', s)  # python 3.7 and later
    # or use regular expressions: ''.join(re.findall(r'\d', s))  # python 3.7 and later
    # or use regular expressions: re.sub('[13579]', '', s) 