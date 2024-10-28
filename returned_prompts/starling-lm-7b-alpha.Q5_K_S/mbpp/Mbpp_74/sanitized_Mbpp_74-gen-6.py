from itertools import islice
def is_samepatterns(str_list1, str_list2):
    return all(str_list1[i] == str_list2[i] for i in range(len(str_list1)))