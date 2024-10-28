def dict_filter(my_dict,n):
    new_dict={}
    for key,value in my_dict.items():
        if value>=n:
            new_dict[key]=value
    return new_dict