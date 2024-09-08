def add_string(lst, fmt_str):
    return [fmt_str.format(i) for i in lst]

#Testing
print(add_string([1,2,3,4],'temp{0}'))

#Output: ['temp1', 'temp2', 'temp3', 'temp4']

