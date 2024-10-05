    def check_digit_count(file_name):
        count = 0
        for elem in file_name:
            if elem.isdigit():
                count += 1
        return count <= 3

    def check_dot_count(file_name):
        dot_count = 0
        for elem in file_name:
            if elem == '.':
                dot_count += 1
        return dot_count == 1

    def check_start(file_name):
        if file_name[0].isalpha():
            return True
        return False

    def check_end(file_name):
        if file_name[-3:] in ['txt', 'exe', 'dll']:
            return True
        return False

    if check_digit_count(file_name) and check_dot_count(file_name) and check_start(file_name) and check_end(file_name):
        return "Yes"
    return "No"


