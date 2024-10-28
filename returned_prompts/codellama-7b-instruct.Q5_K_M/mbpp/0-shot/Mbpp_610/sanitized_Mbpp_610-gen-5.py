def remove_kth_element(my_list,k):
    if k<0 or k>=len(my_list):
        return my_list
    else:
        return [i for i in my_list if i!=my_list[k]]