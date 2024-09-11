def replace_specialchar(s):
    return s.replace(' ', ':').replace(',', ':').replace('.', ':')  # or use regular expressions: re.sub(r'[ ,\.]', ':', s)  # python3.6+