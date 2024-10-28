def remove_kth_element(input_list,k):
    return [x for i,x in enumerate(input_list) if i!=k-1]