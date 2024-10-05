
def prime_length(string):
    if len(string) <= 0:
        return False
    if len(string) == 1:
        return True
    if len(string) == 2:
        return True
    for i in range(2, len(string)):
        if len(string) % i == 0:
            return False
    return True
