
def file_name_check(file_name):
    if len(file_name) > 3:
        return 'No'
    elif file_name.count(".") != 1:
        return 'No'
    elif file_name.split(".")[0] == '' or not file_name.split(".")[0][0].isalpha():
        return 'No'
    else:
        return 'Yes'


