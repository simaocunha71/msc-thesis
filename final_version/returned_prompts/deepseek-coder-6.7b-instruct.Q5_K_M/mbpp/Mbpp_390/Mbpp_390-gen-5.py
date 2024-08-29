def add_string(lst, string_format):
    return [string_format.format(i) for i in lst]

print(add_string([1,2,3,4],'temp{0}'))

