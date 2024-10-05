    def file_name_check(file_name):
        valid_extensions = ['txt', 'exe', 'dll']
        if file_name[0].isdigit():
            return "No"
        if file_name[-1].isdigit():
            return "No"
        if '.' not in file_name:
            return "No"
        if len(file_name.split('.')[0]) == 0:
            return "No"
        if file_name.split('.')[0][-1].isdigit():
            return "No"
        if file_name.split('.')[1][0].isdigit():
            return "No"
        if file_name.split('.')[1][-1].isdigit():
            return "No"
        if file_name.split('.')[1] not in valid_extensions:
            return "No"
        return "Yes"


