
def file_name_check(file_name):
    if len(file_name.split('.')) != 2:
        return 'No'
    
    if len(file_name.split('.')[0]) > 3:
        return 'No'
    
    if file_name.split('.')[0].isdigit():
        return 'No'
    
    if not file_name.split('.')[0][0].isalpha():
        return 'No'
    
    if file_name.split('.')[1] != 'txt' and file_name.split('.')[1] != 'exe' and file_name.split('.')[1] != 'dll':
        return 'No'
    
    return 'Yes'
