
def file_name_check(file_name):
    alphabet_start = file_name[0]
    dot_index = file_name.index('.')
    ext = file_name[dot_index + 1:]
    if len(file_name.split('.')) != 2:
        return 'No'
    if alphabet_start.isalpha():
        if ext in ['txt', 'exe', 'dll']:
            if file_name[:dot_index].count('0') + file_name[:dot_index].count('1') + file_name[:dot_index].count('2') + file_name[:dot_index].count('3') + file_name[:dot_index].count('4') + file_name[:dot_index].count('5') + file_name[:dot_index].count('6') + file_name[:dot_index].count('7') + file_name[:dot_index].count('8') + file_name[:dot_index].count('9') <= 3:
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'
    else:
        return 'No'

# Tests
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.TXT")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("123example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("123.txt")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("123.exE")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("123.dll")) # => 'No' (the name should start with a latin alphapet