
def file_name_check(file_name):
    import re
    # regex = r"[a-zA-Z][a-zA-Z0-9]{0,2}\.[txt|exe|dll]$"
    regex = r"[a-zA-Z][a-zA-Z0-9]{0,2}\.(?:txt|exe|dll)$"
    pattern = re.compile(regex)
    return "Yes" if pattern.match(file_name) else "No"