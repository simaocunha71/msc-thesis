    import re

    match = re.match('^[a-zA-Z][^.]*\.(txt|exe|dll)$', file_name)
    if match:
        return 'Yes'
    else:
        return 'No'


