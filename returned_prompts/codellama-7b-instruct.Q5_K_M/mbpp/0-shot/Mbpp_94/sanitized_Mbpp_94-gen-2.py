def index_minimum(my_list):
    minimum = float('inf')
    minimum_index = None
    for i, (name, age) in enumerate(my_list):
        if age < minimum:
            minimum = age
            minimum_index = i
    return my_list[minimum_index][0]