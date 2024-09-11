def right_insertion(list1,value):
    insert_index = 0
    while insert_index<len(list1) and list1[insert_index]<value:
        insert_index+=1
    return insert_index