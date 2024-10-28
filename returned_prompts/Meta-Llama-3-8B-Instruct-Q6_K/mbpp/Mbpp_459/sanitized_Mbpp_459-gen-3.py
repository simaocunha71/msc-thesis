def remove_uppercase(s):
    return ''.join([c for c in s if c.islower()])
    # or 
    # return ''.join([c for c in s if not c.isupper()])  # This will also work