def file_name_check(file_name):
    if len(re.findall(r'\d', file_name)) > 3:
        return "No"
    if file_name.count('.') != 1:
        return "No"
    if not file_name[0].isalpha():
        return "No"
    if file_name.split('.')[-1] not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"

