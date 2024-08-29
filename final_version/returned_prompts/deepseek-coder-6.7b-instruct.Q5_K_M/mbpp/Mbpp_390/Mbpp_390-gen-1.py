
def add_string(lst, string):
    return [string.format(i) for i in lst]

print(add_string([1,2,3,4],'temp{0}'))

"""
