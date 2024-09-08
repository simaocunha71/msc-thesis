def replace_specialchar(string):
    # We replace all spaces, commas, and dots with colons.
    return string.replace(' ', ':').replace(',', ':').replace('.', ':')