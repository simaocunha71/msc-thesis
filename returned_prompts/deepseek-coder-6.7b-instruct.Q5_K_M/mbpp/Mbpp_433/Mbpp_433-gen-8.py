def find_unique_elements(array):
    count_dict = {}
    for i in array:
        if i in count_dict:
            count_dict[i