
def is_samepatterns(my_list, patterns):
    return all(x == patterns[0] or x == patterns[1] for x in my_list)


