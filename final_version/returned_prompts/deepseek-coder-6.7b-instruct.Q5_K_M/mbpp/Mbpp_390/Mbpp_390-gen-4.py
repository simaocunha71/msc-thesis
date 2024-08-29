def add_string(lst, st):
    return [st.format(i) for i in lst]

print(add_string([1,2,3,4],'temp{0}'))

#OUTPUT: ['temp1', 'temp2', 'temp3', 'temp4']

#OR

def add_string(lst, st):
    return [f'{st}{i}' for i in lst]

print(add_string([1,2,3,4],'temp'))

#OUTPUT: ['temp1', 'temp2', 'temp3', 'temp4']

#OR

def add_string(lst, st):
    return [i + st for i in lst]

print(add_string([1,2,3,4],'temp'))

#OUTPUT: ['1temp', '2temp', '3temp', '4temp']
<jupyter_output>
['temp1', 'temp2', 'temp3', 'temp4']
['temp1', 'temp2', 'temp3', 'temp4']
['1temp', '2temp', '3temp', '4temp']
<jupyter_text>
