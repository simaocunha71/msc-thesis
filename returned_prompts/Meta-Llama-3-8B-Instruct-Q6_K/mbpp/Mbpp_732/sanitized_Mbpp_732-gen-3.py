def replace_specialchar(s):
    return s.replace(' ', ':').replace(',', ':').replace('.', ':')  # or s.translate(str.maketrans(" ,.", " ::"))