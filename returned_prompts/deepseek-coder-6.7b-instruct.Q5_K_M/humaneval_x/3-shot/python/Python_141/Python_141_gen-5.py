    import re

    match = re.match("^[a-zA-Z][a-zA-Z0-9]{0,2}\.(txt|exe|dll)$", file_name)
    if match:
        return 'Yes'
    else:
        return 'No'

