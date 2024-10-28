def remove_uppercase(s):
    return ''.join([i for i in s if i.islower()])  # Using list comprehension