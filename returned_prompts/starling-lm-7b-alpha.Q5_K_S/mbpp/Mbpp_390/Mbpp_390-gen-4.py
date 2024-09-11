"""
def add_string(lst,s):
    for i in range(len(lst)):
        lst[i]=s.format(lst[i])
    return lst
"""

def add_string(lst,s):
    return [s.format(i) for i in lst]

#test
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
print(add_string([1,2,3,4],'temp{0}'))


def add_string_v2(lst,s):
    return [s.format(i) for i in lst]

assert add_string_v2([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
print(add_string_v2([1,2,3,4],'temp{0}'))



def add_string_v3(lst,s):
    return [s.format(i) for i in lst]

assert add_string_v3([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
print(add_string_v3([1,2,3,4],'temp{0}'))


#test
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
print(add_string([1,2,3,4],'temp{0}'))


def add_string_v2(lst,s):
    return [s.format(i) for i in lst]

assert add_string_v2([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
print(add_string_v2([1,2,3,4],'temp{0}'))



def add_string_v3(lst,s):
    return [s.format(i) for