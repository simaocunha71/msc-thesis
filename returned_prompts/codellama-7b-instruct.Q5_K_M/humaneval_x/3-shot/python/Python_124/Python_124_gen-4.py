    import re
    regex = r"^((0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(19|20)\d\d)$"
    return re.match(regex, date) != None

