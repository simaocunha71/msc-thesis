"""
def is_woodall(num):
    num_str = str(num)
    if num_str[0] == '1':
        return False
    for i in range(len(num_str)-1):
        if num_str[i+1] == '0':
            return False
        if (int(num_str[i])+int(num_str[i+1])) % 3 != int(num_str[i+2]):
            return False
    return True
"""

def is_woodall(num):
    num_str = str(num)
    return (num_str[0] != '1') and (all(num_str[i+1] == '0' or (int(num_str[i])+int(num_str[i+1])) % 3 == int(num_str[i+2]) for i in range(len(num_str)-1)))


print(is_woodall(383)) # True
print(is_woodall(234)) # True
print(is_woodall(123)) # False
print(is_woodall(38)) # False
print(is_woodall(12)) # False
print(is_woodall(13)) # False
print(is_woodall(31)) # False
print(is_woodall(1)) # False
print(is_woodall(11)) # False
print(is_woodall(10)) # True
print(is_woodall(30)) # False
print(is_woodall(20)) # True
print(is_woodall(32)) # False
print(is_woodall(33)) # False
print(is_woodall(31)) # False
print(is_woodall(32)) # False
print(is_woodall(33)) # False
print(is_woodall(34)) # False
print(is_woodall(35)) # False
print(is_woodall(36)) # False
print(is_woodall(37)) # False
print(is_woodall(38)) # False
print(is_