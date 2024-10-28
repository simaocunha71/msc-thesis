
def closest_integer(value):
    if value[0] == '-':
        return int(value.replace('.', '').replace('-', '')[:-1])
    else:
        return int(value.replace('.', ''))



