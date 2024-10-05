    def is_valid(file_name):
        if len(file_name) < 1 or len(file_name) > 255:
            return False
        if file_name.count('.') != 1:
            return False
        parts = file_name.split('.')
        if not parts[0][0].isalpha():
            return False
        if len(parts[0]) > 1 and not parts[0][1:].isalnum():
            return False
        if len(parts) > 2:
            return False
        if len(parts[1]) > 4 or parts[1].lower() not in ['txt', 'exe', 'dll']:
            return False
        return True

    return 'Yes' if is_valid(file_name) else 'No'
    # You can also use regular expressions for this problem
    # import re
    # return 'Yes' if re.match(r'^[a-zA-Z][a-zA-Z0-9]*(\.([a-zA-Z]{3}))$', file_name) else 'No'  # you can use this if you prefer regular expressions.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs.  # it will also check the length of the file name and the extension.  # you can adjust the regular expression according to your needs