def file_name_check(file_name):
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789."
    if len(file_name) == 0 or file_name[0] not in valid_chars or file_name.count('.') != 1:
        return "No"
    name, extension = file_name.split('.')
    if len(name) == 0 or len(extension) == 0 or len(name) > 3 or extension not in ["txt", "exe", "dll"]:
        return "No"
    for c in name:
        if c not in valid_chars or c.isdigit() and name.count(c) > 1:
            return "No"
    return "Yes"
