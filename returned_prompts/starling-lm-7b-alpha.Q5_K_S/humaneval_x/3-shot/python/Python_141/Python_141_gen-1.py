    def file_name_check(file_name):
        if len(file_name.split('.')[:-1]) > 3:
            return 'No'
        if len(file_name.split('.')) != 2:
            return 'No'
        if file_name.split('.')[0] == '':
            return 'No'
        if file_name.split('.')[1].lower() not in ['txt', 'exe', 'dll']:
            return 'No'
        return 'Yes'


