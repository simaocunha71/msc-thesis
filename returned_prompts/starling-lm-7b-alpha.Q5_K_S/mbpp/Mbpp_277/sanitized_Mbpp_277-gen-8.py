def dict_filter(dictionary,n):
    new_dictionary={}
    for i in dictionary:
        if dictionary[i]>=n:
            new_dictionary[i]=dictionary[i]
    return new_dictionary