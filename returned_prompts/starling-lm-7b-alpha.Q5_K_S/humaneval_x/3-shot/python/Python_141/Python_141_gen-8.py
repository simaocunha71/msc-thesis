    def check(file_name):
        count = 0
        for char in file_name:
            if char.isdigit():
                count += 1
                if count > 3:
                    return False
        if file_name.count('.') != 1:
            return False
        if file_name[file_name.find('.'):].strip() != '':
            return False
        return file_name[0].isalpha() and file_name[-3:] in ['txt', 'dll', 'exe']

    return 'Yes' if check(file_name) else 'No'


