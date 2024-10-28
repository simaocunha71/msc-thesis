def file_name_check(file_name):
    import re
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9]{0,2}\.(?:txt|exe|dll)$')
    return 'Yes' if pattern.match(file_name) else 'No'