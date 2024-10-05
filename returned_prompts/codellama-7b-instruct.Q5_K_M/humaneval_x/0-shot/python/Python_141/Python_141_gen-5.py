
def file_name_check(file_name):
    return 'No' if file_name.count('0') > 3 or file_name.count('.') > 1 or file_name.startswith('.') or file_name.endswith('.') else 'Yes' if file_name.count('.') == 1 and file_name.split('.')[0].isalpha() and file_name.split('.')[1] in ['txt', 'exe', 'dll'] else 'No'
