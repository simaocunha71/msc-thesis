from itertools import islice

def is_samepatterns(str_list1, str_list2):
    return all(str_list1[i] == str_list2[i] for i in range(len(str_list1)))

#assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True

#assert is_samepatterns(["red","green","blue"], ["a", "b", "c"])==False

#assert is_samepatterns(["red","green","blue"], ["a", "a", "c"])==False

#assert is_samepatterns(["red","green","blue"], ["a", "c"])==False

#assert is_samepatterns(["red","green"], ["a", "b"])==False

#assert is_samepatterns(["red","green"], ["a", "a"])==False


"""
def is_samepatterns(str_list1, str_list2):
    return all(str_list1[i] == str_list2[i] for i in range(len(str_list1)))
"""

"""
def is_samepatterns(str_list1, str_list2):
    for i in range(len(str_list1)):
        if str_list1[i] != str_list2[i]:
            return False
    return True
"""

"""
def is_samepatterns(str_list1, str_list2):
    for i in range(len(str_list1)):
        if str_list1[i] != str_list2[i]:
            return False
    return True
"""

"""
def is_samepatterns(str_list1, str_list2):
    return len(set(str_list1) & set(str_list2)) == len(set(str_list1))
"""

"""
def is_samepatterns(str_list1, str_list2):
    return len(str_list1) == len(str_list2) and all(str_list1[i] == str_list2[i] for i in range(len(