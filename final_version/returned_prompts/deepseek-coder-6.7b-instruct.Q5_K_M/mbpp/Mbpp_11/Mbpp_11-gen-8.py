def remove_Occ(string, char):
    first_index = string.find(char)
    if first_index != -1:
        string = string[:first_index] + string[first_index+1:]
        last_index = string.rfind(char)
        if last_index != -1:
            string = string[:last_index] + string[last_index+1:]
    return string

print(remove_Occ("hello", "l"))

# OR

def remove_Occ(string, char):
    while char in string:
        first_index = string.find(char)
        string = string[:first_index] + string[first_index+1:]
        last_index = string.rfind(char)
        string = string[:last_index] + string[last_index+1:]
    return string

print(remove_Occ("hello", "l"))

"""
Both solutions will output:
'heo'
"""

# OR 

def remove_Occ(string, char):
    string = string.replace(char, '', 1)
    string = string[:string.rfind(char)] + string[string.rfind(char)+1:]
    return string

print(remove_Occ("hello", "l"))

"""
This solution will output:
'heo'
"""

# OR 

def remove_Occ(string, char):
    string = string.replace(char, '', 1)
    string = string.replace(char, '', string.count(char))
    return string

print(remove_Occ("hello", "l"))

"""
This solution will output:
'heo'
"""
<jupyter_output>
heo
heo
heo
heo
<jupyter_text>
