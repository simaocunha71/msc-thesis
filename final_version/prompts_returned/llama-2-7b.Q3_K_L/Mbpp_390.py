"""
Write a function to apply a given format string to all of the elements in a list.
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
"""

def add_string(list,format):
    result=[] 
    for i in range(len(list)):  
        if type(str(list[i])) == str:  
            result.append(str(format).format(str(list[i])))
        else:
            result.append('%s' %str(list[i]))
    return list