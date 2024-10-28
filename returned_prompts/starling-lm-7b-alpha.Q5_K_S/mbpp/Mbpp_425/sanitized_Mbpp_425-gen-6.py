def count_element_in_list(list1,element):
    count=0
    for i in list1:
        if element in i:
            count+=1
    return count