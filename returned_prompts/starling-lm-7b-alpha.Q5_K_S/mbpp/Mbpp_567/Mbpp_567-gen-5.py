def issort_list(input_list):
    for x in range(len(input_list)-1):
        if input_list[x+1] < input_list[x]:
            return False
    return True

# Test
print(issort_list([1,2,4,6,8,10,12,14,16,17]))
# True

# Test
print(issort_list([1,3,4,6,8,10,12,14,16,17]))
# False




















"""
def issort_list(input_list):
    for x in range(len(input_list)-1):
        if input_list[x+1] < input_list[x]:
            return False
    return True



def issort_list(input_list):
    for x in range(len(input_list)-1):
        if input_list[x+1] > input_list[x]:
            return False
    return True



def issort_list(input_list):
    for x in range(len(input_list)-1):
        if input_list[x+1] < input_list[x]:
            return False
    return True



def issort_list(input_list):
    for x in range(len(input_list)-1):
        if input_list[x+1] > input_list[x]:
            return False
    return True
"""
"""
def issort_list(input_list):
    for x in range(len(input_list)-1):
        if input_list[x+1] > input_list[x]:
            return False
    return True


def issort_list(input_list):
    for x in range(len(input_list)-1):
        if input_list[x+1] < input_list[x]:
            return False
    return True
"""
"""
def issort_list(input_list):
    for x in range(len(input_list)-1):
       