def remove_Occ(string,character):
    return string[string.index(character)+1:len(string)-string[::-1].index(character)]

print(remove_Occ("hello","l"))




"""

def remove_Occ(string,character):
    string_list = list(string)
    for i in range(len(string_list)):
        if string_list[i] == character:
            if i == 0:
                string_list.pop(i)
                break
            else:
                string_list.pop(i)
                break

    for i in range(len(string_list)-1,-1,-1):
        if string_list[i] == character:
            if i == len(string_list)-1:
                string_list.pop(i)
                break
            else:
                string_list.pop(i)
                break
    return ''.join(string_list)

print(remove_Occ("hello","l"))
"""


"""
def remove_Occ(string,character):
    left = string.find(character)
    right = string.rfind(character)
    if left != right:
        if left == 0:
            return string[left+1:right]
        elif right == len(string)-1:
            return string[left+1:right]
        else:
            return string[left+1:right-1]
    else:
        return string

print(remove_Occ("hello","l"))
"""

"""
def remove_Occ(string,character):
    left = string.find(character)
    right = string.rfind(character)
    if left != right:
        if left == 0:
            return string[left+1:right]
        elif right == len(string)-1:
            return string[left:right-1]
        else:
            return string[left+1:right-1]
    else:
        return string

print(remove_Occ("hello","l"))
"""

"""
def remove_Occ(string,character):
    left = string.find(character)