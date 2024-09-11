"""
def add_string(list_str,format_str):
    new_list = []
    for i in range(len(list_str)):
        new_list.append(format(format_str.format(list_str[i]),'s'))
    return new_list

assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
"""

def add_string(list_str,format_str):
    return [format(format_str.format(i),'s') for i in list_str]

assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']


# 使用生成器表达式来简化
def add_string(list_str,format_str):
    return [format(format_str.format(i),'s') for i in list_str]

assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']

# 使用map函数来简化
def add_string(list_str,format_str):
    return list(map(lambda x:format(format_str.format(x),'s'),list_str))

assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']

# 使用reduce函数来简化
from functools import reduce
def add_string(list_str,format_str):
    return reduce(lambda x,y:x+[format(format_str.format(y),'s')],list_str,[])

assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']

# 使用列表推导式来简化
def add_string(list_str,format_str):
    return [format(format_str.format(i),'