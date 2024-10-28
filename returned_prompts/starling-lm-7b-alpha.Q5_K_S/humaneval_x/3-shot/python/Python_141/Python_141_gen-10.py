    def is_latin_alpha(s):
        return ord(s) >= 65 and ord(s) <= 90 or ord(s) >= 97 and ord(s) <= 122

    def is_three_digits(s):
        return s.isdigit() and len(s) == 3

    def is_sub_string(s):
        return s in ['txt', 'dll', 'exe']

    if file_name[0].isdigit() or not is_latin_alpha(file_name[0]):
        return 'No'

    if '.' not in file_name or file_name.count('.') != 1:
        return 'No'

    if len(file_name) == 1 or file_name[-1].isdigit():
        return 'No'

    if file_name[-2].isdigit() or not is_three_digits(file_name[-2]):
        return 'No'

    if not is_sub_string(file_name[-1]):
        return 'No'

    return 'Yes'


