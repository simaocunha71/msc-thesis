"""
def check_integer(string):
    try:
        x = int(string)
    except ValueError:
        return False
    else:
        return True
"""

def check_integer(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True

# assert check_integer("python")==False
# assert check_integer("3")==True

def check_integer(string):
    if string.isdigit():
        return True
    else:
        return False

# assert check_integer("python")==False
# assert check_integer("3")==True

def check_integer(string):
    if string.replace(".", "", 1).isdigit():
        return True
    else:
        return False

# assert check_integer("python")==False
# assert check_integer("3")==True

def check_integer(string):
    try:
        value = float(string)
    except ValueError:
        return False
    else:
        return value == int(value)

# assert check_integer("python")==False
# assert check_integer("3")==True

def check_integer(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True

# assert check_integer("python")==False
# assert check_integer("3")==True

def check_integer(string):
    return string.isdigit()

# assert check_integer("python")==False
# assert check_integer("3")==True

def check_integer(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True

# assert check_integer("python")==False
# assert check_integer("3")==True

def check_integer(string):
    if string[0] == "-":
        return False
    if string.replace("-", "", 1).replace(".", "", 1).isdigit():
        return True
    else:
        return False

# assert check_integer("python")==False
# assert check_