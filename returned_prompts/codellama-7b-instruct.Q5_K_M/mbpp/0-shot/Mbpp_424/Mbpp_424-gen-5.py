def extract_rear(my_tuple):
    rear_tuple = ()
    for i in my_tuple:
        rear_tuple += (i[-1],)
    return rear_tuple


