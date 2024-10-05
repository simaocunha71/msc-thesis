    def is_valid_extension(extension):
        return extension in ['txt', 'exe', 'dll']

    def is_valid_name(name):
        return name.isalpha() and name.islower()

    def is_valid_number_of_digits(name):
        return sum(c.isdigit() for c in name) <= 3

    def is_valid_file_name(file_name):
        return is_valid_number_of_digits(file_name) and \
               is_valid_name(file_name[0]) and \
               file_name.count('.') == 1 and \
               is_valid_extension(file_name.split('.')[-1])

    return 'Yes' if is_valid_file_name(file_name) else 'No'