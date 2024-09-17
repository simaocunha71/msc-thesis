def remove_uppercase(string):
    result = ''.join([char for char in string if char.islower()])
    return result

