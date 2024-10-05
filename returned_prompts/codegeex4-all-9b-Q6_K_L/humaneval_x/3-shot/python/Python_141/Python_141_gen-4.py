    def is_valid_file_name(file_name):
        # Check if the file name has more than three digits
        if sum(c.isdigit() for c in file_name) > 3:
            return False

        # Check if the file name contains exactly one dot '.'
        if file_name.count('.') != 1:
            return False

        # Check if the substring before the dot starts with a letter from the latin alphabet
        if not file_name.split('.')[0].isalpha():
            return False

        # Check if the substring after the dot is one of ['txt', 'exe', 'dll']
        if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
            return False

        return True

    # Test the function with some examples
    print(is_valid_file_name("example.txt"))  # => 'Yes'
    print(is_valid_file_name("1example.dll"))  # => 'No' (the name should start with a latin alphapet letter)