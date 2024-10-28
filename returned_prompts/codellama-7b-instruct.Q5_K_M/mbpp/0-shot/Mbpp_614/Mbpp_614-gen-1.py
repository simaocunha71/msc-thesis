
def cummulative_sum(tuple_list):
    return sum(sum(t) for t in tuple_list)

# This is more readable
def cummulative_sum(tuple_list):
    return sum(sum(sub_list) for sub_list in tuple_list)

# This is less readable
def cummulative_sum(tuple_list):
    return sum(map(sum, tuple_list))
