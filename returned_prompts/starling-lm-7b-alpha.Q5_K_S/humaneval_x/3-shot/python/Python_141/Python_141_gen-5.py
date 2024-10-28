    def is_latin_alpha(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    def is_digit(c):
        return '0' <= c <= '9'

    if not file_name or not is_latin_alpha(file_name[0]):
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if not file_name.count(file_name[0]):
        return 'No'
    if not is_latin_alpha(file_name[file_name.index('.') + 1]):
        return 'No'
    if file_name.split('.')[-1] not in ['txt', 'exe', 'dll']:
        return 'No'
    if file_name.count(file_name[file_name.index('.') + 1]) > 1:
        return 'No'
    if file_name.count(file_name[0]) > 1:
        return 'No'
    return 'Yes'


